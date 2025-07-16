import os
import praw
import re
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def get_username_from_url(link):
    parts = link.split("/")
    return parts[-2] if parts[-1] == '' else parts[-1]

def get_data(name):
    redditor = reddit.redditor(name)
    submissions = []
    comments = []

    try:
        for post in redditor.submissions.new(limit=30):
            submissions.append(post)
        for comment in redditor.comments.new(limit=30):
            comments.append(comment)
    except:
        print("Error getting data")
    
    return submissions, comments

def get_subreddits(posts, comments):
    subreddits = []
    for post in posts:
        subreddits.append(str(post.subreddit))
    for c in comments:
        subreddits.append(str(c.subreddit))
    return subreddits

def get_keywords(texts):
    all_words = []
    for t in texts:
        words = re.findall(r'\b\w{5,}\b', t.lower())
        all_words.extend(words)
    keywords = {}
    for w in all_words:
        if w in keywords:
            keywords[w] += 1
        else:
            keywords[w] = 1
    sorted_kws = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    return [k[0] for k in sorted_kws[:5]]

def write_file(name, posts, comments, subreddits, keywords):
    with open(name + "_persona.txt", "w", encoding="utf-8") as f:
        f.write("Reddit Persona: u/" + name + "\n")
        f.write("\nAGE: Unknown\n")
        f.write("OCCUPATION: Unknown\n")
        f.write("STATUS: -\n")
        f.write("LOCATION: Active in " + ", ".join(subreddits[:3]) + "\n")
        f.write("TIER: Curious Explorer\n")
        f.write("ARCHETYPE: The Commentator\n")
        f.write("\n---------------------------\n")
        f.write("PERSONALITY\n")
        f.write("INTROVERT : ⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜\n")
        f.write("SENSING   : ⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜\n")
        f.write("THINKING  : ⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜\n")
        f.write("JUDGING   : ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛\n")

        f.write("\n---------------------------\n")
        f.write("ACTIVE SUBREDDITS:\n")
        for s in subreddits[:5]:
            f.write("- " + s + "\n")

        f.write("\n---------------------------\n")
        f.write("TOP INTERESTS:\n")
        for k in keywords:
            f.write("- " + k + "\n")

        f.write("\n---------------------------\n")
        f.write("TOP POSTS:\n")
        for p in posts[:5]:
            f.write("📝 " + p.title + "\n")
            f.write("🔗 https://reddit.com" + p.permalink + "\n\n")

        f.write("TOP COMMENTS:\n")
        for c in comments[:5]:
            txt = c.body
            f.write("💬 " + txt[:150] + "\n")
            f.write("🔗 https://reddit.com" + c.permalink + "\n\n")

def main():
    url = input("Enter Reddit profile URL: ")
    uname = get_username_from_url(url)
    posts, comments = get_data(uname)

    subreddits = get_subreddits(posts, comments)
    texts = [p.title + " " + p.selftext for p in posts] + [c.body for c in comments]
    keywords = get_keywords(texts)

    write_file(uname, posts, comments, subreddits, keywords)
    print("Done")

if __name__ == "__main__":
    main()
