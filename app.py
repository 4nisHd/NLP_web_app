from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/api/get-paragraph',methods=['POST'])

def get_paragraph():
    #get the button input from the request data
    button_click=request.json.get('buttonClick')
    #process the button click and generate the paragraph
    
    if button_click=="button1":
        paragraph="ildsbdsfhn fdkbnfjdsf dfsjkbnsdffnsd fkdsbnfjds fnkdsbfjsdnf jksdbfds ,f dsjksf d, djksqq d qs djiqs dqs dhjqsbd qs, dnkqsqbdsqd jdsb qsndk djkqs"
    elif button_click=="button2":
        paragraph="this is paragraph2"
    else:
        paragraph="invalid"
    return jsonify({"paragraph":paragraph})

if __name__=="__main__":
    app.run(debug=True)
            