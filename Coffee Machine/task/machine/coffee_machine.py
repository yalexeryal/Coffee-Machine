class CoffeeMachine:
    coffee_drinks = {
        '1': {'name': 'espresso', 'water': 250, 'coffee_beans': 16, 'milk': 0, 'costs': 4},
        '2': {'name': 'late', 'water': 350, 'coffee_beans': 20, 'milk': 75, 'costs': 7},
        '3': {'name': 'cappuccino', 'water': 200, 'coffee_beans': 12, 'milk': 100, 'costs': 6},
    }
    msg_1 = 'I have enough resources, making you a coffee!'
    msg_2 = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
    msg_3 = 'Write action (buy, fill, take, remaining, exit):'

    def __init__(self, water=400, milk=540, coffee_beans=120, cups=9, money=550, ):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def remaining(self):
        """
        Outputs the balance after purchase.

        :return:
        """
        return f"The coffee machine has:\n" \
               f"{self.water} of water\n" \
               f"{self.milk} of milk\n" \
               f"{self.coffee_beans} of coffee beans\n" \
               f"{self.cups} of disposable cups\n" \
               f"{self.money} of money"

    def sales_calculator(self, answer):
        """
        Performs stock adjustments after purchase.

        :param answer:
        :return:
        """
        self.water -= self.coffee_drinks[answer]['water']
        self.milk -= self.coffee_drinks[answer]['milk']
        self.coffee_beans -= self.coffee_drinks[answer]['coffee_beans']
        self.cups -= 1
        self.money += self.coffee_drinks[answer]['costs']

    def answer_actions(self, answer_action):
        """
        Processes incoming requests.

        :param answer_action:
        :return:
        """
        if answer_action == 'buy':
            print(coffee_machine.msg_2)
            answer_coffee = input()
            if answer_coffee == 'back':
                pass
            elif self.remaining_portion(answer_coffee) == '':
                self.sales_calculator(answer_coffee)
                return self.msg_1
            else:
                return f"Sorry, not enough {self.remaining_portion(answer_coffee)}!"
        elif answer_action == 'fill':
            self.water += int(input('Write how many ml of water you want to add: '))
            self.milk += int(input('Write how many ml of milk you want to add: '))
            self.coffee_beans += int(input('Write how many grams of coffee beans you want to add: '))
            self.cups += int(input('Write how many disposable coffee cups you want to add: '))
        elif answer_action == 'take':
            print(f"I gave you ${self.money}")
            self.money = 0
        elif answer_action == 'remaining':
            return self.remaining()

    def remaining_portion(self, answer):
        """
        calculation of coffee portions from the received products
        """
        remaining_portions = ""

        if self.water < self.coffee_drinks[answer]['water']:
            remaining_portions = remaining_portions + 'water'
        if self.milk < self.coffee_drinks[answer]['milk']:
            remaining_portions = remaining_portions + ' milk'
        if self.coffee_beans < self.coffee_drinks[answer]['coffee_beans']:
            remaining_portions = remaining_portions + ' coffee_beans'
        if self.cups < self.cups:
            remaining_portions = remaining_portions + ' cups'

        return remaining_portions


coffee_machine = CoffeeMachine()

print(coffee_machine.msg_3)
answer_action = input()
while answer_action != 'exit':
    print(coffee_machine.answer_actions(answer_action))
    print()
    print(coffee_machine.msg_3)
    answer_action = input()
