import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys
import time

# upload ##################################################################

upload_endpoint = "https://api.assemblyai.com/sk/upload"
transcript_endpoint = "https://api.assemblyai/sk/trancript"

headers = {'authorization': API_KEY_ASSEMBLYAI}

filename = sys.argv[1]

filename ="/path/audiofile.wav"
def upload(): 
    def read_file(filename, chunk_size=5242880)
         with open(filename, 'rb') as _file:
            while True:
                 data = _file.read(chunck_size)
                 if not data:
                   break
                 yield data
               
    response = requests.post(upload_endpoint,
                             headers = headers,
                             data = read_file(filename))               
                         
    audio_url = response.json()['upload_url']      
    return audio_url
 
 # transcribe ##############################################################
 
def transcribe(audio_url):
    transcript_request = {"audio_url": audio_url}
    transcript_response = request.post(transcript_endpoint, json = transcript_request, header = header)
    job_id = transcript_response.json()['id']
    return job_id
 
audio_url = upload(filename)
transcript_id = transcribe(audio_url)

print(transcript_id)
     
# poll #####################################################################
 
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers = headers)
    print(polling_response)

def get_transcript_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
       data = poll(transcribe_id)
       if data['status'] == 'completed':
           return data, None
       elif data['status'] == 'error':
           return data, data['error']
       print('waiting 30 seconds....')
       time.sleep(30)    
 
 audio_url = upload(filename)
 get_transcription_result_url(audio_url)  
         

# save transcript ##########################################################
                   
def save_transcript(audio_url):
    data, error = get_transcript_result_url(audio_url)  
    
    if data:
       text_filename = filename + ".txt"
       with open(text_filename,"w") as f:
            f.write(data['text'])
       print('Transcription saved!!')
    elif error:
       print("Error!!", error)
                           
audio_url = upload(filename)
save_transcript(audio_url) 
                  
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
