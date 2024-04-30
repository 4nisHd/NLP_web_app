from flask import Flask
from src.text_summerizer.text_sum_bp import text_summarization_blueprint
from src.text_gen.text_gen_bp import text_generation_blueprint
from src.Q_A.qa_bp import q_a_blueprint

app=Flask(__name__)
app.register_blueprint(text_summarization_blueprint)
app.register_blueprint(text_generation_blueprint)
app.register_blueprint(q_a_blueprint)
if __name__=='__main__':
    app.run(debug=True)