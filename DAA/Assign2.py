import heapq

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
    def __lt__(self, others):
        return self.freq < others.freq
    
char = []
freq = []

string = input("Enter the String/Text ").lower()

for i in string:
    if i != " " and i not in char:
        char.append(i)

print(f"The Char Array = {char}")

for i in char:
    count = 0
    for j in string:
        if i == j:
            count += 1
    freq.append(count)
print(f"The Frequency Array = {freq}")

for i in range(len(freq)):
    for j in range(len(freq)-i-1):
        if freq[j] > freq[j+1]:
            freq[j], freq[j+1] = freq[j+1], freq[j]
            char[j], char[j+1] = char[j+1], char[j]
print(f"The Sorted Char Array = {char}")
print(f"The Sorted Frequency Array = {freq}")

def printNode(node, val = " "):
    if node.left:
        printNode(node.left, val + "0")
    if node.right:
        printNode(node.right, val + "1")
    if not node.left and not node.right:
        print(f"{node.symbol} -> {val}")
nodes = []

for i in range(len(char)):
    heapq.heappush(nodes, node(freq[i], char[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

printNode(nodes[0])
