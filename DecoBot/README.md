# DecoBot - Rule-Based Chatbot

## About the Project

DecoBot is a simple rule-based chatbot built using Python. It can answer a few predefined questions related to AI, Python, chatbots, and DecodeLabs.

The main idea behind this project was to understand how a chatbot works before moving to more advanced AI-based chatbots. Instead of using machine learning, DecoBot works using predefined responses and keyword matching.

## Features

* Responds to greetings like Hello, Hi, and Hey
* Answers basic questions related to AI and Python
* Uses exact matching for predefined questions
* Uses keyword matching for longer sentences
* Handles unknown questions using a fallback response
* Allows users to exit the chat using commands like Bye, Exit, or Quit

## Technologies Used

* Python
* Regular Expressions (re module)
* Object-Oriented Programming (OOP)

## How It Works

1. The user enters a message.
2. The input is cleaned and converted to lowercase.
3. The chatbot first checks for an exact match.
4. If no exact match is found, it checks for keywords.
5. If a match is found, the corresponding response is returned.
6. Otherwise, a default message is displayed.

## Sample Conversation

You: hello

DecoBot: Hey! How are you?

You: what is ai

DecoBot: AI means Artificial Intelligence, where machines try to think like humans.

You: tell me about python

DecoBot: Python is one of the most popular programming languages today.

You: bye

DecoBot: Bye! See you next time.

## What I Learned

While building this project, I learned:

* How rule-based chatbots work
* How to process user input
* How dictionaries can be used for storing responses
* How keyword matching improves chatbot responses
* Basic use of OOP in Python

## Future Improvements

* Add more responses and topics
* Store conversation history
* Create a GUI version
* Integrate machine learning for smarter responses
