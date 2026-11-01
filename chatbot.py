def chatbot(): 
    print("Chatbot: Hello! How can I help you?") 
 
    while True: 
        msg = input("You: ").lower() 
 
        if "hello" in msg or "hi" in msg: 
            print("Chatbot: Hello!") 
        elif "your name" in msg: 
            print("Chatbot: I am a simple chatbot.") 
        elif "how are you" in msg: 
            print("Chatbot: I am fine!") 
        elif "bye" in msg: 
            print("Chatbot: Goodbye!") 
            break 
        else: 
            print("Chatbot: Sorry, I don't understand.") 
 
chatbot() 
