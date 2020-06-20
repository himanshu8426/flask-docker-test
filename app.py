# app.py - a minimal flask api using flask_restful
from flask import Flask, request, jsonify
import json
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/sentiment', methods=['GET'])
def sentiment():
    text = request.args.get('text', default='i am good', type=str)
    sa = TextBlob(text)
    if sa.sentiment.polarity > 0:
        polar = 'Positive'
    elif sa.sentiment.polarity < 0:
        polar = 'Negative'
    else:
        polar = 'Neutral'
    return jsonify({'Text' : text, 'Sentiment' : polar})
    
if __name__ == '__main__':
    app.run(port=8000, debug=True, use_reloader=False)