__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Slot

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()
     # attributes set to value of dictionary and load_method called
        self.client_listing, self.accounts = load_data()
       
        #establishing connnections
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        #self.account_table.cellClicked.connect(self.on_select_account)
   
    @Slot()  
    def on_lookup_client(self):
       
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return
        """
        it will obtain the client number entered into the client number edit widget
        and convert into integer and if it fails to convert to integer, it willl cause an exception.
        """    
           
 
        # check if client exists in dictionary
        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return
       
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")
       
        self.account_table.setRowCount(0)
       
        """
        if client number of client object matches the client number
        it will add row to account table.
        """
       
        for account in self.accounts.values():
            if account.client_number == client_number:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
           
                # creating table items  
                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:.2f}")
                date_created_item = QTableWidgetItem(account.date_created)
                account_type = QTableWidgetItem(account.__class__.__name__)  
           
                # adding items to the table
                self.account_table.setItem(account_count, 0, account_number_item)
                self.account_table.setItem(account_count, 1, balance_item)
                self.account_table.setItem(account_count, 2, date_created_item)
                self.account_table.setItem(account_count, 3, account_type)              
           
                account_count += 1
           
        self.account_table.resizeColumnsToContents()
 
    @Slot()
    def on_text_changed(self) -> None:
        self.account_table.setRowCount(0)
 
    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        account_number_item = self.account_table.item(row, 0)
 
        if not account_number_item or not account_number_item.text():
            QMessageBox.warning(self, "Invalid selection", "Please select a valid record")
            return
 
        account_number = int(account_number_item.text().strip())
 
        if account_number in self.accounts:
            account = self.accounts[account_number]
 
            account_details_window = AccountDetailsWindow(account)
            account_details_window.exec_()
        else:
            QMessageBox.warning(self, "No Bank Account", "Bank Account selected does not exist.")
        
