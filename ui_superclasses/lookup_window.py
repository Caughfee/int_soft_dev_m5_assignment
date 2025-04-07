__author__ = "ACE Faculty"
__version__ = "1.0.0"

from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QComboBox, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from user_interface.manage_data import load_data

class LookupWindow(QMainWindow):
    """
    A Python class which allows users to retrieve Client 
    information.
    """    

    def __init__(self):
        """
        Initializes the Client Lookup window by adding 
        various widgets and setting properties. Widgets include: client_number_edit, 
        client_info_label, lookup_button and account_table.
        """
        super().__init__()

        # Call the load_data method
        client_data, account_data = load_data()
        self.client_listing = client_data
        self.accounts = account_data

        COLUMN_HEADERS = ["Account Number", "Balance", "Date Created", "Account Type"]

        self.setWindowTitle("Client Lookup")
        self.resize(600, 400) 

        # Main layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QGridLayout(centralWidget)

        # Bold font for labels and headers
        bold_font = QFont()
        bold_font.setBold(True)

        # Widgets
        self.prompt_label = QLabel("Enter Client Number:")
        self.prompt_label.setFont(bold_font)
        self.client_number_edit = QLineEdit()
        self.lookup_button = QPushButton("Lookup Client")
        self.lookup_button.setDefault(True)

        self.client_info_label = QLabel()
        self.account_table = QTableWidget()
        self.prompt_label.setAlignment(Qt.AlignCenter)
        self.client_number_edit.setAlignment(Qt.AlignCenter)
        self.client_info_label.setAlignment(Qt.AlignCenter)

        # Assignment 5 Widgets
        self.filter_label = QLabel("Data is Not Currently Filtered")
        self.filter_label.setFont(bold_font)
        self.filter_edit = QLineEdit()
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(COLUMN_HEADERS)
        self.filter_button = QPushButton("Apply Filter")

        # Adjusting layout to make widgets centered in the middle column of a 3-column layout
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(2, 1)

        # Add widgets to the layout, placing them in the second (middle) column
        layout.addWidget(self.prompt_label, 0, 1)
        layout.addWidget(self.client_number_edit, 1, 1)
        layout.addWidget(self.lookup_button, 2, 1)
        layout.addWidget(self.client_info_label, 3, 1)

        
        # Table (for BankAccount data) span all columns
        layout.addWidget(self.account_table, 4, 0, 1, 3)  

        # Add Assignment 5 Widgets
        layout.addWidget(self.filter_label, 5, 0)
        layout.addWidget(self.filter_combo_box, 6, 0)
        layout.addWidget(self.filter_edit, 6, 1)
        layout.addWidget(self.filter_button, 6, 2)

        self.account_table.setColumnCount(4)
        self.account_table.setHorizontalHeaderLabels(COLUMN_HEADERS)                
        self.account_table.horizontalHeader().setFont(bold_font)
        self.account_table.resizeColumnsToContents()
        self.account_table.resizeRowsToContents()
        self.reset_display()

        # Connect events to the buttons
        self.lookup_button.clicked.connect(self.on_lookup_client)
        #self.client_number_edit.textChanged.connect(self.on_text_changed)
        #self.account_table.cellClicked.connect(self.on_select_account)


    def reset_display(self):
        """
        Resets the display.

        This function Clears contents of display fields client_number_edit, client_info_label 
        and account_table, and resets focus to the client_number_edit.

            reset_display()

        Note that the function does not return anything.
        """
        self.account_table.setRowCount(0)
        self.client_number_edit.clear()
        self.client_info_label.setText("")
        self.client_info_label.setFocus()
        self.filter_edit.setText("")
        self.filter_combo_box.setCurrentIndex(0)
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)
        self.filter_label.setEnabled(False)

    def on_lookup_client(self):
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
                

   