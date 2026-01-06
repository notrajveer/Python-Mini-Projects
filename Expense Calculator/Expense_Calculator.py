rent = int(input("Enter your monthly rent: "))
bills = int(input("Enter your bills (electricity, water, etc.: "))
misc = int(input("Enter your miscellanious expenses: "))
num = int(input("Enter total number of people in the flat: "))
final = (rent + bills + misc)/num
print(f"Each person has to pay {final} rupees.")