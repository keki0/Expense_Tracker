import json
import os

class Expense:
    def __init__(self,expense_id,category,amount):
        self.expense_id = expense_id
        self.category=category
        self.amount=amount

    def to_dict(self):
        return {
            'expense_id':self.expense_id,
            'category':self.category,
            'amount': self.amount
        }
    

class ExpenseManager:
    def __init__(self,file_path):
        self.file_path=file_path
        self.expenses=[]
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.file_path):
            with open(self.file_path,'r') as file:
                self.expenses = [Expense(**expense) for expense in json.load(file)]
        else:
            self.expenses=[]

    def save_expenses(self):
        with open(self.file_path,'w') as file:
            json.dump([expense.to_dict() for expense in self.expenses], file)

    def get_all_expenses(self):
        return self.expenses
    
    def add_expenses(self,category,amount):
        expense_id=len(self.expenses)+1
        new_expense=Expense(expense_id,category,amount)
        self.expenses.append(new_expense)
        self.save_expenses()

    def delete_expenses(self,expense_id):
        self.expenses=[expense for expense in self.expenses if expense.expense_id != expense_id]
        self.save_expenses()

    def get_expenses_by_category(self):
        expenses_by_category={}
        for expense in self.expenses:
            if expense.category in expenses_by_category:
                expenses_by_category[expense.category] += expense.amount
            else:
                expenses_by_category[expense.category]= expense.amount
        return expenses_by_category