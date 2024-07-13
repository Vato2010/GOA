def calculate_bmi():
    weight = float(input("შეიყვანეთ წონა კილოგრამებში: "))
    height = float(input("შეიყვანეთ სიმაღლე მეტრებში: "))
    
    bmi = weight / (height * height)
    
    print(f"თქვენი BMI არის: {bmi:.2f}")
    
    if bmi < 18.5:
        print("შესაბამისად, თქვენ გამოიწვევთ 'Underweight' ჯანმრთელობის სტატუსს.")
    elif 18.5 <= bmi <= 24.9:
        print("შესაბამისად, თქვენ გამოიწვევთ 'ნორმალური წონა' ჯანმრთელობის სტატუსს.")
    elif 25.0 <= bmi <= 29.9:
        print("შესაბამისად, თქვენ გამოიწვევთ 'Overweight' ჯანმრთელობის სტატუსს.")
    else:
        print("შესაბამისად, თქვენ გამოიწვევთ 'სიმსუქნე' ჯანმრთელობის სტატუსს.")
calculate_bmi()