import json
from tabulate import tabulate
from datetime import datetime
class Expense:

    __id = 1
    __getExpense = {}

    @classmethod
    def load(Expense):
        with open("id.json", "r") as id_file:
            Expense.__id = json.load(id_file)
        
        with open("expense.json","r") as json_file:
            try:
                Expense.__getExpense = json.load(json_file)
            except json.JSONDecodeError:
                Expense.__getExpense = {}


    def __init__(self,current_time,description,amount,type):
        self.current_time = current_time
        self.description = description
        self.amount = amount
        self.type = type
        self.__id = Expense.__id
        Expense.__id += 1
        self.add()

    def writeJson():
        with open("expense.json","w") as task_file:
            json.dump(Expense.__getExpense,task_file,indent=4)

    def add(self):
        newData = {
                "id" : Expense.__id,
                "date" : self.current_time,
                "description" : self.description,
                "amount" : self.amount
            }
        
        if self.type in Expense.__getExpense:
            Expense.__getExpense[self.type].append(newData)
        else:
            Expense.__getExpense[self.type] = [newData]
        
        with open("id.json","w") as json_file:
            json.dump(Expense.__id,json_file,indent=1)

        Expense.writeJson()

    def list(type):
        if type == None:
            for x in Expense.__getExpense:
                print("\n",x.upper(),"\n")
                print(tabulate(Expense.__getExpense[x], headers="keys", tablefmt="grid"))
        else:
            for x in Expense.__getExpense:
                if x == type:
                    print("\n",x.upper(),"\n")
                    print(tabulate(Expense.__getExpense[x], headers="keys", tablefmt="grid"))
                    break

    def summary(type,month):
        sumExpense = 0
        if type != None and month != None:
            for x in Expense.__getExpense:
                if type == x:
                    for y in Expense.__getExpense[x]:
                        date_object = datetime.strptime(y["date"], "%m/%d/%y").month
                        if int(month) == date_object:
                            sumExpense += int(y["amount"])
                    print(sumExpense," dollars spent on ",type," in the ",month,"th month")
                    break
        elif type != None:
            for x in Expense.__getExpense:
                if type == x:
                    for y in Expense.__getExpense[x]:
                        sumExpense += int(y["amount"])
                    print(sumExpense,"dollars spent on ",type)
                    break
        elif month != None:
            for x in Expense.__getExpense:
                for y in Expense.__getExpense[x]:
                    date_object = datetime.strptime(y["date"], "%m/%d/%y").month
                    if int(month) == date_object:
                        sumExpense += int(y["amount"])
            print(sumExpense," dollars spent in the ",month,"th month")

    def delete(id):
        if Expense.__getExpense != {}:
            newExpense = {}
            for x in Expense.__getExpense:
                for y in Expense.__getExpense[x]:
                    if y["id"] != id:
                        if x in newExpense:
                            newExpense[x].append(y)
                        else:
                            newExpense[x] = [y]
            Expense.__getExpense = newExpense
            Expense.writeJson()
            print(id," is deleted")
        else:
            print("Not found expense")