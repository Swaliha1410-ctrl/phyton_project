class Coffee:
    def __init__(self):
        self.order_items = []
        self.order_prices = []
        self.menu_items = {
            "cappuccino": 350, "mocha": 320, "caramel kiss": 300, 
            "vanilla dream": 280, "spiced cocoa": 290, "latte": 380, 
            "american chocolate": 400
        }

    def menu(self):
        print("\n" + "-"*10 + " Menu " + "-"*10)
        for item, price in self.menu_items.items():
            print(f'{item.title():<20}: ₹{price}')
        print("-" * 26)

    def order(self):
        try:
            size = int(input('\nHow many coffees would you like to buy? '))
            for i in range(size):
                while True:
                    choice = input(f'Enter flavour for coffee #{i+1} ☕: ').lower().strip()
                    if choice in self.menu_items:
                        self.order_items.append(choice.title())
                        self.order_prices.append(self.menu_items[choice])
                        print(f"Added {choice.title()} to cart.")
                        break
                    else:
                        print('This coffee is not available. Please check the menu.')
            print('--- Order Added !!! ---')
        except ValueError:
            print("Invalid input. Please enter a number for the quantity.")

    def bill(self):
        if not self.order_items:
            print("\nYour cart is empty!")
            return

        print('\n' + '='*25)
        print('      YOUR RECEIPT      ')
        print('='*25)
        
        subtotal = sum(self.order_prices)
        
        for index, (item, price) in enumerate(zip(self.order_items, self.order_prices), 1):
            print(f'{index}. {item:<15} ₹{price}')
        
        print("-" * 25)
        print(f"Subtotal:       ₹{subtotal}")
        
        discount_amt, final_total = self.calculate_discount(subtotal)
        
        if discount_amt > 0:
            print(f"Discount:      -₹{discount_amt}")
        print(f"TOTAL PAYABLE:  ₹{final_total}")
        print('='*25)

    def calculate_discount(self, amount):
        """Returns (discount_value, final_amount) without modifying state."""
        if amount >= 1500:
            rate = 0.20
        elif amount >= 1000:
            rate = 0.15
        elif amount >= 500:
            rate = 0.10
        else:
            rate = 0.0
        
        discount_val = amount * rate
        return discount_val, (amount - discount_val)

    def start(self):
        while True:
            print('\n--- Welcome to Our Coffee Shop ---')
            print('1. Show Menu\n2. Add Coffee\n3. View Bill & Pay\n4. Exit')
            choice = input('Enter your choice: ')
            
            if choice == '1':
                self.menu()
            elif choice == '2':
                self.order()
            elif choice == '3':
                self.bill()
            elif choice == '4':
                print('Thank you for visiting! Have a caffeinated day! ☕')
                break
            else:
                print('Kindly enter a valid choice (1-4)')

c1 = Coffee()

c1.start()

