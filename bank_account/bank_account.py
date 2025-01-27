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
            self.balance = balance
        else:
            self.balance = 0.0

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
                self.balance += amount
            else:
                # If the amount is not a float
                try:
                    # This will try to check if amount can be converted into a float. Ex) 120 turns into 120.00
                    self.balance += float(amount)
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
                        raise ValueError(f"Deposit Amount: {amount} must be a positive number")
                    else:
                        self.update_balance(float_amount)
                except ValueError:
                    # If the amount is not a numeric
                    print(f"Deposit amount: {amount} must be numeric")

        
                



        

