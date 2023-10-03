# 1. Stwórz pustą listę o nazwie "numbers".
numbers = []
12
# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
print(numbers)

i = 0
while i < 5:
    inp = int(input("dodaj do listy: "))
    numbers.append(inp)
    print(numbers)
