def chatbot_input(user_message):
    #convert user input to lowercase
    user_message=user_message.lower()

    #Greeting
    if"hello" in user_message or "hi" in user_message:
        return "Hello!how can i help you?"

    #Booking
    elif "book" in user_message or "reserve"in user_message:
        return "provide details"
    
    #Help
    elif "help" in user_message or"support" in user_message:
        return "I can help you in general infomation"
    #Exit
    elif "bye"in user_message or "good bye" in user_message:
        return "Good bye,happy to help you"
    #default response
    else:
        return "sorry,i did not understand"
#Test the chatbot
while True:
    user_message=input('User:')
    print('Chatbot:',chatbot_input(user_message))
