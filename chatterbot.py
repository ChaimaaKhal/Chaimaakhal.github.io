# Import necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Define a function to handle user input and get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Get a response from the chatbot
response = get_response("Hello")

# Print the response
print(response)
