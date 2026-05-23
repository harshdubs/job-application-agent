import gradio as gr
from graph import app

def process( file_path, job_description):
    result = app.invoke({
    "resume_path": file_path ,
    "job_description": job_description
    })

    return result["updates"], result["cover_letter"], result["compatibility"]

with gr.Blocks(title="Job Application Agent") as demo:
    gr.Markdown("Job Application Agent")
    resume =  gr.File(file_types=[".pdf"])
    status = gr.Markdown("Upload a resume in pdf format")
    job_description = gr.Textbox(placeholder="Paste Job Description!")
    resume_updates = gr.Textbox()
    cv = gr.Textbox()
    compatibility_review = gr.Textbox()
    start_button = gr.Button("Start!")

    start_button.click(
    fn=process,
    inputs=[resume,job_description],
    outputs=[resume_updates, cv, compatibility_review]
    )

if __name__ == "__main__":
    demo.launch()
