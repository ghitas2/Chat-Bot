# Chat-Bot
Variables mapping :

User Message: This refers to the entire input provided by the user, which is typically a sentence or a sequence of words. It's a string.

List of Words: This represents the individual words extracted from the user's message. In the code you provided, a loop is used to iterate through each character in the user's message and effectively create a list of words.

Recognized words : set of words associated with a specific response. If any of these words are found in the user's input, it increases the probability of that response being chosen.

Required words are words that must be present in the user's input for a specific response to be considered. If any of these required words are missing, it might decrease the probability of that response being chosen.

Usage in Code: In the same message_probability function, the required_words parameter is a list of words that must be present in the user_message. If any required word is missing, the has_required_words flag is set to False, affecting the final probability.