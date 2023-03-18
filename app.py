import openai
import os
from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    video_id = parse_qs(urlparse(url).query)['v'][0]
    lst = YouTubeTranscriptApi.get_transcript(video_id)
    text_lst = [d['text'] for d in lst]
    text = ' '.join(text_lst)
    length = len(text)
    bigtext = True;
    if bigtext == True:
        words = text.split()
        word_limit = 1000
        num_parts = len(words) // word_limit + 1
        parts = []
        for i in range(num_parts):
            start_index = i * word_limit
            end_index = (i + 1) * word_limit
            parts.append(' '.join(words[start_index:end_index]))

    openai.api_key = os.environ.get("API_KEY")

    if bigtext == True:
        summary_list = []
        for i, part in enumerate(parts):
            model_engine = "text-davinci-002"
            prompt = f"This text is a piece of a youtube video script. Please summarize this in depth mentioning all the main points:\n{part}\n"
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                temperature=0.5,
                max_tokens=1000,
                n=1,
                stop=None,
                timeout=20,
            )
            summary = response.choices[0].text.strip()
            summary_list.append(summary + "\n\n")  # Add two newline characters to create a blank line between key points

        summary = "".join(summary_list)  # Separate each summary with a new line


    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
