#!/usr/bin/env python
# coding: utf-8

# 
# Question 1: Calculate Euclidean distance
# 
# Write a Python program to calculate Euclidean Distance.
# 
# Example 1:
# 
# Input:
# Given First point values P(x1, y1) : 6 , 7
# Given second point values Q(x2, y2) : 5, 4
# 
# Output:
# The Euclidean Distance between the above given two points 'PQ' = 3.1622776601683795
# 

# In[25]:


import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print(d)


# ----------------------------------------------------------------------------------------------------------------
# Question 2: Reverse User Input for Data Processing
# 
# Imagine you are developing a secure system for user input validation, and part of the system 
# involves reversing strings (such as passwords or IDs) for a unique encryption method.
# 
# Write a Python program that accepts a string from the user and returns it in reverse order. This 
# could simulate part of a process where data is transformed before being stored or transmitted 
# securely.
# 
# Example 1:
# 
# Input:
# 1234abcd
# 
# Output:
# dcba4321
# 
# Explanation:
# Reverse of 1234abcd is dcba4321
# 
# Example 2:
# 
# Input:
# Python@123
# 
# Output:
# 321@nohtyP
# 
# Explanation:
# Reverse of Python@123 is 321@nohtyP

# In[12]:


n =input()
print(n[::-1])


# ----------------------------------------------------------------------------------------------------------------------
# Question 3: Finding indices of Closest Temperatures
#     
# Imagine you work for a weather station, and you have a list of temperatures recorded 
# throughout the day. Your job is to find which two temperatures in the list are the most similar 
# (closest in value). Once you find the two closest temperatures, you need to tell their positions 
# (indices) in the list.
# 
# Note: "Closest", we mean finding two numbers that have the smallest difference between 
# them.
# 
# Example 1:
#     
# Input:
# [1, 7, 9, 2, 10]
# 
# Output:
# [0, 3]
# 
# Explanation:
# The output [0, 3] represents the indices of the closest pair of numbers in the list [1, 7, 9, 2, 10]. 
# The numbers at indices 0 and 3 are 1 and 2, which have the smallest difference (1).
# 
# Example 2:
# 
# Input:
# [5, 8, 12, 15, 7]
# 
# Output:
# [4, 1]
# 
# Explanation:
# The output [4, 1] represents the indices of the closest pair of numbers in the list [5,8,12,15,7]. 
# The numbers at indices 4 and 1 are 7 and 8 which have the smallest difference (1).
# 
# Example 3:
# 
# Input:
# [100, 101, 99, 103, 105]
# 
# Output:
# [0, 1]
# 
# Explanation:
# The output [0, 1] represents the indices of the closest pair of numbers in the list [100, 101, 99, 
# 103, 105]. The numbers at indices 0 and 1 are 100 and 101, which have the smallest difference 
# (1).
# 

# In[52]:


def find_closest_temperatures(temps):
    # Initialize variables to store the smallest difference and the pair of indices
    min_diff = float('inf')
    closest_pair = []

    # Loop through the list to compare each temperature with every other temperature
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            # Calculate the absolute difference between temps[i] and temps[j]
            diff = abs(temps[i] - temps[j])

            # If the current difference is smaller than the smallest difference found so far
            if diff < min_diff:
                min_diff = diff
                closest_pair = [i, j]

    return closest_pair

# Test cases
print(find_closest_temperatures([1, 7, 9, 2, 10]))  # Output: [0, 3]
print(find_closest_temperatures([5, 8, 12, 15, 7]))  # Output: [4, 1]
print(find_closest_temperatures([100, 101, 99, 103, 105]))  # Output: [0, 1]


# --------------------------------------------------------------------------------------------------------------
# Question 4: Strange Sort: Alternating Smallest and Largest
# 
# In an amusement park ticket queue, visitors are sorted in a strange manner. The smallest 
# number (representing the youngest visitor) stands first, followed by the oldest visitor. The next 
# youngest visitor stands next, followed by the next oldest visitor, and so on. Write a Python 
# program to sort a list of numbers in such a “strange sort,” where the first element is the 
# smallest, the second is the largest, the third is the next smallest, and so on.
# 
# Example 1:
# 
# Input:
# [1, 3, 4, 5, 11]
# 
# Output:
# [1, 11, 3, 5, 4]
# 
# Explanation:
# The smallest element is 1, then the largest is 11, followed by the next smallest (3), the next 
# largest (5), and the remaining element (4).
# 
# Example 2:
# 
# Input:
# [7, 2, 10, 4, 8]
# 
# Output:
# [2, 10, 4, 8, 7]
# 
# Explanation:
# The smallest element is 2, then the largest is 10, followed by the next smallest (4), the next 
# largest (8), and the remaining element (7).
# 
# Example 3:
# 
# Input:
# [9, 15, 3, 12, 6, 1]
# 
# Output:
# [1, 15, 3, 12, 6, 9]
# 
# Explanation:
# The smallest element is 1, then the largest is 15, followed by the next smallest (3), the next 
# largest (12), and so on.
# 

# In[36]:


def strange_sort(n):
    n.sort()
    b = []
    i = 0
    j = len(n)-1
    while i <= j:
        if i <= j:
            b.append(n[i])
            i = i+1
        if i <= j:
            b.append(n[j])
            j = j-1        
    print(b)
    
n = [5,2,11,6] #[2,5,6,11]
strange_sort(n)


# ----------------------------------------------------------------------------------------------------------
# Question 5: Check if a String is Pangram
# 
# You are designing a chatbot for an e-commerce platform. The chatbot is expected to understand 
# and respond to user queries efficiently. To ensure that it can handle diverse inputs, you need to 
# verify that its internal processing covers all possible alphabetical characters. A pangram is a 
# sentence that contains every letter of the English alphabet at least once.
# 
# Write a Python function that takes a string as input and checks whether the string is a pangram 
# (contains every letter of the alphabet at least once).
# 
# Example 1:
# 
# Input:
# The quick brown fox jumps over the lazy dog
# 
# Output:
# True
# 
# Explanation:
# This is a famous pangram that contains all the letters of the alphabet.
# 
# Example 2:
# 
# Input:
# Pack my box with five dozen liquor jugs.
# 
# Output:
# True
# 
# Explanation:
# This is a famous pangram that contains all the letters of the alphabet.
# 
# Example 3:
# 
# Input:
# I love programming in Python
# 
# Output:
# False
# 
# Explanation:
# This string is missing several letters, such as ‘z’, ‘j’, and ‘k’, so it is not a pangram.

# In[22]:


def pangram(str_1):
    str_1 = str_1.lower()
    alphabets = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    characters = set()
    for char in str_1:
        if char.isalpha():
            characters.add(char)
    if characters==alphabets:
        return True
    else:
        return False
input_1 ="Pack my box with five dozen liquor jugs."
input_2 = "The quick brown fox jumps over the lazy dog"
input_3 = " I love programming in Python"
print(pangram(input_1))

print(pangram(input_2))

print(pangram(input_3))


# In[ ]:





# In[ ]:




