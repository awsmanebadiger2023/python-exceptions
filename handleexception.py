import sys

boys=int(input("enter boys number:::::"))
girls=int(input("enter girls number:::::"))

try:
    print("Ration of Boys to Girls is::::",boys/girls)

except BaseException as be:
    print("BaseException Exception Occured::::", be, "")
    sys.exit()
except ZeroDivisionError as ze:
    print("ZeroDivisionError Exception Occured::::", ze, "")
finally:
    print("Program is Finished")