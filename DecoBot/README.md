# DecoBot - Rule-Based Chatbot

## About the Project

DecoBot is a simple rule-based chatbot developed using Python as part of my AI/ML Internship at DecodeLabs.

The chatbot responds to user queries using predefined responses and keyword matching. The goal of this project was to understand the fundamentals of chatbot development, including user input processing, response generation, and code organization using Object-Oriented Programming (OOP).

## Features

* Responds to greetings and common user queries
* Answers basic questions related to AI, Python, Chatbots, and DecodeLabs
* Uses exact matching for predefined questions
* Uses keyword matching for longer user inputs
* Cleans and sanitizes user input before processing
* Handles unknown queries using a fallback response
* Supports exit commands such as Bye, Exit, and Quit
* Organized using Object-Oriented Programming (OOP)

## Technologies Used

* Python
* Regular Expressions (re module)
* Object-Oriented Programming (OOP)

## How It Works

1. The user enters a message.
2. The input is cleaned and converted to lowercase.
3. The chatbot checks for an exact match in the response dictionary.
4. If no exact match is found, keyword matching is performed.
5. If a match is found, the corresponding response is returned.
6. Otherwise, a fallback response is displayed.

## Main Functions

* `show_welcome()` – Displays the chatbot welcome message.
* `clean_text()` – Cleans and formats user input.
* `exact_match()` – Checks for direct matches in the response dictionary.
* `keyword_match()` – Searches for keywords within user input.
* `get_response()` – Generates the appropriate chatbot response.
* `start_chat()` – Starts and manages the chatbot conversation.

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

Through this project, I learned:

* How rule-based chatbots work
* How to process and sanitize user input
* How dictionaries can be used for storing chatbot responses
* The difference between exact matching and keyword matching
* How to organize code using Object-Oriented Programming (OOP)
* How chatbot conversation flow is managed

## Future Improvements

* Add more responses and topics
* Store conversation history
* Create a graphical user interface (GUI)
* Integrate machine learning for smarter responses
* Add support for more natural conversations

