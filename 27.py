l=[
    {
        "name":"puneeth",
        "food":"jamoon"
    },
    {
        "name":"arohi",
        "food":"juice"
    }
]
for persons in l:
    print(persons ["name"], "=", persons ["food"])



s = int(input("Enter the number of rows:"))
matrix = []
for i in range(rows):
    rows = [int (num) for num in input(f"Enter row {i+1}:").split()]
    matrix.append (rows)

    print(matrix)



rows = int(input("Enter the number of rows:"))  
coloumns = int(input("Enter the number of coloumns:"))

matrix = []
for i in range (rows):
    row = []
    for j in range(coloumns):
        x = int(input("Enter the elements:"))
        row.append(row)
    matrix.append(row)

print(matrix)
