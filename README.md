# 🌐 AI Website Summarizer

A Python tool that scrapes a website's content and uses an LLM to generate a concise summary.

## 📖 What It Does

This project automatically:
1.  **Scrapes** a given URL for its main textual content.
2.  **Cleans** the HTML to extract relevant text.
3.  **Sends** the content to an LLM (e.g., OpenAI's GPT models).
4.  **Generates** a summary of the webpage.

## 🎯 Key Features

-   ✅ Scrapes content from any public URL.
-   ✅ Cleans and processes HTML to focus on main content.
-   ✅ Uses modern LLMs for high-quality summarization.
-   ✅ Simple command-line interface.

## 🛠️ Technologies Used

-   **Python 3.9+**
-   **requests** — For making HTTP requests.
-   **BeautifulSoup4** — For parsing HTML.
-   **OpenAI Python SDK** — For interacting with LLM APIs.
-   **python-dotenv** — For managing environment variables.

## 📋 Prerequisites

1.  Python 3.9 or higher.
2.  An OpenAI API key.

## 🚀 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd Website_Summary_Project
    ```

2.  **Install dependencies**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install .
    ```

3.  **Set up your API key**
    
    Create a `.env` file in the project root:
    ```
    OPENAI_API_KEY="sk-..."
    ```
    
    > ⚠️ **Never commit your `.env` file to GitHub!**

## 💡 How to Use

Run the summarizer from your terminal:

```bash
python src/main.py "https://en.wikipedia.org/wiki/Artificial_intelligence"
```

You can also specify a different model:
```bash
python src/main.py "https://www.deeplearning.ai/" --model gpt-3.5-turbo
```
