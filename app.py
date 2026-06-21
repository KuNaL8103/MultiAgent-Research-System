import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="ResearchMind", page_icon="🔬", layout="wide")
st.title("🔬 ResearchMind")
st.caption("Multi-agent AI research system")

topic = st.text_input("Research Topic", placeholder="e.g. Quantum computing breakthroughs in 2025")

if st.button("Run Research Pipeline"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Running pipeline… this may take 1–2 minutes"):
            result = run_research_pipeline(topic)

        st.subheader("Final Report")
        st.markdown(result["report"])

        st.subheader("Critic Feedback")
        st.markdown(result["feedback"])

        with st.expander("Raw search results"):
            st.text(result["search_results"])

        with st.expander("Scraped content"):
            st.text(result["scraped_content"])