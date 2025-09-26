from flask import Flask, render_template, request
from ai import send_prompt_to_Azure_OpenAI

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    response_text = ""
    prompt = request.form.get("prompt", "")
    try:
      send_prompt_to_Azure_OpenAI(prompt)
    except Exception as e:
      f"Ocurrió un error: {e}"
    return render_template(response=response_text)

    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0", port=5001)