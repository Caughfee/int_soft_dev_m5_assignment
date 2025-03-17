"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client





# 2. Create a Client object with data of your choice.
client_1 = Client(101, "Anby", "Demara", "anby.demara@gmail.com")



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = ChequingAccount(123, 101, 1000.00, date(2022, 1, 1), 500.0, 0.05)
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_account = SavingsAccount(321, 101, 2000.00, (2022, 1, 1), 100.00)




# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account.attach(client_1)
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account.attach(client_1)





# 5a. Create a second Client object with data of your choice.
client_1 = Client(102, "Billy", "Kid", "billy.kid@gmail.com")
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account = SavingsAccount(456, 102, 1245.00, (2023, 1, 1), 100.00)




# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

