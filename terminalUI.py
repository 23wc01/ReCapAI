# External libraries
import os

# Local libraries & modules
from output import *
import recapai
from transcribe import aai_transcribe

# In cmd, quick setup of API key by entering: setx KEY_NAME "my_key"
ASSEMBLYAI_KEY = os.getenv('ASSEMBLYAI_KEY')

def terminal_recapai(audio_file="./upload_audio/EarningsCall.wav", output_types=["pdf","docx","txt"], recap_file_path="./output_recap/", recap_file_name="EarningsCallRecap"):
    transcript = aai_transcribe(ASSEMBLYAI_KEY, audio_file)
    recap_info = recapai.recap(transcript)
    for output_type in output_types:
        if output_type == "pdf":
          save_as_pdf(recap_info, recap_file_path, recap_file_name)
        elif output_type == "docx":
          save_as_docx(recap_info, recap_file_path, recap_file_name)
        elif output_type == "txt":
          save_as_txt(recap_info, recap_file_path, recap_file_name)
def prompt():
    run_default = input("Run default demonstration? (y/n) ")
    if run_default == "y":
        print("Demo: Recaps the EarningsCall.wav in 'upload_audio' folder & saves the resulting EarningsCallRecap file in 'output_recap' folder.")
        terminal_recapai()
    else:
        desired_output_types = []
        audio_file = input("Path to audio file. Ex: './upload_audio/':")
        for output_type in ["pdf", "docx", "txt"]:
            desired_output = input("Save recap as a ." + output_type + "? (y/n) ")
            if desired_output == "y":
                desired_output_types.append(output_type)
        recap_file_path = input("Path to store recap file. Ex: './output_recap/': ")
        recap_file_name = input("Name of recap file: ")
        terminal_recapai(audio_file, desired_output_types, recap_file_path, recap_file_name)
