# SEO Article Generator with OpenRouter

This repository provides a fully working Python workflow that
* reads a list of article titles,
* pulls a live web summary using an OpenRouter online model,
* renders a Jinja2 prompt,
* generates a ~2000‑word SEO‑optimized article with remio features,
* and saves each article to Markdown.

## 📋 Prerequisites
* Python ≥ 3.9
* An [OpenRouter](https://openrouter.ai) API key with access to an online/browsing model (e.g. `perplexity/llama-3-sonar-small-online`).

## 🚀 Quickstart

```bash
git clone https://github.com/yourname/seo-generator.git
cd seo-generator
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-yourkey"
python search_and_generate.py
```

Generated articles will appear in `outputs/`.

## 🔧 Project Structure
```
seo-generator/
├── config.py
├── prompts/seo_template.txt
├── search_and_generate.py
├── data/titles.csv
├── outputs/
└── requirements.txt
```

## 🛠 Configuration
Edit **`config.py`** to set:
```python
OPENROUTER_API_KEY = "your-openrouter-key"
MODEL_NAME = "perplexity/llama-3-sonar-small-online"
```

## 📰 Adding Titles
Append rows to `data/titles.csv`:

```csv
id,title
1,How to Write an A/B Test Report of Growth Product Manager With remio in 2025
2,How to Learn Product Analytics with remio in 2025
```

## 📈 Extending
* Add keyword analysis in `get_main_keyword`.
* Integrate Unsplash API for automatic images.
* Push generated content to your CMS via API.

MIT License
