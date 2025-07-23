from flask import Flask, request, jsonify, render_template
from grammar_engine import generate_line

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    role = data.get("role", "hero")
    context = data.get("context", None)
    use_llm = data.get("use_llm", True)
    response = generate_line(role=role, context=context, use_llm=use_llm)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
