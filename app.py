# Main module
# Imports
import time
import streamlit as st
import streamlit.components.v1 as components
from src.config import load_environment, FAV_ICON_URL
from src.llm.processor import summarize, custom_response
from warnings import filterwarnings
filterwarnings("ignore")

# Helper function to simulate streaming word-by-word
def stream_text(text, delay=0.02):
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)
    if "\n" in text:
        yield ""

def play_ping_sound():
    try:
        # Option 1: local file (put your own ping.mp3 in assets/)
        ping_file = "assets/ping.mp3"
        with open(ping_file, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mpeg", autoplay=True)
    except FileNotFoundError:
        # Option 2: fallback – Web Audio beep (works after user click)
        components.html("""
            <script>
                (function() {
                    try {
                        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                        var oscillator = audioCtx.createOscillator();
                        var gainNode = audioCtx.createGain();
                        oscillator.connect(gainNode);
                        gainNode.connect(audioCtx.destination);
                        oscillator.frequency.value = 880;   // high 'ping' tone
                        gainNode.gain.value = 0.2;
                        oscillator.type = 'sine';
                        oscillator.start();
                        gainNode.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + 0.3);
                        oscillator.stop(audioCtx.currentTime + 0.3);
                        audioCtx.resume();
                    } catch(e) {
                        console.log("Web Audio not supported – add a custom ping.mp3 to assets/");
                    }
                })();
            </script>
        """, height=0)
    except Exception:
        # Silent fail – no sound
        pass

def main():
    # Page configuration
    st.set_page_config(page_title="Website Summary AI App", page_icon=FAV_ICON_URL, layout="centered")

    # Load the API key
    api_key = load_environment()
    if not api_key:
        st.error("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
    elif not api_key.startswith("sk-proj-"):
        st.error("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
    elif api_key.strip() != api_key:
        st.error("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
    else:
        st.success("API key found and looks good so far!")

    st.title("Website Summary AI App")
    st.write("Welcome to the Website Summary App! Enter a URL below to get a summary.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter website URL..."):
        # Play the ping sound (Messenger style)
        play_ping_sound()

        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            try:
                # Check if the input looks like a URL
                if prompt.strip().startswith("http://") or prompt.strip().startswith("https://"):
                    full_response = summarize(prompt, ctr=False)
                else:
                    full_response = custom_response(prompt) + "\n\n(Note: For website summaries, please enter a valid URL starting with http:// or https://)"

                # Stream the response word by word
                st.write_stream(stream_text(full_response))
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()