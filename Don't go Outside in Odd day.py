#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_numbers = 0
count_even_numbers = 0
for i in numbers:
    if not i % 2:
        count_even_numbers += 1
    else:
        count_odd_numbers += 1
print ("Number of even numbers :",count_even_numbers)
print ("Number of odd numbers :",count_odd_numbers)


# In[ ]:




