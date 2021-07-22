from .models import Transaction
def chart():

    dataset1 = {"Week 1": 0, "Week 2": 0,"Week 3": 0,"Week 4": 0}
    dataset2 = {"Week 1": 0, "Week 2": 0,"Week 3": 0,"Week 4": 0}

    #add data to structure
    trans_data = Transaction.objects.all()
    for e in trans_data:
        data_day = int(e.date.day)
        if e.ammount < 0:
            if data_day < 7:
                key = "Week 1"
                new = add(dataset2.get(key) , e.ammount)
            elif data_day < 14:
                key = "Week 2"
                new = add(dataset2.get(key) , e.ammount)
            elif data_day < 21:
                key = "Week 3"
                new = add(dataset2.get(key) , e.ammount)
            else:
                key = "Week 4"
                new = add(dataset2.get(key) , e.ammount)

            dataset2[key] = new
        else: 
            if data_day < 7:
                key = "Week 1"
                new = add(dataset1.get(key) , e.ammount)
            elif data_day < 14:
                key = "Week 2"
                new = add(dataset1.get(key) , e.ammount)
            elif data_day < 21:
                key = "Week 3"
                new = add(dataset1.get(key) , e.ammount)
            else:
                key = "Week 4"
                new = add(dataset1.get(key) , e.ammount)
            dataset1[key] = new

    dataset1_labels = []
    dataset1_data = []
    dataset2_data = []
    dataset3_data = []
    for e in dataset1:
        day_data = e
        amnt = dataset1.get(e)
        dataset1_labels.append(day_data)
        dataset1_data.append(amnt)
    for e in dataset2:
        day_data = e
        amnt = dataset2.get(e)
        dataset2_data.append(amnt)

    for e, a in zip(dataset1_data, dataset2_data):
        if not e:
            e = 0
        if not a:
            a = 0
        new = e + a
        dataset3_data.append(new)



        

    context = {}
    context['sales_data'] = dataset1_data
    context['transaction_labels'] = dataset1_labels
    context['expense_data'] = dataset2_data
    context['profit_data'] = dataset3_data
    return context

def add(value, value2):
    if value:
        return value + value2
    else:
        return value2