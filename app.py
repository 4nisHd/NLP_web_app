from flask import Flask, request, jsonify
from flask_cors import CORS

#natural language processing toolkit
from nltk import sent_tokenize


from text_summerization import (
    _create_frequency_matrix,
    _create_tf_matrix,
    _create_documents_per_words,
    _create_idf_matrix,
    _create_tf_idf_matrix,
    _score_sentences,
    _find_average_score,
    _generate_summary,
)





app = Flask(__name__)
CORS(app)

@app.route('/api/get-paragraph', methods=['POST'])



def get_paragraph():
    
    button_click = request.json.get('buttonClick')
    
    text_data = request.json.get('textData') 

    sentences = sent_tokenize(text_data)
    
    total_documents = len(sentences)
    
    freq_matrix = _create_frequency_matrix(sentences)
    
    tf_matrix = _create_tf_matrix(freq_matrix)
    
    count_doc_per_words = _create_documents_per_words(freq_matrix)
    
    idf_matrix = _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)
    
    tf_idf_matrix = _create_tf_idf_matrix(tf_matrix, idf_matrix)
    
    sentence_scores = _score_sentences(tf_idf_matrix)
    
    threshold = _find_average_score(sentence_scores)


    if button_click == "summerize":

        paragraph = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

    else:
        
        paragraph = "invalid"

    return jsonify({"paragraph": paragraph})

if __name__ == "__main__":
    app.run(debug=True)
