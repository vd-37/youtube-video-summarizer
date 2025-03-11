from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from dotenv import load_dotenv
from helpers import constants
import os

load_dotenv(dotenv_path="../.env")


def get_summary(video_id, user_input):
    transcript = get_transcript(video_id)
    print("Fetched transcript")
    client = setup_gemini_client()
    print("Making a call to Gemini to fetch the summary")
    summarized_transcript = get_summarized_transcript(client, transcript, user_input)
    print("Summary written in the file")
    return summarized_transcript


def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = get_transcript_text(transcript)
    return transcript_text


def get_transcript_text(transcript):
    transcript_text_list = []
    for dict in transcript:
        text = dict["text"]
        transcript_text_list.append(text)
    transcript_text_list = ("\n").join(transcript_text_list)
    return transcript_text_list

def setup_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client


def get_summarized_transcript(client, transcript, user_input):
    if user_input == "":
        user_input = constants.DEFAULT_USER_INPUT

    content = user_input + transcript
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
    )
    return response.text
