# Import local libraries & modules
from transcribe import aai_transcribe
import recapai
import output

# In cmd, quick setup of API key by entering: setx KEY_NAME "my_key"
ASSEMBLYAI_KEY = os.getenv('ASSEMBLYAI_KEY')


#Run functions
audio_file_path = "./sample_audio/"
audio_file_name = "EarningsCall.wav"

transcript = aai_transcribe(ASSEMBLYAI_KEY, audio_file_path+audio_file_name)

recapped_info = recapai.recap(transcript)

output.print_recap(recapped_info)
