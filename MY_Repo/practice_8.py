name = "Tholapi Sri kartik"
roll_no =123456789
height = 5.10

print ("hello!! my name is {} my roll no is {}, my height is {}".format(name,roll_no,height))
print ("hello!! my name is {0} my roll no is {1}, my height is {2}".format(name,roll_no,height))
print ("hello!! my name is {n} my roll no is {m}, my height is {o}".format(n=name,m=roll_no,o=height))
print ("hello!! my name is {n} my roll no is {m}, my height is {o:.2f}".format(n=name,m=roll_no,o=height))
print ("hello!! my name is {0} my roll no is {1:.1f}, my height is {2}".format(name,roll_no,height))
print ("hello!! my name is {n} my roll no is {m:,.1f}, my height is {o:.2f}".format(n=name,m=roll_no,o=height))
print ("hello!! my name is {n} my roll no is {m:+.1f}, my height is {o:.2f}".format(n=name,m=roll_no,o=height))


# how do we reverse a string 
string = "madam"
print(string[::-1])

print(string == string[::-1])

vowels = "aeiouAEIOU"
string1="srikartik"
print(sum(1 for char in string1 if char in vowels))
 # join keyword 
list1 = ["apple","banana","orange"]
print(" and ".join(list1))

# len function 
print(len(string))