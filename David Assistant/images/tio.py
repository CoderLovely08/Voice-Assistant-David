dict1={"subject":"python","marks":80,"result":"pass","book":"PWPbook"}
print("Original dictionary: ",dict1)
print("-"*90)
dict1["syallbus"]="6units"
print("After addding new element:",dict1)
print("-"*90)
print("element which pop out is: ",dict1.pop("book"))
print(dict1)
print("-"*90)
print("pop item is: ",dict1.popitem())
print(dict1)
print("-"*90)
print("updated values: ")
dict1["marks"]=100
print(dict1)







































#set1 = {10,55.63,'Python', 'html',101}
#print("original set: ",set1)
#print("-"*50)
#v1=int(input("Enter integer value to add in set: "));
#v2=str(input("Enter string value to add in set: "));
#set1.add(v1)
#set1.add(v2)
#print("updated set: ",set1)
#print("-"*50)
#v3=input("Enter value for remove from the list: ")
#set1.remove(v3)
#print("After deletion: ",set1)
