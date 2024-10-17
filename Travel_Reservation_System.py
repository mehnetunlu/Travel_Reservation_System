print("Welcome to the travel reservation system!")

accounts = {"mehmet": "12345"}

def user():
    while True:
        choose = input("Login or create account. 1-login, 2-create account: ")
        if choose == "1":
            if login():
                choose_action()
                break
        elif choose == "2":
            create_account()
        else:
            print("Enter a valid number, please try again.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in accounts and accounts[username] == password:
        print("Login successful.")
        return True
    else:
        print("Wrong username or password, please try again...")
        return False

def create_account():  
    while True:
        new_username = input("Enter your new username: ")
        if new_username in accounts:
            print("This username is already taken.")
        else:
            new_password = input("Enter your new password: ")
            accounts[new_username] = new_password
            print("Account created successfully!")
            break

def choose_action():
    while True:
        choose = input("Choose an action. 1- Buy tickets, 2- Cancel ticket: ")
        if choose == "1":
            buy_ticket()
            break
        elif choose == "2":
            cancel_ticket()
            break
        else:
            print("Enter a valid number.")

def buy_ticket():
    confirm = input("Should I buy a ticket? (Y/N): ").upper()
    if confirm == "Y":
        choose_transport()
    else:
        print("Ticket purchase canceled.")

def cancel_ticket():
    confirm = input("Do you want to cancel the ticket? (Y/N): ").upper()
    if confirm == "Y":
        print("Your ticket is being canceled.")
    else:
        print("Ticket cancellation process aborted.")

def choose_transport():
    vehicle_prices = {"1": ("Bus", 1000), "2": ("Train", 300), "3": ("Airline", 2000)}
    while True:
        choice = input("Choose the vehicle you want to travel in: 1- Bus, 2- Train, 3- Airline: ")
        if choice in vehicle_prices:
            vehicle, price = vehicle_prices[choice]
            print(f"Travel vehicle: {vehicle}, Price: ${price}")
            final_price = apply_discount(price)
            seat_number() 
            if not make_payment(final_price):
                print("Payment failed. Please try again.")
                return
            choose_food()
            break
        else:
            print("Enter a valid number.")

def seat_number():
    seat = input("Choose seat number: ")
    print(f"Your seat number is {seat}. Enjoy your journey!")

def make_payment(amount):
    attempts = 3
    while attempts > 0:
        method = input("Is payment by credit card or debit card? ").lower()
        if method in ["credit card", "debit card"]:
           print(f"Payment of ${amount:.2f} completed successfully with {method}.")
           return True
        else:
           attempts -= 1
           print(f"Invalid payment method. {attempts} attempts remaining.")
        
    return False 
             

def apply_discount(ticket_price):
    discount_rates = {"Student": 0.1, "Senior": 0.15, "Child": 0.5}
    for discount_type, rate in discount_rates.items():
        confirm = input(f"Are you a {discount_type.lower()}? (Y/N): ").upper()
        if confirm == "Y":
            ticket_price -= ticket_price * rate
            print(f"Discount applied for {discount_type}. New ticket price: ${ticket_price:.2f}")
            break
    return ticket_price



def choose_food():
    confirm = input("Would you like food or drink? (Y/N): ").upper()
    if confirm == "Y":
        options = {"1": "Cake", "2": "Fruit Juice", "3": "Coffee", "4": "Tea"}
        while True:
            choice = input("Choose your item: 1- Cake, 2- Fruit Juice, 3- Coffee, 4- Tea: ")
            if choice in options:
                print(f"Bon appétit! Enjoy your {options[choice].lower()}.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Alright, have a good journey!")
        satisfaction_survey()



def satisfaction_survey():
    attempts = 3
    while attempts > 0:
       point = input("Give a point (1,2,3,4,5): ")

       if point == "1":
        print("We're sorry you had a bad experience.")
        break
       elif point == "2":
        print("We appreciate your feedback and will try to improve.")
        break
       elif point == "3":
        print("Thanks for your feedback! We'll keep working to get better.")
        break
       elif point == "4":
        print("We're glad you had a good trip! Thanks for the feedback.")
        break
       elif point == "5":
         print("Thank you! We're thrilled you had a great trip!")
         break
       else:
          attempts -= 1
          print("Invalid number, please try again. {attempts} attempts remaining")
          if attempts == 0:
              print("All attempts used. Exiting survey.")

user() 
