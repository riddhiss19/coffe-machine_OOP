from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from colorama import Fore, Back, Style

menu=Menu()
machine=CoffeeMaker()
money=MoneyMachine()

is_on=True
str=menu.get_items()

while is_on:
    
    print("_________________________"+Fore.GREEN+Style.BRIGHT+"\nWELCOME TO COFFEE MACHINE\n"+"_________________________") 
    ch=input(f"\n{Fore.MAGENTA}***** MENU *****\n{Fore.RED}DRINK\t  COST\n{Fore.BLUE} {str}\n{Fore.YELLOW} \n What would you like?:")
    if(ch=="report"):
        machine.report()
        money.report()
    elif ch=="off":
        is_on=False
    else:
        item=menu.find_drink(ch)
        if(item!= None):
            if (machine.is_resource_sufficient(item)):
                if(money.make_payment(item.cost)):
                    machine.make_coffee(item)
                    
           
           


    
