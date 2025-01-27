__author__ = "Rogine Mirando"
__version__ = "1.0.0"

class BankAccount:
    """
    A class that containts bank account information
    """
    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes the bank account information based on the values
        Args:
            account_number (int): The account number
            client_number (int): The client number
            balance (float): The balance of the bank account
        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Enter a valid account number")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Enter a valid client number")

        if isinstance(balance, float):
            self.__balance = balance
        else:
            self.__balance = 0.0
            raise ValueError("Enter a numeric")

    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute
        Returns: int - The account number
        """
        return self.__account_number
        
    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute
        Returns: int - the client number
        """
        return self.__client_number
        
    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute
        Returns: float - the balance in the bank account
        """
        return self.__balance
        
    def update_balance(self, amount) -> None:
        """
        Updates the account balance
        Args:
            amount (float): The amount that will be added to the balance
        """
        if isinstance(amount, float):
            self.__balance += amount
        else:
            # If the amount is not a float
            try:
                # This will try to check if amount can be converted into a float. Ex) 120 turns into 120.00
                self.__balance += float(amount)
            except ValueError:
                # if all fails, the balance will not be changed
                print("The amount is not valid")

    def deposit(self, amount: float) -> None:
        """
        Allows to make a deposit
        Args:
            amount (float): the amount that will be deposited
        """
        if isinstance(amount, float):
            if amount <= 0:
                raise ValueError(f"Deposit Amount: {amount} must be a positive number")
            else:
                self.update_balance(amount)
        else:
            try:
                # Just in case the amount is an integer and not a float, this will convert it into a float
                float_amount = float(amount)
                if float_amount <= 0:
                    raise ValueError(f"Deposit Amount: {float_amount} must be a positive number")
                else:
                    self.update_balance(float_amount)
            except ValueError:
                # If the amount is not a numeric
                print(f"Deposit amount: {amount} must be numeric")

    def withdraw(self, amount:float) -> None:
        """
        Allows to make withdrawals
        Args:
            amount (float): The amount of the withdrawal
        """
        if isinstance(amount, float):
            if amount <= 0:
                raise ValueError(f"Withdrawal amount: {amount} must be positive")
            elif amount > self.__balance:
                raise ValueError(f"Withdrawal amount: {amount} must not exceed the account balance {self.__balance}")
            else:
                self.update_balance(-amount)
        else:
            try:
                # Just in case the amount is an integer and not a float, this will convert it into a float
                float_amount = float(amount)
                if float_amount <= 0:
                    raise ValueError(f"Withdrawal Amount: {float_amount} must be a positive number")
                else:
                    self.update_balance(-float_amount)
            except ValueError:
                # If the amount is not a numeric
                print(f"Withdrawal amount: {amount} must be numeric")
                
    def __str__(self) -> str:
        """
        Returns a string of that shows the values of the attributes in the class
        Returns: str - The BankAccount instance as a formatted string
        """
        return (f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}")