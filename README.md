# Chat-Bot
Description : 

Introducing a friendly and interactive chatbot designed to engage in natural conversations with users. This chatbot employs a rule-based system, where it analyzes user inputs to determine the most suitable response. Using a set of recognized words and required conditions, the chatbot calculates the probability of various responses, ensuring dynamic and context-aware interactions.

Key Features:

Natural Conversation: Engage in casual and meaningful conversations with the chatbot.
Probability-based Responses: Responses are dynamically selected based on the likelihood of relevance to the user's input.
Recognized and Required Words: Responses are influenced by the presence of recognized words and required conditions in the user's message.
Single-response Option: Certain responses can be designated as standalone, independent choices.

Variables mapping :

User Message: This refers to the entire input provided by the user, which is typically a sentence or a sequence of words. It's a string.

List of Words: This represents the individual words extracted from the user's message. In the code you provided, a loop is used to iterate through each character in the user's message and effectively create a list of words.

Recognized words : set of words associated with a specific response. If any of these words are found in the user's input, it increases the probability of that response being chosen.

Required words are words that must be present in the user's input for a specific response to be considered. If any of these required words are missing, it might decrease the probability of that response being chosen.

Usage in Code: In the same message_probability function, the required_words parameter is a list of words that must be present in the user_message. If any required word is missing, the has_required_words flag is set to False, affecting the final probability.
