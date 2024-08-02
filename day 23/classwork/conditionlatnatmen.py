def guess_number():
    # მომხმარებლის მიერ შეყვანილი რიცხვის მიღება
    user_number = int(input("შეიყვანეთ რიცხვი 1-დან 100-მდე: "))
    
    # პროგრამის მხრიდან გამოცნობის დიაპაზონის დასაწყისი
    low = 1
    high = 100
    attempts = 0
    
    while True:
        attempts += 1
        # პროგრამის მიერ გამომცნობი რიცხვის გენერირება
        guess = (low + high) // 2
        print(f"პროგრამის გამოცნობა: {guess}")
        
        if guess == user_number:
            print(f"პროგრამამ გამოიცნო თქვენი რიცხვი {attempts} ცდაში!")
            break
        else:
            feedback = input("რიცხვი მეტია, თუ ნაკლებია? (მეტი/ნაკლები): ")
            if feedback.lower() == "მეტი":
                low = guess + 1
            elif feedback.lower() == "ნაკლები":
                high = guess - 1

guess_number()
