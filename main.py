import argparse
from expense import Expense 
import datetime

parser = argparse.ArgumentParser(description="Expense")

subparsers = parser.add_subparsers(dest='command', help='commands')
add_parser = subparsers.add_parser('add', help='Expense Add')
list_parser = subparsers.add_parser("list",help="List Expense")
summary_parser = subparsers.add_parser("summary",help="List Expense")
delete_parser = subparsers.add_parser("delete",help="Delete Expense",)

add_parser.add_argument("--description", type=str, help="description")
add_parser.add_argument("--amount", type=str, help="amount")
add_parser.add_argument("--type", type=str,help = "type")
summary_parser.add_argument("--month",type=str,help="month")
summary_parser.add_argument("--type",type=str,help="type")
list_parser.add_argument("--type",type=str,help="type")
delete_parser.add_argument("id", type=int, help="ID of the expense to delete")

args = parser.parse_args()

Expense.load()
if args.command == "add":
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%x")
    Expense(current_time,description=args.description,amount=args.amount,type=args.type),
    print("Expense added for ",args.type)
elif args.command == "list":
    Expense.list(type = args.type)
elif args.command == "summary":
    Expense.summary(type = args.type,month = args.month)
elif args.command == "delete":
    Expense.delete(args.id)