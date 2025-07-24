import os
import requests
from bs4 import BeautifulSoup
import html2text
from slugify import slugify
import re

ZENDESK_API = "https://support.optisigns.com/api/v2/help_center/articles.json"
OUTPUT_DIR = "articles_md_raw"
MAX_ARTICLES = 50

os.makedirs(OUTPUT_DIR, exist_ok=True)

def remove_images_from_markdown(md_text):
    """Remove all ![](image_url) from markdown"""
    return re.sub(r'!\[.*?\]\(.*?\)', '', md_text)

def clean_html_to_markdown(html):
    """Clean up Zendesk article HTML into readable Markdown"""
    soup = BeautifulSoup(html, "html.parser")

    # Optional: remove navigation or ads by class if needed
    for tag in soup.find_all(["nav", "footer", "aside"]):
        tag.decompose()

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.body_width = 0

    markdown = converter.handle(str(soup))
    markdown = remove_images_from_markdown(markdown)
    return markdown.strip()

def fetch_articles(limit=40):
    all_articles = []
    page = 1

    while len(all_articles) < limit:
        url = f"{ZENDESK_API}?page={page}"
        resp = requests.get(url)
        if resp.status_code != 200:
            print(f" Failed to fetch page {page}")
            break

        data = resp.json()
        articles = data.get("articles", [])
        if not articles:
            break

        all_articles.extend(articles)
        if not data.get("next_page"):
            break

        page += 1

    return all_articles[:limit]

def save_article(article):
    title = article["title"]
    html_body = article["body"]
    article_id = article["id"]
    url = f"https://support.optisigns.com/hc/en-us/articles/{article_id}"
    slug = slugify(title)

    markdown = clean_html_to_markdown(html_body)

    # Optional: add title + article URL to the top
    full_markdown = f"# {title}\n\n{markdown}\n\n---\nArticle URL: {url}\n"

    out_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_markdown)

    print(f" Saved: {slug}.md")

def main():
    print(" Fetching articles...")
    articles = fetch_articles(limit=MAX_ARTICLES)
    print(f" Fetched {len(articles)} articles")

    for article in articles:
        save_article(article)

    print(" All articles scraped and saved.")

if __name__ == "__main__":
    main()
