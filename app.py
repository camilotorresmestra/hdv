import base64
import gradio as gr
import os
from rendercv.api import create_a_pdf_from_a_yaml_string
from rendercv.renderer.renderer import render_a_pdf_from_typst
# Pre-baked PDF (base64) that will be shown on the right panel.

import os




def save_input_as_yaml(text: str, filename = 't.yaml') -> str:
    """Persist the user text into a YAML file and return the file path."""
    with open(filename, "wb") as f:
        f.write(text.encode("utf-8"))
    return filename

def process_text(yaml_string, tickle_box=False):  # Added tickle_box argument
    # empty the typst output file if it already exists
    try:
        os.system('rm -rf rendercv_output')
        #os.mkdir('rendercv_output')
    except:
        raise Exception("Could not create test directory")
    
    if tickle_box:
         print("Tickle box is checked, appending engineering resume style.")
         with open('engineering_resume_style.yaml', 'r') as tickle_file:
             tickle_content = tickle_file.read()   
         yaml_string += "\n" + tickle_content
    
    save_input_as_yaml(yaml_string, 't.yaml')
    # concatenate the yanmlk with the engineering resume style yaml if tickle_box is checked
    os.system('cat engineering_resume_style.yaml >> t.yaml')
    # os execute rendercv render command
    os.system('rendercv render t.yaml')
    return "rendercv_output/Camilo_Torres_Mestra_CV.pdf"

    

def render_pdf(pdf_path: str = "rendercv_output/Camilo_Torres_Mestra_CV.pdf") -> str:
    """Return HTML that embeds the PDF from a file path for preview."""
    if not pdf_path:
        return "<p>No PDF path provided.</p>"

    try:
        with open(pdf_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        return f"<p>Failed to load PDF: {e}</p>"

    return (
        "<iframe "
        f'src="data:application/pdf;base64,{encoded}" '
        'style="width:100%;height:600px;" '
        'type="application/pdf"></iframe>'
    )

with gr.Blocks(title="Generate YAML") as demo:
    with gr.Row():
        with gr.Column(scale=1):
            user_text = gr.Textbox(label="Input", lines=4, placeholder="Type something...")
            run_btn = gr.Button("Render PDF", variant="primary")
        with gr.Column(scale=2):
            pdf_view = gr.HTML(label="PDF Preview")
            pdf_path = gr.State()
            run_btn.click(process_text, inputs=user_text, outputs=pdf_path).then(
                render_pdf, inputs=pdf_path, outputs=pdf_view, 
            )

if __name__ == "__main__":
    demo.launch(server_port=1000, server_name="0.0.0.0")