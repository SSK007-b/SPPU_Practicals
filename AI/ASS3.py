class Greedy:

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][2] > R[j][2]:
                    arr[k] = L[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1  
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def job(self, arr, t):

        self.mergeSort(arr)
        result = [False] * t
        job = ['-1'] * t
        total_profit = 0

        for i in range(len(arr)):
            for j in range(min(t-1, arr[i][1]-1),-1,-1):
                if result[j] == False:
                    result[j] = True
                    job[j] = arr[i][0]
                    total_profit += arr[i][2]
                    break
        print("The Job Sequece is", job)
        print("The Maximum Profit is: ",total_profit)

if __name__ == "__main__":
    g = Greedy()
    n = int(input("Enter the number of Jobs: "))
    arr = []
    for i in range(n):
        Job_ID = input("Enter the Job_ID: ")
        deadline = int(input("Enter the deadline: "))
        profit = int(input("Enter the Profit: "))
        arr.append([Job_ID, deadline, profit])

    t = int(input("Enter the number of Time slots: "))
    g.job(arr, t)
