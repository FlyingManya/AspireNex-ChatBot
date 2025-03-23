import re
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

 patterns = {
        r'\b(hi|hello)\b': "Hello! How can I assist you regarding vector-borne diseases?",
        r'\b(what is your name|who are you)\b': "I'm Vector Guard's AI assistant, here to help with disease awareness and prevention.",
        r'\b(where are you from)\b': "I exist in the digital space, ready to provide health-related information.",
        r'\b(how are you)\b': "I'm always ready to assist you with health queries!",
        r'\b(do you have any hobbies|what do you do for fun)\b': "Helping people stay informed about vector-borne diseases is my purpose!",
        r'\b(can I upload my health report)\b': "Yes, you can upload your health report for AI-driven analysis to gain insights into potential health risks.",
        r'\b(what are vector-borne diseases)\b': "Vector-borne diseases are infections transmitted by vectors like mosquitoes, ticks, and fleas. Examples include malaria, dengue, and chikungunya.",
        r'\b(how to prevent mosquito bites)\b': "To prevent mosquito bites, use insect repellents, wear long sleeves, and avoid stagnant water near your home.",
        r'\b(symptoms of malaria)\b': "Malaria symptoms include fever, chills, sweating, headache, nausea, and muscle pain.",
        r'\b(symptoms of dengue)\b': "Dengue symptoms include high fever, severe headache, joint pain, rashes, and bleeding gums.",
        r'\b(what should I do if I have a fever)\b': "If you have a fever, rest, stay hydrated, and consult a doctor for proper diagnosis.",
        r'\b(is there a vaccine for dengue)\b': "Yes, some countries offer a dengue vaccine. Consult your healthcare provider for more details.",
        r'\b(tell me about chikungunya)\b': "Chikungunya is a viral disease transmitted by mosquitoes. Symptoms include fever, joint pain, and rashes.",
        r'\b(what should I do if I get a mosquito-borne disease)\b': "Seek medical attention immediately, stay hydrated, and follow your doctor’s advice.",
        r'\b(what languages do you speak)\b': "I can understand and respond in English to assist with health-related queries.",
        r'\b(are you a robot)\b': "Yes, I am an AI chatbot designed to help with vector-borne disease awareness.",
        r'\b(do you dream)\b': "I don't dream, but I continuously learn to provide better health assistance.",
        r'\b(what do you do for fun)\b': "Chatting with users like you and providing health insights is my main function!",
        r'\b(are you human)\b': "No, I'm a chatbot created to provide health-related information and support.",
        r'\b(whats the time)\b': "I'm sorry, I don't have access to real-time information like the current time.",
        r'\b(bye)\b': "Goodbye! Stay safe and take precautions against vector-borne diseases!",
    }
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
