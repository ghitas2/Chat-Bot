import re
import long_responses as long

#Function to get response 
def get_response(input):
    split_message = re.split(r'\s+|[,;?!.-]/s*' , input.lower())
    response = check_all_messages(split_message)
    return response

#Function to know probab of a word
def message_probability(user_message,recognised_words,single_response =False , recquired_words =[] ):
    message_certainity=0
    has_recquired_words = True

    #loop to check if words are recognised
    for words in user_message :
        if words in recognised_words:
            message_certainity +=1
    #calculate the percent of recognized words in a user's message
    percentage = (float(message_certainity)/float(len(recognised_words)))*100


 
#Testing the response sytem 
while True:
    print('Bot : ' + get_response(input('You: ')))