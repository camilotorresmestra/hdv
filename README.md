# HDV

Hijo de la V... is a simple Gradio script to render my CV (HojaDeVida) in a web interface, I basically pipe whatever chatgpt generates into a Gradio app. It runs in rendercv

## TODO: 

- Deploy in the web (private access)
- Find a way to pipe the output from chatgpt to the app automatically

## How to run

IF this is the very first time you run the app, please install the dependencies.
Since Im using `uv` I can do: `uv sync` to install everything.

Then just run:

```bash
uv run python app.py
```

Everything should work out of the box.