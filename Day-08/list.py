list = ["server1","server2","server3"]
#adding new element
list.append("server4")
print(list)
#removing element from the list
list.remove("server3")
print(list)
#creating new list from the list
new_list= list[0:3]
print(new_list)
#calling the first element of list
print(new_list[0])
#combining the list 
new_list2= new_list + ["server3","server5"]
print(new_list2)