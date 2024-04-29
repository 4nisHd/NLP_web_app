from flask import Blueprint, request, jsonify
from flask_cors import CORS
from transformers import pipeline
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

text_generation_blueprint = Blueprint('text_gen', __name__)
CORS(text_generation_blueprint)

text_generation_pipeline = pipeline("text-generation", model="akhooli/gpt2-small-arabic")

@text_generation_blueprint.route('/api/text-generation/', methods=['POST'])
def text_gen():
    data = request.get_json()
    button_click = data.get('buttonClick')
    text_data = data.get('textData', '')
    
    if is_valid(text_data):  # Call the is_valid method on the TextValidator instance
        if button_click == 'generate' and text_data:
            generated_text = text_generation_pipeline(text_data)
            return jsonify({"generated_text": generated_text})
        else:
            return jsonify({"generated_text": "Text could not be generated."})
    else:
        return jsonify({"generated_text": "Only Arabic text is accepted."})

