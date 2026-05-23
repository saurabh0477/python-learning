num= int(input("Enter a number to get table: "))
table=[num*i for i in range(1,11)]
print(table)
table2=[f"table of: {num}:- "]
for i in table:
    table2.append(str(i))
    table2.append(" ")
table2.append("\n")
with open("table.txt","a")as f:
    f.writelines(table2)