import time

class RentalPropertyROI():
    yes = ['y','yes','yep','yeah','yup']
    no = ['n','no','nope']

    def __init__(self):
        self.income = {"rental": 0, "laundry": 0, "storage": 0, "misc": 0}
        self.total_income = 0
        self.expense = {"mortgage": 0, "tax": 0, "insurance": 0, "utilities": 0, "repairs": 0, "HOA": 0, "maintenance": 0, "vacancy": 0}
        self.total_expense = 0
        self.invest = {"Down Payment": 0, "Closing fees": 0, "Repairs": 0, "Additional fees": 0}
        self.total_investment = 0
        # self.cash_flow = 0

    def incomeCollect(self):
        print("Please answer all questions based on a monthly period.\n")
        start = input("Press enter to begin the questionnaire: ")
        print("")
        # force numerical value inputs for incomes
        while True:
            try:
                rental = int(input("How much income do you make from rent payments?: "))
                self.income["rental"] = rental
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                laundry = int(input("How much income do you make from laundry payments?: "))
                self.income["laundry"] = laundry
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:    
                storage = int(input("How much income do you make from storage payments?: "))
                self.income["storage"] = storage
                break
            except:
                print("Please enter a numerical value")

        while True:
            extra = input("Do you charge your tenants any additonal fees that haven't been mentioned? (y/n): ")
            if extra.lower() in self.yes:
                while True:
                    try:
                        misc = int(input("How much income do you make from these additional charges?: "))
                        self.income["misc"] = misc
                        break
                    except:
                        print("Please enter a numerical value")
                break
            elif extra.lower() in self.no:
                break
            else:
                print("Please enter a valid input")
        self.total_income = sum(list(self.income.values()))


    def expenseCollect(self):
        print("Please answer all questions based on a monthly period.\n")
        start = input("Press enter to begin the questionnaire: ")
        print("")
        # force numerical value inputs for expenses
        while True:
            try:
                mortgage = int(input("How much do you pay on this property in mortgage?: "))
                self.expense["mortgage"] = mortgage
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                tax = int(input("How much do you pay on this property in taxes?: "))
                self.expense["tax"] = tax
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                insurance = int(input("How much do you pay on this property in insurance?: "))
                self.expense["insurance"] = insurance
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                utilities = int(input("How much do you pay on this property in utilities?: "))
                self.expense["utilities"] = utilities
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                repairs = int(input("How much do you pay on this property in repairs?: "))
                self.expense["repairs"] = repairs
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                hoa = int(input("How much do you pay on this property in HOA fees?: "))
                self.expense["HOA"] = hoa
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                maintenance = int(input("How much do you pay on this property in maintenance?: "))
                self.expense["maintenance"] = maintenance
                break
            except:
                print("Please enter a numerical value")


        while True:
            extra = input("Do you put money aside monthly incase of rental property vacancy? (y/n): ")
            if extra.lower() in self.yes:
                while True:
                    try:
                        vacancy = int(input("How much money do you put aside for vacancies?: "))
                        self.expense["vacancy"] = vacancy
                        break
                    except:
                        print("Please enter a numerical value")
                break
            elif extra.lower() in self.no:
                break
            else:
                print("Please enter a valid input")
        self.total_expense = sum(list(self.expense.values()))

    def investmentCollect(self):
        invested = []
        while True:
            try:
                down = int(input("How much was your down payment on this property?: "))
                invested.append(down)
                self.invest["Down Payment"] = down
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                closing = int(input("How much did you pay in closing fees on this property?: "))
                invested.append(closing)
                self.invest["Closing fees"] = closing
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                repairs = int(input("How much did you spend on repairs?: "))
                invested.append(repairs)
                self.invest["Repairs"] = repairs
                break
            except:
                print("Please enter a numerical value")
        while True:
            try:
                additional = int(input("What is the sum of any additional fees that were spent to acquire this property?: "))
                invested.append(additional)
                self.invest["Additional fees"] = additional
                break
            except:
                print("Please enter a numerical value")
        self.total_investment = sum(invested)

    @property
    def cashFlow(self):
        cash_flow = self.total_income - self.total_expense
        # self.cash_flow = cash_flow
        return cash_flow
    
    @property
    def cashReturn(self):
        roi = ((12 * self.cashFlow) / self.total_investment) *100
        roi = str(roi)+"%"
        return roi

    def run(self):
        print("***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****")
        print("Welcome to BiggerPockets Rental Property Program where WE, help YOU, become financially independent")
        print("***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****\n")

        time.sleep(4)

        # checkpoint = input("Press Enter to continue: ")

        # Investment on Property questionnaire
        print("Please start by answering the following questionanire for your investments on your property:\n")

        time.sleep(4)

        # checkpoint = input("Press Enter to continue: ")

        print("")
        while True:
            self.investmentCollect()
            print("\nOkay, here are your investment details on this property")
            for k, v in self.invest.items():
                print("\t",k,": $",v, sep="")
            print(f"\t>Total Investment: ${self.total_investment}")
            ans = input("Does everything look right?(y/n): ")
            if ans in self.yes:
                break
            else:
                print("Okay, let's try that again...\n")

        # Income questionnaire
        print("\nNow let's collect data on your income from this property:\n")
        time.sleep(3)
        while True:
            self.incomeCollect()
            print("Here is the breakdown of your income on this property")
            for k, v in self.income.items():
                print("\t",k.title(),": $",v, sep="")
            print(f"\t>Total Income: ${self.total_income}")
            ans = input("Does everything look correct?(y/n): ")
            if ans in self.yes:
                break
            else:
                print("Let's try that again...\n")

        # Expenses questionnaire
        print("Let's do a deep dive into your expenses on this property:\n")
        time.sleep(3)
        while True:
            self.expenseCollect()
            print("Here is the breakdown of your expenses on this property")
            for k, v in self.expense.items():
                print("\t",k.title(),": $",v, sep="")
            print(f"\t>Total Expenses: ${self.total_expense}")
            ans = input("Does everything look correct?(y/n): ")
            if ans in self.yes:
                break
            else:
                print("Let's try that again...\n")

        print("\nPerfect!\n")
        print("Rental Property Program is computing your data...")
        time.sleep(5)

        print("Here is your cash flow ~ the amount of monthly profit you are making on your property")
        print(f"${self.cashFlow} per month")

        time.sleep(2)
        checkpoint = input("\nPress Enter to continue: ")

        print("\nHere is your cash return ~ the percentage of your initial investment that you're making back each year")
        print(f"{self.cashReturn} per annum")

        print("\nThank you for using our program")
        end = ("\nPress Enter to exit: ")


myrental = RentalPropertyROI()
myrental.run()