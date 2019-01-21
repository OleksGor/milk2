"""
ID: alex.go2
LANG: PYTHON3
TASK: milk2
"""
f = open("milk2.in", "r")
g = open ("milk2.out", "w")
readfile = f.readlines()
n = int(readfile[0])
arrold = []
arrmid = []
arr = []
finaltotalx = 0
totalsx = []
finaltotaly = 0
totalsy = []

for x in range(1, int(readfile[0])+1): 
    arrold.append([int(readfile[x].split(" ")[0]), int(readfile[x].split(" ")[1])])

"""sorts that array"""
def quicksort(arr):
    if len(arr)==0: return []
    if len(arr)==1: return arr
    left = [i for i in arr[1:] if int(i[0])<int(arr[0][0])]   
    right = [i for i in arr[1:] if int(i[0])>=int(arr[0][0])] 
    return quicksort(left)+[arr[0]]+quicksort(right)
arrmid = quicksort(arrold).copy()


High = arrmid[0][1]
arr.append(arrmid[0])
for x in range (0, n - 2):
    if arrmid[x + 1][1] > High:
        arr.append(arrmid[x + 1])
        High = arrmid[x+1][1]
arr.append(arrmid[len(arrmid)- 1])
HighestTime = arr[0][1]
LowestTime = arr[0][0]

"""if array only has one elements"""
if len(arr) == 1:
    finaltotalx = int(arr[0][1]) - int(arr[0][0])
for x in range (0, len(arr) - 1):
    if arr[x + 1][0] <= arr[x][1]:
        if arr[x + 1][1] > HighestTime:
            HighestTime = arr[x + 1][1]
    else:
        if HighestTime - LowestTime > finaltotalx:
            finaltotalx = HighestTime - LowestTime
        if arr[x+1][0] - arr[x][1] > finaltotaly:
            finaltotaly = arr[x+1][0] - arr[x][1]
        LowestTime = int(arr[x + 1][0])
        HighestTime = int(arr[x + 1][1])
if HighestTime - LowestTime > finaltotalx:
    finaltotalx = HighestTime - LowestTime


if arr[0][1] > arr [len(arr)-1][1]:
    finaltotaly = 0
g.write(str(finaltotalx) + " " + str(finaltotaly) + "\n")
g.close()



