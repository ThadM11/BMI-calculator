#!/usr/bin/env python
# coding: utf-8

# In[ ]:


prompt_for_name = "What is your name? "
name = input(prompt_for_name)

prompt_for_weight = "What is your weight in kg? "
weight = input(prompt_for_weight)

prompt_for_height = "What is your height in meters? "
height = input(prompt_for_height)

BMI = float(weight) / float(height)**2

print("Your BMI is", BMI)

if BMI < 18:
    print(name + " is underweight")
elif 18 < BMI < 25:
    print(name + "is healthy")
else:
    print(name + "is overweight")


