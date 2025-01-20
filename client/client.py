__author__ = "Rogine Mirando"
__version__ = "1.0.0"

class Client:
    """
    A class that manages client information
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes the client information based on the values
        Args:
            client_number (int): The client's number
            first_name (str): The first name of the client
            last_name (str): The last name of the client
            email_address (str): The email address of the client
        Raises:
            ValueError: If any of the arguments are invalid
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name must be filled.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name must be filled.")
        
        if len(email_address.strip()) > 0:
            self.__email_address = email_address
        else:
            raise ValueError("Email address must be filled.")