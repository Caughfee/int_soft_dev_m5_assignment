__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()  # Close the window if invalid account type
            return

        # Store a deep copy of the account to avoid modifying the original directly
        self.account = copy.deepcopy(account)

        # Populate labels with formatted account data
        self.account_number_label.setText(f"Account Number: {self.account.account_number}")
        self.balance_label.setText(f"Balance: ${self.account.balance:.2f}")  # Format balance as currency

        # Connect buttons to corresponding methods
        self.deposit_button.clicked.connect(self.on_apply_transaction)  # Connect deposit button
        self.withdraw_button.clicked.connect(self.on_apply_transaction)  # Connect withdraw button
        self.exit_button.clicked.connect(self.on_exit)  # Connect exit button

        def on_apply_transaction(self):
            pass

        def on_exit(self):
            pass
        
