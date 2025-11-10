# write a code for slicing without using [:]
def manual_slicing(number,start,end):
    result =[]
    for i in range(start,end):
        result.append(number[i])
    return result;   # ✅ manual slicing logic

number = [10,20,30,40,50,None,10]
print(manual_slicing(number,2,5)) 
# ✅ Output: [30, 40, 50]

set_1 = {10,20,30,40,50,None,10}

# slicing using [:] for comparison
print(number[2:5])
# ✅ Output: [30, 40, 50]

# check duplicates and null ?
print(number)
# ✅ Output: [10, 20, 30, 40, 50, None, 10]
print(set_1)
# ✅ Output (order may vary): {None, 40, 10, 50, 20, 30}
# ✅ list accepts duplicates, set removes duplicates; both accept None

# discard Vs remove
number.remove(20)        # ✅ removes 20 from list
#number.discard(70)      # ❌ list object has no attribute 'discard'
set_1.remove(20)         # ✅ removes 20 from set
set_1.discard(70)        # ✅ safe, no error even if 70 not present
# set_1.remove(70)       # ❌ would raise KeyError if uncommented

print(number)
# ✅ Output: [10, 30, 40, 50, None, 10]
print(set_1)
# ✅ Output (order may vary): {None, 40, 10, 50, 30}

# set operations
list1=[1,2,3]
list2=[4,5,6]
print(set(list1)|set(list2))
# ✅ Union Output: {1, 2, 3, 4, 5, 6}
print(set(list1)&set(list2))
# ✅ Intersection Output: set()
print(set(list1)-set(list2))
# ✅ Difference Output: {1, 2, 3}

# join() for strings
words =['Hi!','my','name','is','Sri Kartik']
result= ' '.join(words)
print(result)
# ✅ Output: Hi! my name is Sri Kartik

# Tuple examples
tuple1=(1,2,3,"temp","temp","temp")
tuple2=(1,)   # ✅ single element tuple (comma needed)
tuple3=(1)    # ⚠️ not a tuple, just an integer

print(type(tuple1))  # ✅ Output: <class 'tuple'>
print(type(tuple2))  # ✅ Output: <class 'tuple'>
print(type(tuple3))  # ⚠️ Output: <class 'int'>

print(tuple1.count("temp"))
# ✅ Output: 3

# write a program to count elements manually in tuple
tuple4 =(1,"temp",2,"temp",3,"temp")
count =0
for i in tuple4 :
    if i =="temp":
        count+=1
print(count)      
# ✅ Output: 3

# tuple unpacking : assigning tuple values to variables at once
tuple5=("sri_kartik",21,"CSE")
name,age,branch = tuple5
print(name)    # ✅ Output: sri_kartik
print(age)     # ✅ Output: 21
print(branch)  # ✅ Output: CSE
