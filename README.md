# YouTube Video Summarizer

This is a simple Flask application that uses the YouTubeTranscriptApi and OpenAI to summarize a YouTube video's transcript.

## Prerequisites

- Python 3.6 or later
- Flask
- youtube-transcript-api
- openai

## Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

## Usage

1. Run the application using `python app.py`.
2. Visit `http://localhost:5000` in your browser.
3. Enter the YouTube URL of the video you want to summarize and click the "Summarize" button.
4. Wait for the application to summarize the video, which may take a few seconds.
5. The summarized text will be displayed on the same page.


## Credits

- [YouTubeTranscriptApi](https://github.com/jdepoix/youtube-transcript-api)
- [OpenAI API](https://openai.com/)
