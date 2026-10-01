# hello.py
print("Hello, GitHub!")

#A message to the user
print("Hi!")
name = input("What's your name? ")
print("It's nice to meet you,", name)
age = int(input("How old are you? "))

if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)  
age = 36
print(age)
print(type(age))

email_address = "john.doe@me.com"
print(email_address)
print(type(email_address))

answer = input("Are you enjoying the course? ")
if answer == "Yes" or answer == "Yeah" or answer == "Absolutely":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")

print("Challenge 1:")

# A message for the user
message = "This is going to be tricky ;)"
print(message)

message = "Very tricky!"
print(message)

result = int(2 ** 3)
print("2 ** 3 =", result)

result = int(5 - 3)
print("5 - 3 =", result)

print("Challenge complete!")






print("Goodbye world!")    
