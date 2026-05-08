import os
import json
import google.generativeai as genai
from typing import Dict, Any, List

def get_gemini_model(model_name="gemini-2.5-flash"):
    """Initialize and return the Gemini model."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("WARNING: GOOGLE_API_KEY environment variable not set.")
        return None
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def extract_structured_data(text: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract structured JSON data from text using Gemini.
    """
    model = get_gemini_model("gemini-2.5-flash")
    if not model:
        return {}
    
    prompt = f"""
    You are an expert data extraction assistant.
    Extract the following information from the provided text according to the JSON schema.
    Output ONLY valid JSON.
    
    JSON Schema:
    {json.dumps(schema, indent=2)}
    
    Text:
    {text}
    """
    
    try:
        # Use JSON response mime type to enforce JSON output
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error extracting data with Gemini: {e}")
        return {}

def analyze_resume_text(resume_text: str) -> Dict[str, Any]:
    """
    Analyze resume text and extract structured information including ATS score.
    """
    schema = {
        "type": "object",
        "properties": {
            "skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Comprehensive list of technical skills including frameworks, libraries, tools, databases, cloud platforms, certifications, and programming languages."
            },
            "education": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "degree": {"type": "string"},
                        "institution": {"type": "string"},
                        "year": {"type": "string"}
                    }
                }
            },
            "experience": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "role": {"type": "string"},
                        "company": {"type": "string"},
                        "duration": {"type": "string"},
                        "description": {"type": "string"}
                    }
                }
            },
            "projects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "technologies_used": {"type": "array", "items": {"type": "string"}}
                    }
                }
            },
            "ats_score": {
                "type": "integer",
                "description": "A score from 0 to 100 indicating how well formatted and rich the resume is for ATS systems."
            },
            "improvement_suggestions": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Actionable advice to improve the resume."
            }
        },
        "required": ["skills", "education", "experience", "projects", "ats_score", "improvement_suggestions"]
    }
    
    return extract_structured_data(resume_text, schema)
