name = input("What is your name? ")
print("hello, ", end="") #end="" prevents the newline character from being printed after "hello, "
print(name)
print ("Welcome to Python programming!")


name = input("What is your name? ")
print("hello, ", name, sep="") #concatenates "hello, " and the value of name 

name = input("What is your name? ")
# remove whitespace from string
name = name.strip()
print(f"hello, {name}!")



name = input("What is your name? ")
name = name.strip().title() # converts the first letter of each word to uppercase and the rest to lowercase
print(f"hello, {name}!")


name = input("What is your name? ").strip().title()
name = name 
print(f"hello, {name}!")




name = input("What is your name? ").strip().title()
first, last = name.split(" ") # splits the name into first and last name based on the space character
print(f"hello, {first} {last}!")

