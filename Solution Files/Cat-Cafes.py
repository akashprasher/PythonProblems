cafes = {}

while True:
    try:
        name, visitors = input().split()
        cafes.update({name: int(visitors)})
    except ValueError:
        break

print(max(cafes, key=cafes.get))