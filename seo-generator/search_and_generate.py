import csv, os, openai
from jinja2 import Template
from config import OPENROUTER_API_KEY, MODEL_NAME

openai.api_key = OPENROUTER_API_KEY
openai.api_base = "https://openrouter.ai/api/v1"

DATA_FILE = "data/titles.csv"
OUTPUT_DIR = "outputs"
TEMPLATE_FILE = "prompts/seo_template.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_titles():
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def get_main_keyword(title: str) -> str:
    # Simple heuristic: second significant word lowercased
    return title.split()[2].lower()

def fetch_summary(query: str) -> str:
    prompt = f"Search the web and return a concise, multi-paragraph summary about: {query}"
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def render_prompt(title: str, summary: str, keyword: str) -> str:
    with open(TEMPLATE_FILE, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(title=title, search_summary=summary, main_keyword=keyword)

def generate_article(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.7
    )
    return response.choices[0].message.content

def save_article(article_id: str, content: str):
    path = os.path.join(OUTPUT_DIR, f"article-{article_id.zfill(3)}.md")
    with open(path, "w", encoding='utf-8') as f:
        f.write(content)

def main():
    rows = load_titles()
    for row in rows:
        title = row["title"]
        article_id = row["id"]
        keyword = get_main_keyword(title)
        print(f"🔍 Generating for: {title}")
        summary = fetch_summary(title)
        prompt = render_prompt(title, summary, keyword)
        article = generate_article(prompt)
        save_article(article_id, article)
        print(f"✅ Saved outputs/article-{article_id.zfill(3)}.md")

if __name__ == "__main__":
    main()
