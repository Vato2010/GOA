def calculate_total():
    num_items = int(input("შეიყვანეთ ნივთების რაოდენობა: "))
    
    total_cost = 0
    
    for i in range(1, num_items + 1):
        price = float(input(f"შეიყვანეთ ფასი ნივთის #{i}-სთვის: "))
        total_cost += price
    
    print(f"ყველა ნივთის მთლიანი ღირებულება არის: {total_cost} ლარი")

# პროგრამის გაშვება
calculate_total()
