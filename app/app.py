import streamlit as st
from streamlit_chat import message
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

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Streamlit Chat - Demo")
st.markdown("[Github](https://github.com/kobrinartem/chatgpt-streamlit-demo)")

if 'polly' not in st.session_state:
    st.session_state['polly'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(message):
	response = openai.Completion.create(engine="text-davinci-003", prompt=message, max_tokens=256, temperature=0.5, frequency_penalty=1, presence_penalty=1).choices[0]
	return response.text

def get_text():
    message = st.text_input('You:')
    return message 

# Get the user's message
user_input = get_text()

if user_input:
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    
    # Synthesize the response to speech
    synthesis_response = polly.synthesize_speech(Text=output, VoiceId='Joanna', OutputFormat='mp3')
 
    # Get the audio stream from the synthesis response
    audio_stream = synthesis_response['AudioStream']
    
    # Convert the audio stream to a bytes object
    audio_bytes = audio_stream.read()
    
    # Play the audio
    # st.audio(audio_bytes)
    st.session_state.polly.append(audio_bytes)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.text(f'Bot: {st.session_state["generated"][i]}')
        st.text(f'Bot Audio: ')
        st.audio(st.session_state["polly"][i])
        st.text(f'You: {st.session_state["past"][i]}')






