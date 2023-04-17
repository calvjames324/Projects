#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
read_file = pd.read_excel (r'F:\Physics project.xlsx')
read_file.to_csv (r'F:\Project\New Physics project.csv', index = None, header=True)


# In[2]:


data = pd.read_csv("Physics_project.csv")
plt.scatter(data.time, data.temperature)
plt.xlabel("Time(min)")
plt.ylabel("100 mL Temperature °C")
plt.show()
print(data)


# In[3]:


def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].time
        y = points.iloc[i].temperature
        total_error += (y -(m * x + b)) ** 2
    total_error / float(len(points))


# In[4]:


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x = points.iloc[i].time
        y = points.iloc[i].temperature
        
        m_gradient += -(2/n) * x * (y - (m_now*x + b_now))
        b_gradient += -(2/n) * (y - (m_now*x + b_now)) 
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    
    return m, b
        


# In[ ]:


m = 0
b = 0
L = 0.001
epochs = int(input("Enter the number of iterations you want to perform: "))
for i in range(epochs):
    if i % 500 == 0:
        print(f"Epoch:{i}")
    m, b = gradient_descent(m, b, data, L)
    
print(m, b)


# In[51]:


plt.scatter(data.time, data.temperature, color = "black")
plt.xlabel("Time(min)")
plt.ylabel("100 mL Temperature °C")
plt.plot(list(range(0, 60)), [m * x + b for x in range(0, 60)])


# In[ ]:




