print("""
********
Welcome to the perfect number algorithm...

If you want to quit press 0
********
""")


while True:
    number = int(input("Write a number: "))
    if number == 0:
        break
    else:
        if number > 0:
            i = 1
            bt = 0
            while (i < number):
                if number % i == 0:
                    bt = bt + i
                    i = i + 1
                else:
                    i = i + 1
                    continue
        else:
            print("Write a positive number...")

        if bt == number:
            print(number, " is a perfect number.")

        else:
            print(number, " is not a perfect number.")
