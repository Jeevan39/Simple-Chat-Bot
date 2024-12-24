from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

faq_data = {
    "timings": "The college timings are from 8:30 AM to 5:30 PM.",
    "library": "The library is located on the second floor of the main building.",
    "leave": "To apply for leave, fill out the leave application form available on the college portal.",
    "cse": "The head of the CSE department is Dr. Jyothi K S."
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword, response in faq_data.items():
        if keyword in user_input:
            return response
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("query")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
