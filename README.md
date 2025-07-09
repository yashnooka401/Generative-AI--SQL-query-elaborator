# 🧠 GenSQLProc: Generative AI-Powered SQL Stored Procedure Elaborator

## 📌 Project Overview

**GenSQLProc** is a Generative AI-based tool designed to automatically **analyze SQL stored procedures**, extract **step-by-step summaries**, and generate:

- 🧾 **Functional and Technical Requirements**
- 🔁 **Execution Flow Diagrams**
- 📊 **Entity-Relationship (ER) Diagrams**

This project bridges the gap between technical SQL code and business understanding, aiding developers, analysts, and documentation teams in reverse-engineering, modernizing, or understanding legacy stored procedures.

---

## 🎯 Features

- 🔍 **Stored Procedure Analysis**: Reads `.sql` files and extracts structured logic using LLMs (e.g., GPT-4 or local LLMs).
- 📄 **Step-wise Summarization**: Explains each SQL operation clearly in natural language.
- 📑 **Requirements Generation**:
  - **Functional Requirements** (FR)
  - **Technical Requirements** (TR)
- 📈 **Flowchart Generation**: Visualizes stored procedure logic and flow control.
- 🧬 **ER Diagram Generation**: Builds ER diagrams from table usage, joins, and relationships.
- 🛠️ **Local & API-based Models**: Works with both OpenAI APIs or local LLMs (e.g., LLaMA, Mistral).
