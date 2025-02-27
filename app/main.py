from youtube_transcript_api import YouTubeTranscriptApi

def main():
    get_transcript()

def get_transcript():
    transcript = YouTubeTranscriptApi.get_transcript("GZbeL5AcTgw")
    transcript_text = get_transcript_text(transcript)
    write_transcript(transcript_text)

def get_transcript_text(transcript):
    transcript_text_list = []
    for dict in transcript:
        text = dict["text"]
        transcript_text_list.append(text)
    transcript_text_list = ("\n").join(transcript_text_list)
    return transcript_text_list

def write_transcript(transcript):
    with open("filename.txt", "w") as file:
        file.write(transcript)
        file.close()

if __name__ == "__main__":
    main()