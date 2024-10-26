from flask import Flask, render_template, request, redirect, jsonify, url_for
from models import ExpenseManager

app = Flask(__name__)
expense_manager = ExpenseManager('expenses.json')

@app.route('/')
def index():
    expenses = expense_manager.get_all_expenses()
    return render_template('index.html',expenses=expenses)

@app.route('/add_expense',methods=['POST'])
def add_expense():
    data=request.json
    expense_manager.add_expenses(data['category'],data['amount'])
    return jsonify({'status':'Expense Added Successfully'})

@app.route('/delete_expense/<int:expense_id>',methods=['DELETE'])
def delete_expense(expense_id):
    expense_manager.delete_expense(expense_id)
    return jsonify({'status':'Expense Deleted Successfully'})

@app.route('/view_chart')
def view_chart():
    expenses_by_category = expense_manager.get_expenses_by_category()
    return render_template('chart.html',expenses_by_category=expenses_by_category)



if __name__ == '__main__':
    app.run(debug=True)