import gradio as gr
from graph import app

def process( file_path, job_description):
    result = app.invoke({
    "resume_path": file_path ,
    "job_description": job_description
    })
    with open("updated_resume.txt", "w") as f:
        f.write(result["updates"])

    with open("cover_letter.txt", "w") as f:
        f.write(result["cover_letter"])
        
    return result["updates"], result["cover_letter"], result["compatibility"], "updated_resume.txt", "cover_letter.txt"

with gr.Blocks(title="Job Application Agent") as demo:
    gr.Markdown("Job Application Agent")
    resume =  gr.File(file_types=[".pdf"], label="Upload Resume (PDF)")
    job_description = gr.Textbox(label="Job Description", lines=10)
    
    
    with gr.Row():
        resume_updates = gr.Textbox(label="Updated Resume", lines=10, scale=4)
        resume_txt = gr.File(label="Download", scale=1)

    with gr.Row():
        cv = gr.Textbox(label="Cover Letter", lines=10, scale=4)
        cv_txt = gr.File(label="Download CV", scale=1)
    
    compatibility_review = gr.Textbox(label="Job Compatibility", lines=10)
    start_button = gr.Button("Start!")

    start_button.click(
    fn=process,
    inputs=[resume,job_description],
    outputs=[resume_updates, cv, compatibility_review, resume_txt,cv_txt]
    )

if __name__ == "__main__":
    demo.launch()
