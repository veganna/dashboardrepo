from django.shortcuts import render
import requests, json
from .models import tasks
from .models import Transaction
from django.db.models import Sum
from .charts import *
from datetime import datetime
from django.contrib.auth import get_user as user

def get_chart():
    total_profit = Transaction.objects.aggregate(Sum('ammount'))
    final = total_profit.get('ammount__sum')
    formatted = "{:.2f}".format(final)
    trans = Transaction.objects.all().values('ammount')
    expenses = []
    sales = []
    for v in trans:
        if v.get('ammount') > 0:
            sales.append(v.get('ammount'))   
        else:
            expenses.append(v.get('ammount'))        

    total_expenses = sum(expenses)
    total_sales = sum(sales)
    context = {}
    avg = sum(sales)/len(sales)
    avg_filal = "{:.2f}".format(avg)
    context['profit'] = formatted
    context['expenses'] = total_expenses
    context['sales'] = total_sales
    context['average'] = avg_filal
    chart_data = chart()
    context['sales_data'] = chart_data.get('sales_data')
    context['transaction_labels'] = chart_data.get('transaction_labels')
    context['expense_data'] = chart_data.get('expense_data')
    context['profit_data'] =chart_data.get('profit_data')
    return context

def get_sales_list():
    db_list = Transaction.objects.all()
    sales_trans_list = []
    for each in db_list:
        if each.ammount > 0:
            sales_trans_list.append([each.name, float(each.ammount), each.category_type.category_name, each.date.strftime('%d, %b %Y')])

    return sales_trans_list

def get_expenses_list():
    db_list = Transaction.objects.all()
    expenses_trans_list = []
    for each in db_list:
        if each.ammount < 0:
            expenses_trans_list.append([each.name, float(each.ammount), each.category_type.category_name, each.date.strftime('%d, %b %Y')])

    return expenses_trans_list



def overview(request):
    context = get_chart()
    return render(request, "core/dashboard/overview.html", context)
    
    
def sales(request):
    context = get_chart()
    sales_trans_list = get_sales_list()
    context['sales_list'] = sales_trans_list
    return render(request, "core/dashboard/sales.html", context)

def expenses(request):
    context = get_chart()
    expenses_trans_list = get_expenses_list()
    context['expenses_list'] = expenses_trans_list
    return render(request, "core/dashboard/expenses.html", context)

 
def profile_view(request):
    context = []
    header = 'application/json'
    motivational = requests.get('https://zenquotes.io/api/random',)  
    context = json.loads(motivational.text)
    context = context[0]
    return render(request, "accounts/profile.html", {"motivational":context['q']} )

def task(request):
    task = tasks.objects.all()
    return render(request, 'core/task.html', {'task':task} )