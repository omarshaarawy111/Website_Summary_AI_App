from openai import OpenAI
from src.llm.templates import prompts_template
from src.scrapper.scraper import fetch_website_contents

# Messges of the conversation
def messages_for(website):
    prompts = prompts_template()
    return [
        {"role": "system", "content": prompts["system_prompt"]},
        {"role": "user", "content": prompts["user_prompt"] + website}
    ]

# Messege of the conversation for custom response
def messages_for_custom(user_input):
    return [
        {"role": "user", "content": user_input}
    ]

# Final result
def summarize(url, ctr=None):
    # Initialize the client inside the function so it picks up the API key loaded in app.py
    client = OpenAI()
    website = fetch_website_contents(url, verified_certificate=ctr)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

# Custom response for another cases
def custom_response(user_input):
    client = OpenAI()
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for_custom(user_input)
    )
    return response.choices[0].message.content