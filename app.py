from flask import Flask, render_template, request
from text_summary import summarizer
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        if not rawtext.strip():  # Handle empty input
            return "Input text cannot be empty", 400
        
        summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)

        # Create audio file for the summary
        tts = gTTS(text=summary, lang='en')
        audio_file = 'static/summary.mp3'
        tts.save(audio_file)

        return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)


