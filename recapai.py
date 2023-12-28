import openai
from openai import OpenAI
from transcribe import aai_transcribe
import output
import os
import gradio
import shutil

#In cmd, set up each API key with command: setx "myAPIKey"
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
ASSEMBLYAI_KEY = os.getenv('ASSEMBLYAI_KEY')

# Returns a dictionary of the summaries
def recap(transcript):
    summary = summarizer(transcript)
    sentiment = sentiment_analyzer(transcript)
    key_points = key_points_extracter(transcript)
    tasks = tasks_extracter(transcript)
    return {
        "SENTIMENT": sentiment,
        "SUMMARY": summary,
        "KEY POINTS": key_points,
        "TASKS": tasks
    }
    
# Analyze tone & emotion
def sentiment_analyzer(transcript):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are an AI experienced in language and emotion analysis, analyze the sentiment of the following text. Consider overall tone of the discussion, emotion conveyed by language used, and the context in which words and phrases are used. Indicate if sentiment is positvive, negative, or neutral, and provide brief explanations for your analysis where possible."},
            {"role": "user", "content": transcript}
        ]
    )
    return completion.choices[0].message.content

# Summarize into 1 abstract paragraph
def summarizer(transcript):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a highly skilled AI trained in language comprehension and sumarization. Read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, give a coherent and readable summary that could help a person understand the main points of the disscussion without needing to read the entire text. Avoid unnecessary details or tangential points."},
            {"role": "user", "content": transcript}
        ]
    )
    return completion.choices[0].message.content

# List key points
def key_points_extracter(transcript):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a proficient AI that distills information into key points. Based on the following text, identify and list the main points that were discussed. These should be the most important ideas, finidngs, or topics that are crucial to the essence of the discussion. Your goal is to provide a list someone could scan over quickly and understand what was talked about."},
            {"role": "user", "content": transcript}
        ]
    )
    return completion.choices[0].message.content

# List action items (assignments, tasks, actions, etc.)
def tasks_extracter(transcript):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are an AI expert in analyzing conversations and extracting action items. Please review text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. List action items clearly and concisely."},
            {"role": "user", "content": transcript}
        ]
    )
    return completion.choices[0].message.content

    

#Run functions
audio_file_path = "./"
audio_file_name = "EarningsCall.wav"

transcript = aai_transcribe(ASSEMBLYAI_KEY, audio_file_path+audio_file_name)

recapped_info = recap(transcript)

output.print_recap(recapped_info)
output.save_as_docx(recapped_info, "./reacpai.docx")

"""def process_file(audio_filepath):
    path = "./" + os.path.basename(audio_filepath)  
    shutil.copyfile(audio_filepath.name, path)
    return recap(path)

getAudioFile = gradio.File(file_count="single", file_types=["audio"])
UI = gradio.Interface(process_file, getAudioFile, "file")
UI.launch()"""

    












         

