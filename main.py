import time
import sys
import re
print("This is a Password check!")
time.sleep(0.5)
print("Please Hold on a sec till we boot up!")
ending = time.time() + 5
dots = [". ", ".. ", "... ", "...."]

while time.time() < ending:
    for loading in dots:
        if time.time() >= ending:
            break
        sys.stdout.write(f"\r{loading}  ")
        sys.stdout.flush()
        time.sleep(0.5)
sys.stdout.write('\rWhether it is "strong", "weak", "medium"\n')
time.sleep(0.5)
special_characters = "!£$%^&*()_+=-[]{}#~¬`"
while True:
    password = input("Enter your password: ")
    score = 0
    if len(password) >= 8: #password is too weak
        score += 1
    if any(char.isdigit() for char in password): #digits
        score += 1
    if bool(re.search(r'[A-Z]', password)):
        score += 1
    if any(char in special_characters for char in password):
        score += 1
    if len(password) < 8:
        score += 1

    if score == 4:
        print("Password is Strong.")
    if score == 2 or score == 3:
        print("Password is Medium.")
    if score == 1:
        print("Password is Weak.")

    user_choice = input("Do you want to continue(Y/N): ").strip().lower()
    if user_choice in ['n','no']:
        break