from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Incident Response Chatbot</title>
</head>
<body>
    <h2>Incident Response Chatbot</h2>
    <form action="/get" method="post">
        <textarea name="msg" rows="5" cols="60" placeholder="Type your query here..."></textarea><br><br>
        <input type="submit" value="Send">
    </form>
    <h4>Bot:</h4>
    <p>{{ response }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE, response="")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    
    # Simple predefined responses (you can expand this)
    responses = {
        "malware": "Malware is malicious software designed to harm, exploit, or otherwise compromise a computer system.",
        "phishing": "Phishing is a cyberattack that uses fake messages to trick users into revealing personal data.",
        "ransomware": "Ransomware locks files and demands payment to restore access.",
        "incident": "An incident refers to any event that could lead to a data breach or system compromise.",
    }

    response = responses.get(user_input.lower(), "Sorry, I don't have information about that yet.")
    return render_template_string(HTML_PAGE, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
