import json
from typing import Dict, Any, List
from .gemini_service import extract_structured_data, get_gemini_model

def generate_career_roadmap(current_skills: List[str], target_role: str, missing_skills: List[str]) -> Dict[str, Any]:
    """
    Generate a phased learning roadmap to transition to a target career using Gemini.
    """
    model = get_gemini_model()
    if not model:
        return _fallback_roadmap(target_role, missing_skills)

    schema = {
        "type": "object",
        "properties": {
            "target_role": {"type": "string"},
            "estimated_months": {"type": "integer"},
            "timeline": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "phase": {"type": "string", "description": "e.g., Beginner, Intermediate, Advanced"},
                        "duration": {"type": "string", "description": "e.g., 4 weeks"},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "topics": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "project_idea": {"type": "string"}
                    }
                }
            }
        },
        "required": ["target_role", "estimated_months", "timeline"]
    }
    
    prompt_text = f"Create a step-by-step learning roadmap for a candidate transitioning to a '{target_role}'.\n"
    prompt_text += f"The candidate already knows: {', '.join(current_skills)}.\n"
    prompt_text += f"They need to learn: {', '.join(missing_skills)}.\n"
    prompt_text += "Generate a timeline with clear phases (Beginner, Intermediate, Advanced), durations, topics to cover, and a practical project idea for each phase."
    
    result = extract_structured_data(prompt_text, schema)
    
    if not result or "timeline" not in result:
        return _fallback_roadmap(target_role, missing_skills)
        
    return result

def _fallback_roadmap(target_role: str, missing_skills: List[str]) -> Dict[str, Any]:
    """Fallback roadmap if Gemini API is missing."""
    timeline = []
    
    if missing_skills:
        half = max(1, len(missing_skills) // 2)
        beginner = missing_skills[:half]
        advanced = missing_skills[half:]
        
        timeline.append({
            "phase": "Phase 1: Fundamentals",
            "duration": "4-6 weeks",
            "title": f"Mastering Basics for {target_role}",
            "description": "Start by learning the core foundational skills.",
            "topics": beginner,
            "project_idea": f"Build a simple application utilizing {beginner[0]}." if beginner else "Introductory project."
        })
        
        if advanced:
            timeline.append({
                "phase": "Phase 2: Advanced Topics",
                "duration": "6-8 weeks",
                "title": f"Deep Dive into {target_role}",
                "description": "Move on to advanced concepts and frameworks.",
                "topics": advanced,
                "project_idea": f"Create a comprehensive project incorporating {advanced[0]}."
            })
            
    return {
        "target_role": target_role,
        "estimated_months": 3,
        "timeline": timeline
    }
