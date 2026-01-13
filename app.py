import base64
import gradio as gr

# Pre-baked PDF (base64) that will be shown on the right panel.
PDF_BASE64 = (
    "JVBERi0xLjQKJeLjz9MKMSAwIG9iago8PCAvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFIg"
    "Pj4KZW5kb2JqCjIgMCBvYmoKPDwgL1R5cGUgL1BhZ2VzIC9LaWRzIFszIDAgUl0gL0NvdW50"
    "IDEgPj4KZW5kb2JqCjMgMCBvYmoKPDwgL1R5cGUgL1BhZ2UgL1BhcmVudCAyIDAgUiAvTWVk"
    "aWFCb3ggWzAgMCA2MTIgNzkyXSAvQ29udGVudHMgNCAwIFIgL1Jlc291cmNlcyA8PCAvRm9u"
    "dCA8PCAvRjEgNSAwIFIgPj4gPj4gPj4KZW5kb2JqCjQgMCBvYmoKPDwgL0xlbmd0aCA0MyA+"
    "PgpzdHJlYW0KQlQKL0YxIDE4IFRmCjEwMCA3MDAgVGQKKEhlbGxvIFBERikgVGoKRVQKZW5k"
    "c3RyZWFtCmVuZG9iago1IDAgb2JqCjwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL05h"
    "bWUgL0YxIC9CYXNlRm9udCAvSGVsdmV0aWNhPj4KZW5kb2JqCnhyZWYKMCA2CjAwMDAwMDAw"
    "MCA2NTUzNSBmIAowMDAwMDAwMTEgMDAwMDAgbiAKMDAwMDAwMDYwIDAwMDAwIG4gCjAwMDAw"
    "MDA5OCAwMDAwMCBuIAowMDAwMDAxNzggMDAwMDAgbiAKMDAwMDAwMjk3IDAwMDAwIG4gCnRy"
    "YWlsZXIKPDwgL1NpemUgNiAvUm9vdCAxIDAgUiAvSW5mbyA8PCAvQ3JlYXRvciAoRXhhbXBs"
    "ZSkgPj4gPj4Kc3RhcnR4cmVmCjQ1MwolJUVPRgo="
)

def render_pdf(_text: str) -> str:
    """Return HTML that embeds the PDF for preview."""
    return (
        "<iframe "
        f'src="data:application/pdf;base64,{PDF_BASE64}" '
        'style="width:100%;height:600px;" '
        'type="application/pdf"></iframe>'
    )

with gr.Blocks(title="PDF Preview App") as demo:
    with gr.Row():
        with gr.Column(scale=1):
            user_text = gr.Textbox(label="Input", lines=4, placeholder="Type something...")
            run_btn = gr.Button("Render PDF", variant="primary")
        with gr.Column(scale=2):
            pdf_view = gr.HTML(label="PDF Preview")

    run_btn.click(render_pdf, inputs=user_text, outputs=pdf_view)

if __name__ == "__main__":
    demo.launch()