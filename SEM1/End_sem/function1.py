def modify_int(x):
     x+=10
     print ("inside the function" , x)
num = 5
modify_int(num)
print("outside the function",num)



def modify_string(s):
     s += "World!"
     print("inside the function", s)
greeting="Hello "
modify_string(greeting)
print("outside the function ", greeting)

def modify_tuple(t):
     t+=(4,5)
     print("inside the function:",t)
coordinates=(1,2,3)
modify_tuple(coordinates)
print("outside the function", coordinates)

def modify_list(lst):
     lst.append(4)
     lst[0]=99
     print("inside the fucntion:", lst)

numbers = [1,2,3]
modify_list(numbers)
print ("outside the function:" , numbers)

def modify_dict(d):
     d['new_key'] = 'new_value'
     print("inside the fucntion:", d)
     
my_dict ={'key1':'value1', 'key2':'value2'}
modify_dict(my_dict)
print ("outside the function: ", my_dict)