list1=[]
list2=[]
list3=[]
n=int(input())
for k in range(0,n):
    list1= input().split()
    list2.append(list1)
    
list3 = [[int(item) for item in sublist] for sublist in list2]

for i in range(len(list2)-1):
    if list2[i][i] < list2[i+1][i] and list2[i][i+1] > list2[i+1][i+1]:
        print("happy irsa")
        break
    else :   
         print("poor irsa")
         break