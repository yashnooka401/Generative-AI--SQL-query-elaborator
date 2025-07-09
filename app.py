import streamlit as st
from PIL import Image
import time
import os

from main import analyze_stored_procedure, generate_flowchart

# Set page config
st.set_page_config(page_title="SQL Analyzer", layout="centered")

st.markdown("<h1 style='text-align: center; color: white;'>SQL QUERY ELABORATOR</h1>", unsafe_allow_html=True)

# Text area input for SQL Stored Procedure
sql_input = st.text_area("Paste your Stored Procedure here:", height=300)

# Submit button
if st.button("Analyze"):
    if not sql_input.strip():
        st.warning("Please enter a valid stored procedure.")
    else:
        with st.spinner("Analyzing the stored procedure..."):
            try:
                # Call backend function to get the LLM-based analysis
                result = analyze_stored_procedure(sql_input)

                # Show results
                st.success("Analysis complete!")

                st.subheader("🧾 Summary")
                st.write(result["summary"])

                st.subheader("🛠️ Technical Requirements")
                st.write(result["technical_requirements"])

                st.subheader("📋 Functional Requirements")
                st.write(result["functional_requirements"])

                st.subheader("🔁 Flow of Execution")
                st.write(result["steps"])

                # Generate and display flowchart
                with st.spinner("Generating flowchart..."):
                    generate_flowchart(result["steps"])
                    if os.path.exists("flowchart.png"):
                        st.image("flowchart.png", caption="Procedure Flowchart", use_column_width=True)
                    else:
                        st.warning("Flowchart generation failed.")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
