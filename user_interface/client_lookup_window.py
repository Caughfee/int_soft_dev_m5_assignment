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
    def __init__(self) -> None:
        super().__init__()

        # Connect events to the buttons
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)
        self.filter_button.clicked.connect(self.on_filter_clicked)
        

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

    @Slot()
    def on_lookup_client(self):
        """
        Retrieves and displays client and account information based on client number input.

        Exceptions:
            - Displays an error if the client number is not numeric.
        """
        try:
            client_number = int(self.client_number_edit.text().strip())

        except ValueError:
            QMessageBox.warning(self, "Input Error","The client number must be a numeric value.")

            self.reset_display()

            return
        
        client = (self.client_listing.get(client_number))
        if not client:
            QMessageBox.warning(self, "Not Found", f"Client number: {client_number} not found.")

            self.reset_display()
            return
        
        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        self.account_table.setRowCount(0)

        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(account._date_created.strftime('%Y-%m-%d')))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

                for column in range(4):
                    item = self.account_table.item(row_position, column)
                    if column == 1:
                        item.setTextAlignment(Qt.AlignRight) #align balance column to the right
                    else:
                        item.setTextAlignment(Qt.AlignCenter) # align the rest of the columns to the center

        self.account_table.resizeColumnsToContents()

        # toggle filter to indicate data is NOT filtered
        self.toggle_filter(False)
                
    @Slot()
    def on_text_changed(self):
        """
        clears all account records from the account_table
        """
        self.account_table.setRowCount(0) # removes all rows
    
    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """
        Handles the selection of an account from the account table.

        Args:
            row (int): The row index of the selected cell
            column (int): The column index of the selected cell

         Displays warning messages if:
            The selected cell doesn't contain valid data
            The account number cannot be converted to an integer
        """
        item = self.account_table.item(row, 0) # column 0 is the account number

        if item is None or item.text().strip() == "":
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return
        
        try:
            account_number = int(item.text().strip()) # Convert to integer
        except ValueError:
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return

        # check if account exists in self.accounts
        if account_number in self.accounts:
            selected_account = self.accounts[account_number]
            
            account_details_dialog = AccountDetailsWindow(selected_account)

            # Connect the balance_updated signal to the update_data slot
            account_details_dialog.balance_updated.connect(self.update_data)

            account_details_dialog.exec()

    @Slot()
    def on_filter_clicked(self) -> None:
        """
        Handles filtering rows in the account table based on the defined criteria
        """

        if self.filter_button.text() == "Apply Filter":
            filter_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().strip()

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_index)

                if item and filter_text.lower() in item.text().lower():
                    self.account_table.setRowHidden(row, False) # show matching

                else:
                    self.account_table.setRowHidden(row, True) # hide non matching

            self.toggle_filter(True)

        else:
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

                self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool) -> None:
        """
        Toggles the display of filter widgets / indicates whether the user if its filtering or not.
        """

        # Set the filter button true initially
        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0) # set the current index to 0

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

