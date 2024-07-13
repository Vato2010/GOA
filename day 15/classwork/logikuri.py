def discount_eligibility():
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    purchase_amount = float(input("შეიყვანეთ შესყიდვის მთლიანი თანხა ($): "))

    if age > 60:
        if purchase_amount >= 100:
            print("თქვენ შეგიძლიათ მიიღოთ ფასდაკლება!")
        else:
            print("თქვენ არ შეგიძლიათ მიიღოთ ფასდაკლება.")
    else:
        if purchase_amount >= 100:
            print("თქვენ მიგიღიათ მაღალი ფასდაკლების უფლება!")
        else:
            print("თქვენ არ მიგიღიათ ფასდაკლება.")
            
discount_eligibility()