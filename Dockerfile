FROM python:3.8

# Install the dependencies
RUN pip install openai streamlit boto3

# Copy the application code to the container
COPY app /app

WORKDIR /app/

# Run the Streamlit app
CMD streamlit run app.py
