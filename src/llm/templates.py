# Prompts module
system_prompt = """
You are a helpfull assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

def prompts_template(system_prompt=system_prompt, user_prompt_prefix=user_prompt_prefix):
    return {
        "system_prompt": system_prompt,
        "user_prompt": user_prompt_prefix
    }
