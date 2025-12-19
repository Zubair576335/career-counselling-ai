# Career Counselling AI

**An AI-powered system to provide personalized career guidance using Retrieval-Augmented Generation (RAG).**

---

## 📅 Current Progress: Week 5
**Focus: Intelligent PDF Parsing (The "Input" Layer)**

We have successfully built the "Eyes" of our AI system. Before the AI can give advice, it must first accurately "read" the student's resume.

### ✅ Achievements
*   **Built the Ingestion Module**: Created `pdf_parser.py` using **PyMuPDF**.
*   **Solved "PDF Noise"**: The system now intelligently removes headers, footers, and page numbers that confuse standard AI models.
*   **Layout Awareness**: It distinguishes between different sections (like "Education" vs. "Skills") by analyzing font sizes and layout, ensuring data is preserved in context.
*   **Frontend Integration**: Connected the Django upload interface to this backend parser.

### 🔜 Next Steps (Week 6)
*   Build the **Vector Knowledge Base** (FAISS).
*   Connect to **Google Gemini API** for reasoning.
