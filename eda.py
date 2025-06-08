import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def run_eda(df):
    st.write("### Generating Profiling Report...")
    profile = ProfileReport(df, explorative=True)
    st_profile_report(profile)
