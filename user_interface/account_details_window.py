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
            QMessageBox.warning(self, "Invalid Account", "Invalid Bank Account provided.")
            self.reject()
            return
 
        self.account = copy.copy(account)  
 
        self.account_number_label.setText(f"Account Number: {self.account.account_number}")
        self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
 
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)
 
    def on_apply_transaction(self) -> None:
        """
        Handles both deposit and withdrawal transactions.
        Determines if the user wants to deposit or withdraw, performs the transaction,
        and updates the balance.
        """
 
        try:
            transaction_amount = float(self.transaction_amount_edit.text().strip())
            if transaction_amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
 
        transaction_type = ""
        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(transaction_amount)  
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(transaction_amount)  
        except Exception as e:
            QMessageBox.warning(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            return
 
        self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
 
        self.transaction_amount_edit.clear()
        self.transaction_amount_edit.setFocus()
 
        self.balance_updated.emit(self.account)
 
    def on_exit(self) -> None:
        """
        Closes the AccountDetailsWindow when the exit button is clicked.
        """
