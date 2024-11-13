import random

KnowledgeBase = {
    "hi":[
        "Hello My Name is Jamse Bot",
        "Hi I am classed as Jamse Bot",
        "How Can I help You"
    ],
    "what are the symptoms of COVID-19?":[
        "Symptoms of COVID-19 can include fever, cough, shortness of breath, fatigue, body aches, loss of taste or smell, sore throat, and headache."
    ],
    "how can you reduce the risk of heart disease?":[
        "You can reduce the risk of heart disease by maintaining a healthy diet, exercising regularly, not smoking, limiting alcohol intake, and managing stress."
    ],
    "what is the difference between a cold and the flu?":[
        "A cold is usually milder than the flu and does not typically result in serious health problems. The flu can lead to complications like pneumonia and can be life-threatening."
    ],
    "how often should you have a dental check-up?":[
        "You should have a dental check-up every six months to maintain good oral health and catch any potential issues early."
    ],
    "what are the benefits of eating a balanced diet?":[
        "Eating a balanced diet can help maintain a healthy weight, reduce the risk of chronic diseases, improve digestion, and boost overall health."
    ],
    "default":[
        "Thanks For Using ME",
        "Bye"
    ]
}

def respond(message):
    if message in KnowledgeBase:
        bot_message = random.choice(KnowledgeBase[message])
    else:
        bot_message = random.choice(KnowledgeBase["default"])
    return bot_message

def sendMessage(message):
    print("The User Message is: ", message)
    response = respond(message)
    print("The Response is: ", response)

if __name__ == "__main__":
    while True:
        user_input = input()
        user_input = user_input.lower()
        sendMessage(user_input)
        if user_input == "exit" or user_input == "stop":
            break
        