List=[5,35,10,20,25,40,30,15]
print("Original List: ",List)
Count=0
for i in List:
    Count+=i
Average=Count/len (List)
print ("Sum= ",Count)
print ("Aversge= ",Average)
List.sort()
print("Smallest element is: ",List[0])
print("Largest Elemnt is: ",List[-1])

