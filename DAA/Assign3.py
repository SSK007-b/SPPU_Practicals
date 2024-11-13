def greedy(arr, capacity):
    totalProfit = 0
    for item in arr:
        if item[2] <= capacity:
            capacity -= item[2]
            totalProfit += item[1]
            item.append(1)
        else:
            fraction = capacity/item[2]
            totalProfit += item[1]*fraction
            item.append(fraction)

    for item in arr:
        if len(item) >= 4:
            print(f"The Object Selected = {item[0]} and fraction is {item[4]}")

    print("The Total Profit is ", totalProfit)

n = int(input("Enter the Number of Objects "))
capacity = int(input("Enter the Capacity "))

process = []

for i in range(n):
    temp = []
    temp.append(i+1)
    profit = int(input("Enter the Profit "))
    temp.append(profit)
    weight = int(input("Enter the Weight "))
    temp.append(weight)
    temp.append(profit/weight)
    process.append(temp)

print('Id\tProfit\tWeight\tRatio')
for i in process:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")

process.sort(key=lambda x:x[3], reverse=True)
greedy(process, capacity)