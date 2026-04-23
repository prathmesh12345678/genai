import os
import json
from typing import Optional, Dict, List, Any
import re

class ResumeAnalyzer:
    """Resume analyzer using LLM APIs"""
    
    def __init__(self, api_provider: str = "OpenAI", model: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.api_provider = api_provider
        self.model = model
        self.temperature = temperature
        self.client = self._initialize_client()
    
    def _initialize_client(self):
        """Initialize LLM client based on provider"""
        try:
            if self.api_provider == "OpenAI":
                from openai import OpenAI
                return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            elif self.api_provider == "Anthropic":
                from anthropic import Anthropic
                return Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            else:
                return None
        except Exception as e:
            print(f"Warning: Could not initialize {self.api_provider} client: {e}")
            return None
    
    def _call_llm(self, prompt: str) -> str:
        """Call LLM with the given prompt"""
        try:
            if self.api_provider == "OpenAI" and self.client:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=2000
                )
                return response.choices[0].message.content
            elif self.api_provider == "Anthropic" and self.client:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature
                )
                return message.content[0].text
            else:
                # Fallback for testing
                return self._mock_analysis(prompt)
        except Exception as e:
            return f"Error calling LLM: {str(e)}"
    
    def _mock_analysis(self, prompt: str) -> str:
        """Mock analysis for testing without API keys"""
        return """
{
    "status": "Demo Mode",
    "message": "Please configure API keys to enable real analysis",
    "recommendations": [
        "Set up OPENAI_API_KEY or ANTHROPIC_API_KEY in .env file",
        "Check the documentation for setup instructions"
    ]
}
        """
    
    def complete_analysis(self, resume_text: str) -> Dict[str, Any]:
        """Perform complete analysis of resume"""
        prompt = f"""
Analyze the following resume and provide a comprehensive analysis in JSON format:

RESUME:
{resume_text}

Please provide:
1. Summary of the candidate
2. Key skills identified
3. Experience level assessment
4. Strengths
5. Areas for improvement
6. Recommended enhancements

Format as JSON with keys: summary, skills, experience_level, strengths, improvements, recommendations
        """
        
        result = self._call_llm(prompt)
        return self._parse_json_response(result)
    
    def extract_skills(self, resume_text: str) -> Dict[str, List[str]]:
        """Extract skills from resume"""
        prompt = f"""
Extract all skills from this resume and categorize them:

RESUME:
{resume_text}

Please provide JSON with categories like:
- technical_skills: [list of technical skills]
- soft_skills: [list of soft skills]
- tools_technologies: [list of tools/technologies]
- languages: [list of programming languages]
- other_skills: [list of other relevant skills]

Return only valid JSON.
        """
        
        result = self._call_llm(prompt)
        return self._parse_json_response(result)
    
    def get_improvements(self, resume_text: str) -> Dict[str, Any]:
        """Get improvement suggestions for resume"""
        prompt = f"""
Review this resume and provide specific improvement suggestions:

RESUME:
{resume_text}

Please provide JSON with:
- formatting_improvements: [list of formatting suggestions]
- content_improvements: [list of content suggestions]
- missing_sections: [list of sections that could be added]
- skill_gaps: [list of common skills to consider adding]
- action_items: [prioritized list of improvements]

Return only valid JSON.
        """
        
        result = self._call_llm(prompt)
        return self._parse_json_response(result)
    
    def match_job_description(self, resume_text: str, job_description: str) -> Dict[str, Any]:
        """Match resume against job description"""
        prompt = f"""
Analyze how well this resume matches the job description:

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Please provide JSON with:
- match_score: (0-100)
- matching_skills: [skills that match]
- missing_skills: [skills from job not in resume]
- matching_experience: [relevant experience sections]
- recommendations: [how to better match the role]
- confidence: (low/medium/high)

Return only valid JSON.
        """
        
        result = self._call_llm(prompt)
        return self._parse_json_response(result)
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Parse JSON from LLM response"""
        try:
            # Try to find JSON in the response
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                return json.loads(json_str)
            else:
                return {"raw_response": response}
        except json.JSONDecodeError:
            return {"raw_response": response}
        except Exception as e:
            return {"error": str(e), "raw_response": response}
