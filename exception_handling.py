try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
   
    print(a/b)

except ZeroDivisionError:
    print("zero divisor error")

except TypeError:
    print("type error")

except ValueError:
    print("Wrong value was given")
finally:
    print("Execution done !!")