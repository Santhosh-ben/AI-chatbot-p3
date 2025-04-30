from flask import Flask, request, jsonify, render_template
import nltk
import wikipedia
import wolframalpha

# Ensure punkt is downloaded
nltk.download('punkt')

app = Flask(__name__)

# Replace with your actual WolframAlpha App ID
app_id = "LY825Y-L8X566YGG4"
client = wolframalpha.Client(app_id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_input = request.args.get('msg')
    print("User input:", user_input)

    try:
        # Try answering using WolframAlpha
        res = client.query(user_input)
        answer = next(res.results).text
        print("WolframAlpha answer:", answer)
    except Exception as e:
        print("WolframAlpha error:", e)
        try:
            # Fallback to Wikipedia
            answer = wikipedia.summary(user_input, sentences=2)
            print("Wikipedia answer:", answer)
        except Exception as e:
            print("Wikipedia error:", e)
            answer = "Sorry, I couldn't find an answer."

    return jsonify({'response': answer})

if __name__ == "__main__":
    app.run(debug=True)

