class Bank_Account:
    INTEREST_RATE = 0.03 # 3% - constant for all bank accounts

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def summary(self):
            return f"{self.owner}: ${self.balance:2f}"
    
    @classmethod # class methods are for alternate constructors
    def open_with_bonus(cls, owner):
        return cls(owner, 100.00)
    
    @staticmethod # static methods are for helper functions in a class, similar to private functions in c++
    def is_valid_deposit(amount):
        return isinstance(amount, (int, float)) and amount > 0
        # isinstance is a built in python function that checks if an object is from the same class

if __name__ == "__main__":
    # --- instance method ---
    acc1 = Bank_Account("Alice", 500)
    print(acc1.summary()) # Alice: $500.00

    # --- class method used as a factory ---
    acc2 = Bank_Account.open_with_bonus("Bob")
    print(acc2.summary()) # Bob: $100.00

    # --- static method ---
    print(Bank_Account.is_valid_deposit(50))    # True
    print(Bank_Account.is_valid_deposit(-10))   # False

    # static method on the class method:
    print(acc2.is_valid_deposit(67)) # true