import re
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

 patterns = {
    r'\b(hi|hello)\b': "Hello! How can I help you today?",
    r'\b(what is your name|who are you)\b': "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    r'\b(where are you from)\b': "I'm from the digital world, always ready to chat!",
    r'\b(how are you)\b': "I'm just a chatbot, but I'm here to assist you.",
    r'\b(do you have any hobbies|what do you do for fun|what do you Do for fun)\b': "I'm always busy helping users, so my hobby is chatting with people like you!",
    r'\b(what did you eat today)\b': "I don't eat, but I can help you find delicious recipes and food-related information.",
    r'\b(what\'?s your favorite color)\b': "I'm a chatbot, so I don't have personal preferences for colors.",
    r'\b(do you enjoy listening to music)\b': "I can't listen to music, but I'm here to chat about it!",
    r'\b(tell me a joke)\b': "Sure! Why don't scientists trust atoms? Because they make up everything!",
    r'\b(tell me something interesting)\b': "Did you know that the world's oldest piece of chewing gum is over 9,000 years old?",
    r'\b(what is the weather like today)\b': "I'm sorry, I can't check the weather right now, but you can use a weather app for that!",
    r'\b(can you help me with programming)\b': "Absolutely! I can assist you with programming questions.",
    r'\b(recommend a movie)\b': "Sure! How about 'The Matrix'?",
    r'\b(what\'?s the meaning of life)\b': "That's a deep question! Philosophers have debated it for centuries.",
    r'\b(who is your creator)\b': "I was created by talented developers using JavaScript and HTML!",
    r'\b(what languages do you speak)\b': "I can understand and respond in English.",
    r'\b(are you a robot)\b': "Yes, I am a chatbot powered by artificial intelligence!",
    r'\b(do you dream)\b': "No, I don't dream like humans do.",
    r'\b(what do you do for fun)\b': "Chatting with users like you is what I enjoy the most!",
    r'\b(are you human)\b': "No, I'm a chatbot designed to assist with various tasks.",
    r'\b(what\'?s the time)\b': "I'm sorry, I don't have access to real-time information like the current time.",
    r'\b(bye)\b': "Goodbye! Take care and have a great day!",
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
