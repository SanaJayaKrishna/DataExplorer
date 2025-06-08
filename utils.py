import pandas as pd
import streamlit as st

def load_data(file):
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    return df

def save_report(df, metrics, model_name):
    # Simple markdown report
    content = f"# DataExplorer Report\n\n## Model: {model_name}\n\n### Metrics:\n"
    for k, v in metrics.items():
        content += f"- {k}: {v:.4f}\n"

    content += "\n## Data Sample:\n"
    content += df.head().to_markdown()

    st.download_button(label="Download Report (Markdown)", data=content, file_name="dataexplorer_report.md", mime="text/markdown")
