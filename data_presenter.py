import matplotlib.pyplot as plt
open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     print(line)

# for line in open_file:
#     info = line.rstrip('\n').split(",")
#     print(info[2])


# for line in open_file:
#     info = line.rstrip('\n').split(',')
#     amount = float(info[4])
#     amount = round(amount, 4)
#     print(amount)



# total = 0
# for line in open_file:
#     info = line.rstrip('\n').split(',')
#     amount = float(info[4])
#     total += round(amount, 4)

# print(total)

chocolate = 0
vanilla = 0
strawberry = 0

for line in open_file:
    info = line.rstrip('\n').split(',')
    if info[2] == 'Chocolate':
        chocolate += float(info[4])
    elif info[2] == 'Vanilla':
        vanilla += float(info[4])
    elif info[2] == 'Strawberry':
        strawberry += float(info[4])

chocolate = round(chocolate, 4)
vanilla = round(vanilla, 4)
strawberry = round(strawberry, 4)
print(f"Chocolate: {chocolate}, Vanilla: {vanilla}, Strawberry: {strawberry}")

flavors = 'Chocolate', 'Vanilla', 'Strawberry'
sales = [chocolate, vanilla, strawberry]

fig1, ax1 = plt.subplots()
ax1.pie(sales, labels=flavors, autopct='%1.1f%%')
ax1.axis('equal')
plt.show()

# open_file.close()