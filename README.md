# 🎓 Career Counselling AI
**RAG-Enhanced Career Guidance System**

An AI-powered system that provides personalized career guidance using Retrieval-Augmented Generation (RAG), combining Knowledge Graphs, Vector Databases, and Real-Time Job Market Data.

---

## � Quick Start (For Team Members)

### Prerequisites
- **Python**: 3.10 or higher
- **Git**: For cloning the repository
- **Virtual Environment**: Recommended for dependency isolation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Zubair576335/career-counselling-ai.git
cd career-counselling-ai
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py migrate
```

### Step 5: Start the Development Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```
career_counselling_ai/
├── career_advisor/          # Django app for career guidance logic
├── career_mentor_web/       # Main Django project settings
├── src/                     # Core RAG pipeline components
│   ├── pdf_parser.py       # PDF resume parsing
│   ├── rag_engine.py       # RAG retrieval logic
│   └── vector_store.py     # Vector database integration
├── templates/               # HTML templates
├── docs/                    # Project documentation
├── data/                    # Training data and resources
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🏗️ System Architecture

Our system implements a **6-component RAG pipeline**:

### **Phase A: Data Foundations**
1. **Knowledge Graph (Neo4j)** - 960 occupations + 13,485 skills
2. **Vector Database** - Semantic search for courses and job descriptions
3. **Job Market Data** - Real-time salary and demand APIs

### **Phase B: Intelligence Layer**
4. **Retrieval Engine** - Hybrid search combining all data sources
5. **LLM Generation** - Fine-tuned career counselor
6. **Fairness & Explainability** - SHAP analysis + bias monitoring

---

## 🔧 Key Features

✅ **AI-Powered Resume Analysis** - Intelligent PDF parsing with layout awareness  
✅ **Career Path Recommendations** - Personalized suggestions based on skills and goals  
✅ **Real-Time Market Data** - Live job market insights and salary trends  
✅ **Explainable AI** - SHAP-based explanations for every recommendation  
✅ **Fair Recommendations** - Demographic parity monitoring (±3pp tolerance)  
✅ **Learning Roadmaps** - Step-by-step course recommendations with budgets

---

## 📦 Dependencies Overview

### Core Framework
- **Django 5.0+** - Web framework
- **django-crispy-forms** - Form styling

### AI & RAG Components
- **langchain** - RAG orchestration framework
- **sentence-transformers** - Text embedding models
- **faiss-cpu** - Vector similarity search
- **transformers** - HuggingFace models
- **torch** - Deep learning backend

### PDF Processing
- **PyMuPDF** - Advanced PDF parsing with layout detection

### Data Processing
- **numpy, pandas** - Data manipulation
- **python-dotenv** - Environment variable management

---

## 🎬 Recording a Demo

### To record the current implementation:

1. **Start the server** (as shown above)
2. **Navigate to**: `http://127.0.0.1:8000/`
3. **Key flows to demonstrate**:
   - Upload a resume (PDF)
   - View parsed skills and experience
   - Get career recommendations
   - Explore learning paths

---

## 🔑 Environment Variables (Optional)

Create a `.env` file in the project root for API keys:

```env
# OpenAI API (for advanced features)
OPENAI_API_KEY=your_openai_api_key_here

# Google Gemini API (alternative)
GOOGLE_API_KEY=your_google_api_key_here

# Job Market APIs (for real-time data)
LINKEDIN_API_KEY=your_linkedin_key_here
GLASSDOOR_API_KEY=your_glassdoor_key_here
```

**Note**: The system works without these for basic PDF parsing and demo purposes.

---

## 🧪 Running Tests

```bash
pytest
```

Or with Django integration:
```bash
python manage.py test
```

---

## 📊 Current Implementation Status

### ✅ Completed (MVP)
- [x] PDF resume parsing with PyMuPDF
- [x] Django web interface
- [x] Basic RAG pipeline architecture
- [x] Vector store integration
- [x] Frontend templates

### 🔄 In Progress
- [ ] Job Market API integration
- [ ] Knowledge Graph (Neo4j) deployment
- [ ] LLM fine-tuning with QLoRA
- [ ] SHAP explainability dashboard

### 📋 Planned
- [ ] User authentication system
- [ ] Career progression tracking
- [ ] Interview preparation module
- [ ] Skill gap analysis reports

---

## 👥 Team

**Project Team**: Zubair Khan (1231), Saib Idris (1248), Anshu Kumar (1251), Aman Mishra (1269)  
**Mentor**: Dr. Soumi Paul  
**Institution**: Techno India University, Kolkata | CSE Department  
**Academic Year**: 2025-26

---

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:
- `COMPONENTS-PHASE-A.md` - Data foundation components
- `COMPONENTS-PHASE-B.md` - Intelligence layer components
- `JURY-SPEECH-GENAI-CONTRIBUTION.md` - Technical deep dive
- `DEPLOYMENT_GUIDE.md` - Production deployment instructions

---

## � Troubleshooting

### Common Issues:

**Issue**: `ModuleNotFoundError` when running server  
**Solution**: Ensure virtual environment is activated and dependencies installed

**Issue**: Database errors  
**Solution**: Run `python manage.py migrate` again

**Issue**: Port 8000 already in use  
**Solution**: Use a different port: `python manage.py runserver 8080`

**Issue**: PyMuPDF installation fails  
**Solution**: Try `pip install --upgrade pymupdf`

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

This is an academic project. For collaboration:
1. Create a feature branch
2. Make your changes
3. Submit a pull request
4. Coordinate with the team

---

## 📞 Contact

For questions or issues, contact:
- **Zubair Khan**: [GitHub](https://github.com/Zubair576335)
- **Project Repository**: [career-counselling-ai](https://github.com/Zubair576335/career-counselling-ai)

---

**Last Updated**: January 2026  
**Version**: MVP 1.0
