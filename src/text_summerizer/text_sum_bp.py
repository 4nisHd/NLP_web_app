from flask import Blueprint, request, jsonify
from flask_cors import CORS  
from transformers import BertTokenizer, AutoModelForSeq2SeqLM, pipeline
from arabert.preprocess import ArabertPreprocessor




text_summarization_blueprint = Blueprint('text_summarization', __name__)
CORS(text_summarization_blueprint) 


model_name="malmarjeh/mbert2mbert-arabic-text-summarization"

preprocessor = ArabertPreprocessor(model_name="")

tokenizer = BertTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipeline = pipeline("text2text-generation",model=model,tokenizer=tokenizer)



def is_valid(text):
    range_ = (0x0600, 0x06FF)
    supplement_range = (0x0750, 0x077F)
    extended_range = (0x08A0, 0x08FF)
    presentation_forms_a_range = (0xFB50, 0xFDFF)
    presentation_forms_b_range = (0xFE70, 0xFEFF)
    ranges = [
        range_,
        supplement_range,
        extended_range,
        presentation_forms_a_range,
        presentation_forms_b_range,
    ]

    for char in text:
        if any(start <= ord(char) <= end for start, end in ranges):
            return True
    return False



@text_summarization_blueprint.route('/api/text-summarization/', methods=['POST'])
def text_summarization():
    data = request.get_json()
    button_click = data.get('buttonClick')
    text_data = data.get('textData', '')
    if is_valid(text_data):
        if (button_click=="summarize" and text_data):
            text=preprocessor.preprocess(text_data)
            res=pipeline(text,
                         pad_token_id=tokenizer.eos_token_id,
                         num_beams=3,
                         repetition_penalty=3.0,
                         max_length=len(text),
                         length_penalty=1.0,
                         no_repeat_ngram_size=3)[0]['generated_text']
            return jsonify({'paragraph':res})
        else:
            return jsonify({'error':'Text could not be summarized.'})
    else:
        return jsonify({'error':'Text is not in arabic.'})    
