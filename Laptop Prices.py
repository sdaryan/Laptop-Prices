list1=[]
list2=[]
list3=[]
happy=0
poor=0
n=int(input())
for k in range(0,n):
    list1= input().split()
    list2.append(list1)
    
list3 = [[int(item) for item in sublist] for sublist in list2]
i=0
for i in range(len(list3)):
    for j in range(i+1, len(list3)):
        if list3[i][0] < list3[j-i][0] and list3[i][1] > list3[j-i][1]:
            happy=happy+1
              
    
if happy >  poor :
    print  ('happy irsa')
else:
    print  ('poor irsa')