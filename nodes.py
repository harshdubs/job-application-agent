import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pypdf import PdfReader
from state import AgentState


load_dotenv()

llm  = ChatGroq(
        api_key = os.environ.get("GROQ_API_KEY"),
        model = "llama-3.3-70b-versatile",
        temperature = 0)


def parse_resume(state: AgentState) -> dict:
    print(">>> Node: parse_resume running...")
    text = "" 
    reader = PdfReader(state["resume_path"])
    for page in reader.pages:
        text += page.extract_text()            
    return {"resume_text": text}


def analyze_jd(state: AgentState) -> dict:
    print(">>> Node: analyze_jd running...")
    response = llm.invoke(f"""Analyze this job description and extract the following in a structured format:
        1. Required skills
        2. Key responsibilities  
        3. Experience requirements
        4. Nice to have skills
        Job Description: {state["job_description"]}""")
    return {"job_description_output" : response.content}


def rewrite_resume(state: AgentState) -> dict:
    print(">>> Node: rewrite_resume running...")
    response = llm.invoke(f"""Rewrite the resume bullets to match the JD, keep the ATS score above 90% and format this resume like how a professional recruiter wants,
     here is the resume as {state["resume_text"]} 
    and job_description as {state["job_description_output"]}
    """)
    return {"updates": response.content}

def generate_cv(state: AgentState) -> dict:
    print(">>> Node: generate_cv running...")
    response = llm.invoke(f"""Generate a professional cover letter tailored perfectly for 
    this job description: {state["job_description_output"]} 
    and as per the content in this resume : {state["resume_text"]} """)

    return {"cover_letter" : response.content}


def score_fit(state: AgentState) -> dict:
    print(">>> Node: score_fit running...")
    response = llm.invoke(f""" Generate a summary of advantages and strong points of the applicant after comaprison of 
    resume: {state["resume_text"]} with the given job description: {state["job_description_output"]}, suggest weak points as well and whats not a good match,
    finally provide a compatibiltiy score as well to help the user take the decision whether to apply for the job or not""")

    return {"compatibility": response.content}

