import re


class DecoBot:

    def __init__(self):

        # responses for common questions
        self.responses = {
            "hello": "Hey! How are you?",
            "hi": "Hi there!",
            "hey": "Hey! What's up?",

            "what is ai": "AI means Artificial Intelligence, where machines try to think like humans.",
            "what is a chatbot": "A chatbot is a program that talks with users and responds to their questions.",
            "what is python": "Python is a programming language used for web development, AI, automation, and more.",
            "what is machine learning": "Machine Learning is a branch of AI that helps computers learn from data.",
            "what is decodelabs": "DecodeLabs is a platform that helps students learn technical skills through practical projects.",

            "who are you": "I'm DecoBot, a simple rule-based chatbot.",
            "what can you do": "I can answer questions about AI, Python, chatbots, and DecodeLabs.",

            "how are you": "I'm doing good! Thanks for asking.",
            "motivate me": "Keep learning and stay consistent. Small progress every day leads to big results.",
            "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",

            "thank you": "You're welcome!",
            "thanks": "Happy to help!",

            "bye": "Goodbye! Take care 👋"
        }

        # keyword matching for longer sentences
        self.keywords = {
            "ai": "AI is about making machines think and learn like humans.",
            "python": "Python is one of the most popular programming languages today.",
            "chatbot": "A chatbot is software designed to interact with users through conversation.",
            "machine learning": "Machine Learning allows systems to improve from experience and data.",
            "decodelabs": "DecodeLabs focuses on practical learning and project-based training."
        }

        self.fallback = (
            "Sorry, I didn't understand that. "
            "Try asking about AI, Python, chatbots, or DecodeLabs."
        )

    # clean the user input
    def clean_text(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    # check direct matches
    def exact_match(self, text):
        return self.responses.get(text)

    # check keyword matches
    def keyword_match(self, text):

        for keyword in self.keywords:
            if keyword in text:
                return self.keywords[keyword]

        return None

    # generate response
    def get_response(self, user_input):

        clean_input = self.clean_text(user_input)

        response = self.exact_match(clean_input)

        if response:
            return response

        response = self.keyword_match(clean_input)

        if response:
            return response

        return self.fallback

    # start the chatbot
    def start_chat(self):

        print("=" * 50)
        print("      DecoBot - Rule Based Chatbot")
        print("     DecodeLabs Internship Project")
        print("      Type 'bye' to exit")
        print("=" * 50)

        while True:

            user_input = input("\nYou: ")

            if not user_input.strip():
                continue

            clean_input = self.clean_text(user_input)

            if clean_input in {"bye", "exit", "quit"}:
                print("DecoBot: Bye! See you next time 👋")
                break

            response = self.get_response(user_input)

            print("DecoBot:", response)


if __name__ == "__main__":
    bot = DecoBot()
    bot.start_chat()
