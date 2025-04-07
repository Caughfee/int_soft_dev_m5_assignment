__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Rogine"

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from bank_account import BankAccount, ChequingAccount, SavingsAccount, InvestmentAccount
from client.client import Client

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************






def load_data()->tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Extracting and converting data from the row
                client_number = int(row['client_number'])
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email_address']

                
                # Creating a Client object and storing it in the dictionary
                client_listing[client_number] = Client(client_number, first_name, last_name, email)
            except Exception as e:
                logging.error(f"Unable to create client: {e}")
        

    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Extract and convert account data
                account_number = int(row['account_number'])
                client_number = int(row['client_number'])
                balance = float(row['balance'])
                date_created = datetime.fromisoformat(row['date_created'])
                account_type = row['account_type'].strip()

                # Verify client_number exists
                if client_number not in client_listing:
                    raise ValueError(f"Bank Account: {account_number} contains invalid Client Number: {client_number}")

                # Create appropriate account object
                if account_type == "ChequingAccount":
                    overdraft_limit = float(row.get('overdraft_limit', 0))
                    overdraft_rate = float(row.get('overdraft_rate', 0))
                    account = ChequingAccount(account_number, client_number, balance, date_created,
                                              overdraft_limit, overdraft_rate)
                elif account_type == "SavingsAccount":
                    minimum_balance = float(row.get('minimum_balance', 0))
                    account = SavingsAccount(account_number, client_number, balance, date_created,
                                              minimum_balance)
                elif account_type == "InvestmentAccount":
                    management_fee = float(row.get('management_fee', 0))
                    account = InvestmentAccount(account_number, client_number, balance, date_created,
                                                 management_fee)
                else:
                    raise ValueError(f"Not a valid account type.")

                # Store the account in the dictionary
                accounts[account_number] = account
            except Exception as e:
                logging.error(f"Unable to create bank account: {e}")

    # RETURN STATEMENT
    return client_listing, accounts

def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")