from flask import Blueprint, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from collections import defaultdict

text_summarization_blueprint = Blueprint('text_summarization', __name__)
CORS(text_summarization_blueprint)  # Enable CORS for the Blueprint

nlp = spacy.load('en_core_web_sm')
stopwords = set(STOP_WORDS)
punctuation = set(punctuation + '\n')

@text_summarization_blueprint.route('/api/text-summarization/', methods=['POST'])
def text_summarization():
    data = request.get_json()
    button_click = data.get('buttonClick')
    text_data = data.get('textData', '')
    print(type(text_data))
    if button_click == 'summarize' and text_data:
        doc = nlp(text_data)

        word_frequencies = defaultdict(int)
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                word_frequencies[word.text] += 1

        max_frequency = max(word_frequencies.values())
        word_frequencies = {word: freq / max_frequency for word, freq in word_frequencies.items()}

        sentence_scores = defaultdict(float)
        for sent in doc.sents:
            for word in sent:
                if word.text.lower() in word_frequencies:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

        select_length = int(len(list(doc.sents)) * 0.3)
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)

        final_summary = ' '.join([word.text for word in summary])
        if final_summary.strip():
            return jsonify({'paragraph': final_summary})
        else:
            return jsonify({'error': 'Summary could not be generated or is empty'})

    return jsonify({'error': 'Invalid request or missing data'})
