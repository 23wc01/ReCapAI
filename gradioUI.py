# External libraries
import os
import gradio

# Local libraries & modules
from output import *
import recapai
from transcribe import aai_transcribe

# In cmd, quick setup of API key by entering: setx KEY_NAME "my_key"
ASSEMBLYAI_KEY = os.getenv('ASSEMBLYAI_KEY')

def UI_recapai(audio_file, output_types, file_name="recapai"):
    print(audio_file.name)
    transcript = aai_transcribe(ASSEMBLYAI_KEY, audio_file.name)
    os.remove(audio_file.name) # Remove audio file after transcription
    recap_info = recapai.recap(transcript)
    outputs = []
    for output_type in output_types:
        if output_type == "pdf":
          outputs.append(save_as_pdf(recap_info, file_name=file_name))
        elif output_type == "docx":
          outputs.append(save_as_docx(recap_info, file_name=file_name))
        elif output_type == "txt":
          outputs.append(save_as_txt(recap_info, file_name=file_name))
    return outputs

def get_gradio_UI():
    UI = gradio.Interface(UI_recapai,
    inputs=[
            gradio.File(label="Audio File"),
            gradio.Dropdown(["pdf", "docx", "txt"], multiselect=True, label="Save As", info="Select format(s) to save recap as"),
            gradio.Textbox(label="File Name")
            ],
    outputs=gradio.File(file_count="multiple", file_types=[".txt", ".docx", ".pdf"]),
    examples=[["./upload_audio/EarningsCall.wav", "txt", "EarningsCallRecap"]]
    )
    return UI