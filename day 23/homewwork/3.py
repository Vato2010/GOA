def fizz_buzz():
    for i in range(1, 101):  # მარყუჟი 1-დან 100-მდე
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# პროგრამის გამოძახება
fizz_buzz()
