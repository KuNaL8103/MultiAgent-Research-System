# ResearchMind — Multi-Agent Research System

Four AI components collaborate to research any topic:
1. **Search Agent** — Tavily web search
2. **Reader Agent** — Scrapes top URL for depth
3. **Writer Chain** — Drafts structured report
4. **Critic Chain** — Scores and reviews report

## Setup
pip install -r requirements.txt
cp .env.example .env   # add GROQ_API_KEY and TAVILY_API_KEY

## Run CLI
python pipeline.py

## Run Web UI
streamlit run app.py