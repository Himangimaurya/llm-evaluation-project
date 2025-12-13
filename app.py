import streamlit as st
import json
from evaluator import Evaluator

st.set_page_config(page_title="LLM Evaluation Tool", layout="centered")

st.title("LLM Evaluation Tool")
st.write("Upload chat and context JSON files to evaluate LLM response.")

# File uploaders
chat_file = st.file_uploader("Upload chat.json", type=["json"])
context_file = st.file_uploader("Upload context.json", type=["json"])

if chat_file and context_file:
    try:
        chat_data = json.load(chat_file)
        context_data = json.load(context_file)

        if st.button("Evaluate"):
            evaluator = Evaluator()
            result = evaluator.evaluate_chat(chat_data, context_data)

            st.subheader("Evaluation Report")

            st.write("### Relevance Score")
            st.write(result.get("relevance_score"))

            st.write("### Completeness Score")
            st.write(result.get("completeness_score"))

            st.write("### Missing Parts")
            st.write(result.get("missing_parts"))

            st.write("### Hallucination Score")
            st.write(result.get("hallucination_score"))

            st.write("### Latency (ms)")
            st.write(result.get("latency_ms"))

            # Download report
            st.download_button(
                label="Download Report JSON",
                data=json.dumps(result, indent=2),
                file_name="report.json",
                mime="application/json"
            )

    except Exception as e:
        st.error(f"Error while processing files: {e}")
