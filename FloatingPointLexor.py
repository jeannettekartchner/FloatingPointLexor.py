#!/usr/bin/env python
# coding: utf-8

# Let's take this state transition table and create a lexor
# ![image.png](attachment:image.png)

# In[10]:


import re

state_transition = {    'SAB': {'+':'AB', '-':'AB','.':'C', 'digit':'B'},
     'AB': {'+':'dead', '-':'dead','.':'C', 'digit':'B'},
     'B': {'+':'dead', '-':'dead','.':'C', 'digit':'B'},
     'C': {'+':'dead', '-':'dead','.':'dead', 'digit':'D'},
     'D': {'+':'dead', '-':'dead','.':'dead', 'digit':'D'},
     'dead': {'+':'dead', '-':'dead','.':'dead', 'digit':'dead'}
}

#instead of listing every digit as input into the table, check if it is a digit
digits = ['0','1','2','3','4','5','6','7','8','9']
#could have put +|- together, but there were only 2, so listed separately

state_message = {   'SAB': 'Rejected!',
     'AB': 'Rejected!',
     'B': 'Rejected!',
     'C': 'Rejected!',
     'D': 'Accepted!',
     'dead': 'Rejected!'
}

accept_state = 'D'
current_state = 'SAB'

input_string = '.2456'

for x in input_string:
    if x in digits:
        #if is is a digit give it the transition name of 'digit'
        transition = 'digit'
    else:
        transition = x
    current_state = state_transition[current_state][transition]
    
print(input_string + " is " + state_message[current_state])


# In[ ]:




