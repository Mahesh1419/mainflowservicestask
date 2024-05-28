#creating a list of elements 
my_ownlist = [12,13,14,15,16]
#adding  element to my created list
my_ownlist.append(17)
print("list after adding element:",my_ownlist)
#removing element from created list
my_ownlist.remove(16)
print("list after removing element:",my_ownlist)
#modifying the elements in created list
my_ownlist[0]=20
print("list after modifying element:",my_ownlist)
print("new list with updates:",my_ownlist)

#creating a dictionary
my_dict={'sam':11,'mike':12,'sisu':13}
#adding key value pair to the dictionary
my_dict ['maya']=14
print("dictionary after adding:",my_dict)
#removing key value pair from the dictionary
del my_dict['sam']
print("dictionary after removing:",my_dict)
#modifying key value pair of the dictionary
my_dict['mike']=1222
print("dictionary after modification:",my_dict)
print("updated dictionary:",my_dict)

#creating a set
my_set={11,12,13,14,15}
#adding element into set
my_set.add(16)
print("set after adding:",my_set)
#removing element from set
my_set.remove(11)
print("set after removing :",my_set)
#modifying the set 
my_set.discard(13)
print("set after modifying:",my_set)
print("updated set:",my_set)