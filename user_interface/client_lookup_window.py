__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Rogine"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    @Slot(BankAccount)
    def update_data(self, updated_account: BankAccount) -> None:
        """Updates the balance in the table and accounts dictionary after a signal is received."""
        
        # Loop through the rows of the account_table
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)  # Get account number from the first column
            if item and int(item.text()) == updated_account.account_number:
                # Update balance in the second column (formatted as currency)
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${updated_account.balance:.2f}"))
                break

        # Update the accounts dictionary
        self.accounts[updated_account.account_number] = updated_account

        # Persist changes to the CSV file
        update_data(updated_account)
        
