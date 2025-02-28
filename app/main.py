from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")


def main():
    transcript = get_transcript()
    write_content_to_file("transcript.txt", transcript)
    print("Fetched transcript")
    client = setup_gemini_client()
    print("Making a call to Gemini to fetch the summary")
    summarized_transcript = get_summarized_transcript(client, transcript)
    write_content_to_file("summary.txt", summarized_transcript)
    print("Summary written in the file")


def get_transcript():
    transcript = YouTubeTranscriptApi.get_transcript("3Kqal7QaCCM")
    transcript_text = get_transcript_text(transcript)
    return transcript_text


def get_transcript_text(transcript):
    transcript_text_list = []
    for dict in transcript:
        text = dict["text"]
        transcript_text_list.append(text)
    transcript_text_list = ("\n").join(transcript_text_list)
    return transcript_text_list


def write_content_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)
        file.close()


def setup_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client


def get_summarized_transcript(client, transcript):
    content = "Summarize this text in an easy to read format" + transcript
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
    )
    return response.text


if __name__ == "__main__":
    main()
