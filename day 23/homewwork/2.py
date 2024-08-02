import random

def guess_number():
    # პროგრამა თხოულობს მომხმარებლისგან რიცხვი
    number_to_guess = int(input("შეიყვანეთ რიცხვი 1-დან 100-მდე: "))
    
    # გენერირებას ახდენს შემთხვევითი რიცხვის 1-დან 100-მდე
    guess = random.randint(1, 100)
    
    attempts = 0  # გამოცდის რაოდენობის საწყისი მნიშვნელობა

    while guess != number_to_guess:
        print(f"კომპიუტერის გამოცანა: {guess}")
        attempts += 1
        guess = random.randint(1, 100)  # ხელახლა გენერირდება რიცხვი

    print(f"კომპიუტერმა საბოლოოდ გამოიცნო რიცხვი: {guess} {attempts} ცდის შემდეგ")

# პროგრამის გამოძახება
guess_number()
