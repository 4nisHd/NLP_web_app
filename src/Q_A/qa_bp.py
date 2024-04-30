from flask import Blueprint, request, jsonify
from flask_cors import CORS
#ML/LLM libraries
import torch 
from transformers import AutoTokenizer, AutoModelForCausalLM

q_a_blueprint=Blueprint("q_a_blueprint", __name__)
CORS(q_a_blueprint)

#checking if the language of the prompt is indeed Arabic
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



model_path="inception-mbzuai/jais-13b"

device="cuda" if torch.cuda.is_available() else "cpu"

tokenizer=AutoTokenizer.from_pretrained(model_path)

model=AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)


def get_response(text,tokenizer=tokenizer, model=model):
    input_ids=tokenizer(text, return_tensors="pt").input_ids
    inputs=input_ids.to(device)
    input_len=inputs.shape[-1]
    generate_ids=model.generate(
        inputs,
        top_p=0.9,
        temperature=0.3,
        max_length=200-input_len,
        min_length=input_len+4,
        repetition_penalty=1.2,
        do_sample=True,
    )
    response=tokenizer.batch_decode(
        generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )[0]
    return response 

@q_a_blueprint.route("/api/question-answering/", methods=['POST'])
def QAnswering():
    data=request.get_json()
    button_click=data.get("buttonClick")
    prompt=data.get("textData")
    
    if is_valid(prompt):
        if button_click=='answer' and prompt:
            answer=get_response(prompt)
            return jsonify({'answer':answer})
        else:
            return jsonify({'error':'Prompt is empty.'})
    else:
        return jsonify({'error':'Prompt is not in Arabic.'})

