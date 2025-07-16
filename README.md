# Reddit Persona Generator 🧠📊

## 📌 Project Overview

**Reddit Persona Generator** is a Python-based tool that extracts public activity from Reddit user profiles and uses a language model (LLM) to generate detailed user personas. It’s designed to assist researchers, marketers, and developers in understanding online user behavior, preferences, and personality traits based on publicly available data.

---

## 🔧 Features

- 🔍 Scrapes Reddit user profiles using Reddit API (via PRAW).
- 📜 Gathers data such as comments, posts, subreddits, and karma.
- 🤖 Uses LLM (e.g., OpenAI GPT) to summarize and generate a persona.
- 🧾 Outputs persona details in text format with optional citations.
- 📂 Saves results in a local `.txt` file or prints to console.

---


---
 # Project Structure
 
## 🧰 Requirements

- Python 3.10+
- OpenAI API key
- Reddit API credentials 

Install dependencies:
```bash
pip install -r requirements.txt

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_app_name

How to run this

python persona_generator.py username_here

Generating persona for u/sampleuser...

Persona Summary:
----------------
- Interests: Technology, Startups, Philosophy
- Behavior: Long-form commenter, analytical tone, curious
- Personality: INTJ-like traits, introverted, critical thinker


