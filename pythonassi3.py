#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Make a calculator using Python with addition , subtraction , multiplication.............

print(" select your desire operation \n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n"
        "5. Power\n") 
select = int(input("Select operations form 1, 2, 3, 4, 5 :")) 
if (select>=1 and select<=5):
    number_1 = int(input("Enter first number: ")) 
    number_2 = int(input("Enter second number: ")) 
    if select == 1:
        add = number_1 + number_2
        print(number_1, "+", number_2, "=", add) 
    elif select == 2: 
        sub = number_1 - number_2
        print(number_1, "-", number_2, "=", sub)
    elif select == 3: 
        mul = number_1 * number_2
        print(number_1, "*", number_2, "=", mul) 
    elif select == 4: 
        div = number_1 / number_2
        print(number_1, "/", number_2, "=", div)
    elif select == 5: 
        power = number_1 ** number_2
        print(number_1, "^", number_2, "=", power)
    else: 
        print("Invalid input")


# In[14]:


llist_val= ['1', '3', 'f', 'a', 'j', '1', 'i', 'g', '4', 'j','c']
mynewlist = [s for s in list_val if s.isdigit()]
print(mynewlist)


# In[9]:


my_data = {
    "First Name" : "Fatima Rais",
    "Father Name" : "Rais ur Rehman",
    "D.O.B" : "12-February-1998",
    "Address" : "Saeed Manzil Saddar Karachi."
}
print(my_data)
my_data["N.I.C"] ='42301-5074243-6'
print(my_data)


# In[10]:


num = {
    "A" : 6,
    "B " : 7,
    "C" : 84,
    "D" : 7
}
print(num)
print(sum(num.values()))


# In[11]:


my_list = [10,30,20,30,40,70,15,11,70,10,50,15,1,20]
dub_val = []
for x in my_list:
    if x not in dub_val:
        dub_val.append(x)
print(dub_val)


# In[12]:


my_data = {
    "First Name" : "Fatima Rais",
    "Father Name" : "Rais ur Rehman",
    "D.O.B" : "12-February-1998",
    "Address" : "Saeed Manzil Saddar Karachi."
}
if 'Address' in my_data.keys():
    print("Key is present and value of the key is:")
    print(my_data['Address'])
else:
      print("Key is not present!")


# In[ ]:




