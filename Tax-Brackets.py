interest_range = {132406: 28, 42707: 25, 15527: 15, 0: 0}
income = int(input())
for i in interest_range:
    if income > i:
        print(f"The tax for {income} is {interest_range[i]}%. That is {round(income * interest_range[i] / 100)} dollars!")
        break