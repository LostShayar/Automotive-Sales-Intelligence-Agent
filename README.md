# Automotive-Sales-Intelligence-Agent
"A SQL Agent for Automotive Analytics using LangChain &amp; Llama-3."

---

## Methodology & Design Philosophy

This project adopts a **Neuro-Symbolic** approach to database interaction, addressing the limitations of standard "Text-to-SQL" models.

### 1. The Hallucination Problem
Standard LLMs often invent columns (e.g., assuming a `price` column exists when it is actually named `sellingprice`).
* **Solution:** The Agent utilizes a dynamic **Schema Introspection** step using LangChain's SQL Toolkit. Before generating a query, it "reads" the table structure (`CREATE TABLE` definitions) to ground its reasoning in actual database constraints.

### 2. Handling "Dirty Data"
Real-world automotive data is sparse and messy.
* **Strategy:** The system prompt is engineered with **Defensive SQL** instructions. It explicitly instructs the model to use `IS NOT NULL` checks for aggregation tasks, ensuring statistical accuracy without manual data cleaning.

### 3. Reasoning Loop (ReAct)
The agent follows a **Observation-Thought-Action** loop:
1.  **Thought:** "I need to compare prices between states."
2.  **Action:** Query the database schema.
3.  **Observation:** "The state column uses 2-letter codes (e.g., 'ca', 'tx')."
4.  **Final Action:** Generate the SQL query using correct codes.

---

## Future Directions

This repository represents the initial architectural proof-of-concept. Future research directions include:

* **Vector Search Integration:** Implementing a RAG pipeline (using ChromaDB) to query unstructured PDF vehicle manuals alongside the structured SQL data (e.g., *"Why is the Ford F-150 price dropping?"* + *"What are the common transmission issues listed in the manual?"*).
* **Feedback Learning:** Implementing a "Human-in-the-loop" feedback mechanism where corrected SQL queries are stored to fine-tune the model for domain-specific jargon.
* **Latency Optimization:** Exploring quantized local models (Llama-3-8B) to run the entire inference stack on edge devices without API dependencies.

---

## 📞 Contact

**Aves Abdul**
* **Research Interest:** Trustworthy AI, Machine learning, Neuro-Symbolic Systems, Agentic Workflows.
* **Profile:** https://www.linkedin.com/in/abdulaves/
