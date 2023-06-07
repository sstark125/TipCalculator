import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear()

print("Welcome to the Tip Calculator")
totalBill = float((input("What was the total bill?\n")))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
split = int(input("How many people to split the bill?\n"))

tipAmount = (tipPercent / 100) * totalBill
billWithTip = tipAmount + totalBill
splitCost = round(billWithTip / split, 2)

print(f"Each person should pay: {splitCost}")