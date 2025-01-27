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
        
        
