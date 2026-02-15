def greet(input):
    if "hello" in input.lower():   # .lower() converts the input to lowercase to make the check case-insensitive
        return"Hello! How are you?"
    elif "hi" in input.lower():
        return"Hi there! How can I help you?"
    elif "hey" in input.lower():
        return"Hey! What's up?"
    else:
        return"Sorry, I didn't understand that. Please greet me with 'hello', 'hi', or 'hey'."
        
greet(input("Please greet me: "))