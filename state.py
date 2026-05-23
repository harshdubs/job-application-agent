from typing import TypedDict

class AgentState(TypedDict):
    resume_path: str
    resume_text: str        
    job_description: str 
    job_description_output: str      
    updates: str        
    cover_letter: str        
    compatibility: str