__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
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

    @Slot()
    def on_apply_transaction(self) -> None:
        """
        Handles deposit and withdrawal transactions for the bank account.
        
        Raises:
            Displays warning dialog if amount is not numeric
            Displays warning dialog with error message if transaction fails
        """

        try:
            # Convert transaction amount to float
            amount = float(self.transaction_amount_edit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            # Determine which button was clicked
            sender = self.sender()
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)  # Execute deposit
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)  # Execute withdrawal
            else:
                return  # If no valid button was clicked, exit
            
            # Emit the balance_updated signal after a successful transaction
            self.balance_updated.emit(self.account)  # Send updated BankAccount 
            
            # Update balance label
            self.balance_label.setText(f"Balance: ${self.account.balance:.2f}")

            # Clear transaction amount field and reset focus
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.warning(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    @Slot()
    def on_exit(self):
        """
        Handles closing the QDialog
        """
        self.close()
        
