import streamlit as st
import openai
import boto3

# Create an SSM client using Boto3
ssm = boto3.client('ssm')

# Create a Polly client using Boto3
polly = boto3.client('polly')

# Set the OpenAI API endpoint and the name of the parameter that stores the API key in the SSM Parameter Store
api_endpoint = 'https://api.openai.com/v1/chatbot'
api_key_parameter = '/openai/api_key'

# Get the API key from the SSM Parameter Store
openai.api_key = ssm.get_parameter(Name=api_key_parameter, WithDecryption=True)['Parameter']['Value']

# Get the user's message
message = st.text_input('You:')

if message:
    st.text(f'You: {message}')
    
    # Use the OpenAI ChatGPT API to generate a response
    response = openai.Completion.create(engine="text-davinci-003", prompt=message, max_tokens=256, temperature=0.5, frequency_penalty=1, presence_penalty=1).choices[0].text
 
    # Synthesize the response to speech
    synthesis_response = polly.synthesize_speech(Text=response, VoiceId='Joanna', OutputFormat='mp3')
 
    # Get the audio stream from the synthesis response
    audio_stream = synthesis_response['AudioStream']
    
    # Convert the audio stream to a bytes object
    audio_bytes = audio_stream.read()
    
    # Play the audio
    st.audio(audio_bytes)

    # Display the response
    st.text(f'Bot: {response}')



