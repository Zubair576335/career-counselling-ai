import json
from typing import Dict, Any, List
from .gemini_service import extract_structured_data, get_gemini_model

def analyze_skill_gap(current_skills: List[str], target_role: str) -> Dict[str, Any]:
    """
    Compare current skills with a target role and generate a skill gap report using Gemini.
    """
    model = get_gemini_model()
    if not model:
        # Fallback to simple set comparison if Gemini is not available
        return _fallback_gap_analysis(current_skills, target_role)

    schema = {
        "type": "object",
        "properties": {
            "target_role": {"type": "string"},
            "readiness_score": {
                "type": "integer",
                "description": "A percentage from 0 to 100 indicating how ready the candidate is for the target role."
            },
            "matching_skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Skills the candidate already possesses that match the target role's requirements."
            },
            "missing_skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Critical, highly specific industry skills required for the role that the candidate lacks. Avoid generic soft skills like 'Communication' unless strictly necessary."
            },
            "recommended_next_roles": {
                "type": "array",
                "items": {"type": "string"},
                "description": "1 to 3 related roles the candidate might easily transition into or target next."
            },
            "learning_difficulty": {
                "type": "string",
                "description": "E.g., 'Easy', 'Medium', 'Hard'."
            },
            "estimated_time_to_transition": {
                "type": "string",
                "description": "E.g., '3-6 months', '1-2 years'."
            },
            "salary_insights": {
                "type": "string",
                "description": "A brief, realistic statement about the average salary or earning potential for this role."
            },
            "career_growth_outlook": {
                "type": "string",
                "description": "A brief statement on the market demand and future outlook for this role."
            },
            "suggested_projects": {
                "type": "array",
                "items": {"type": "string"},
                "description": "2-3 highly specific portfolio projects to build the missing skills."
            },
            "recommended_certifications": {
                "type": "array",
                "items": {"type": "string"},
                "description": "1-3 industry-recognized certifications to acquire."
            },
            "recommendations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "skill": {"type": "string"},
                        "resource_name": {"type": "string"},
                        "resource_type": {"type": "string", "description": "e.g., Course, YouTube, Documentation"},
                        "reason": {"type": "string"}
                    }
                }
            }
        },
        "required": ["target_role", "readiness_score", "matching_skills", "missing_skills", "recommended_next_roles", "learning_difficulty", "estimated_time_to_transition", "salary_insights", "career_growth_outlook", "suggested_projects", "recommended_certifications", "recommendations"]
    }
    
    prompt_text = f"Perform a highly accurate, role-specific skill gap analysis for a candidate aiming to become a '{target_role}'.\n"
    prompt_text += f"The candidate currently has the following skills: {', '.join(current_skills)}.\n\n"
    prompt_text += "CRITICAL INSTRUCTIONS:\n"
    prompt_text += "1. Enforce strict, realistic, and highly technical industry requirements for the given role. Do NOT output generic skills like 'Problem Solving' or 'Communication'. Only output specific tools, frameworks, and languages.\n"
    prompt_text += "2. Perform semantic skill matching. For example, if the candidate has 'JS' or 'React.js', treat it as 'JavaScript' or 'React'. Do not say they are missing 'JavaScript' if they have 'JS'.\n"
    prompt_text += "3. Make sure the missing skills are uniquely required for this specific role and aren't just generic tech buzzwords.\n"
    prompt_text += "4. Fill in realistic data for salary insights, career outlook, difficulty, and transition time based on the magnitude of the skill gap.\n"
    
    result = extract_structured_data(prompt_text, schema)
    
    if not result or "readiness_score" not in result:
        return _fallback_gap_analysis(current_skills, target_role)
        
    return result

def _fallback_gap_analysis(current_skills: List[str], target_role: str) -> Dict[str, Any]:
    """Fallback gap analysis if Gemini API is missing."""
    role_skills = {
        "data scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Data Visualization", "Pandas", "NumPy", "TensorFlow"],
        "ai engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "NLP", "LLMs", "LangChain"],
        "full stack developer": ["JavaScript", "HTML", "CSS", "React", "Node.js", "SQL", "Git", "TypeScript"],
        "devops engineer": ["Linux", "Docker", "Kubernetes", "CI/CD", "AWS", "Terraform", "Python", "Jenkins"],
        "cybersecurity analyst": ["Network Security", "Linux", "Python", "SIEM", "Incident Response", "Cryptography", "Ethical Hacking", "Wireshark"],
        "cloud engineer": ["AWS", "Azure", "Linux", "Docker", "Networking", "Python", "Terraform", "Kubernetes"],
        "software engineer": ["Java", "Python", "C++", "Data Structures", "Algorithms", "Git", "SQL", "System Design"],
        "frontend developer": ["HTML", "CSS", "JavaScript", "React", "Tailwind CSS", "TypeScript", "Responsive Design"],
        "backend developer": ["Python", "Node.js", "Java", "SQL", "NoSQL", "REST APIs", "Docker", "Redis"],
        "ml engineer": ["Python", "Machine Learning", "Scikit-Learn", "TensorFlow", "PyTorch", "SQL", "Docker", "MLOps"],
        "data analyst": ["SQL", "Excel", "Tableau", "Power BI", "Python", "Data Cleaning", "Statistics"],
        "ui/ux designer": ["Figma", "Adobe XD", "Wireframing", "Prototyping", "User Research", "HTML", "CSS"],
        "mobile app developer": ["Swift", "Kotlin", "React Native", "Flutter", "Mobile UI", "APIs"],
        "blockchain developer": ["Solidity", "Smart Contracts", "Ethereum", "Cryptography", "Web3.js", "Rust"],
        "game developer": ["C++", "C#", "Unity", "Unreal Engine", "3D Math", "Game Physics"],
        "qa engineer": ["Selenium", "Cypress", "Postman", "Python", "Java", "Test Automation", "JIRA"],
        "product manager": ["Agile", "Scrum", "JIRA", "Data Analysis", "Wireframing", "A/B Testing", "Market Research"],
        "business analyst": ["SQL", "Excel", "Visio", "Tableau", "Requirements Gathering", "Process Modeling"],
        "database administrator": ["SQL Server", "Oracle", "MySQL", "PostgreSQL", "Database Tuning", "Backup & Recovery", "Linux"],
        "network engineer": ["Cisco", "Routing", "Switching", "Firewalls", "TCP/IP", "VPN", "Wireshark"],
        "prompt engineer": ["LLMs", "NLP", "Python", "Few-Shot Prompting", "Chain of Thought", "OpenAI API"],
        "generative ai engineer": ["Python", "PyTorch", "Transformers", "LLMs", "LangChain", "Vector Databases", "RAG"],
        "mlops engineer": ["Python", "Docker", "Kubernetes", "CI/CD", "MLflow", "AWS", "Terraform", "Model Deployment"]
    }
    
    target_role_lower = target_role.lower()
    required = role_skills.get(target_role_lower, ["Python", "JavaScript", "SQL", "Git", "Agile"])
    
    current_lower = [s.lower() for s in current_skills]
    
    matching = [s for s in required if s.lower() in current_lower]
    missing = [s for s in required if s.lower() not in current_lower]
    
    score = int((len(matching) / max(len(required), 1)) * 100)
    
    recommendations = []
    for m in missing:
        recommendations.append({
            "skill": m,
            "resource_name": f"Master {m}",
            "resource_type": "Course",
            "reason": f"Core requirement for {target_role}"
        })
        
    difficulty = "Medium" if score > 40 else "Hard"
    time_to_transition = "3-6 months" if score > 60 else "6-12 months"
        
    return {
        "target_role": target_role,
        "readiness_score": score,
        "matching_skills": matching,
        "missing_skills": missing,
        "recommended_next_roles": ["Related Tech Role 1", "Related Tech Role 2"],
        "learning_difficulty": difficulty,
        "estimated_time_to_transition": time_to_transition,
        "salary_insights": "Average salary varies by location and experience, typically ranging from $80k to $150k+.",
        "career_growth_outlook": "High demand with excellent growth opportunities.",
        "suggested_projects": ["Build a full-stack CRUD app", "Contribute to open source", "Deploy an app to AWS/GCP"],
        "recommended_certifications": ["AWS Certified Solutions Architect", "Google Professional Developer"],
        "recommendations": recommendations
    }

