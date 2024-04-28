from flask import Blueprint, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from checker import is_valid

text_generation_blueprint=Blueprint('text_gen',__name__)
CORS(text_generation_blueprint)



text_generation_pipeline = pipeline("text-generation", model="akhooli/gpt2-small-arabic")

@text_generation_blueprint.route('/api/text-generation/')
def text_gen():
    data=request.get_json()
    button_click=data.get('buttonClick')
    text_data=data.get('textData','')
    if is_valid(text_data):
        if button_click=='generate' and text_data:
            generated_text = text_generation_pipeline(text_data)
            return jsonify({"generated_text":generated_text})
        else:
            return jsonify({"generated_text": "Text could not be generated."})
    else:
        return jsonify({"generated_text":"Only arabic text is accepted."})