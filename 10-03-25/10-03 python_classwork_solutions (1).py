#!/usr/bin/env python
# coding: utf-8

# Scenario 1: Inventory Management System
# Develop an inventory management system for a small retail store. The system should allow the store to:
# 
# Add new products with their quantities and prices.
# Update stock quantities of existing products.
# Calculate the total value of the inventory.
# Instructions:
# 
# Create a function add_product that adds a new product to the inventory. The inventory should be a dictionary where the keys are product names, and the values are dictionaries containing 'quantity' and 'price' keys.
# Create a function update_stock that updates the stock quantity of an existing product.
# Create a function calculate_inventory_value that calculates and prints the total value of the inventory.
# Sample Test Case 1:
# 
# inventory = {}
# add_product(inventory, 'apple', 50, 0.5)
# add_product(inventory, 'banana', 100, 0.2)
# update_stock(inventory, 'apple', 25)
# calculate_inventory_value(inventory)
# Expected Output:
# 
# Total inventory value: $57.50
# 
# Sample Test Case 2:
# 
#  Initialize an empty inventory
# inventory = {}
# 
#  Add new products to the inventory
# add_product(inventory, 'milk', 30, 1.5)
# add_product(inventory, 'bread', 20, 2.0)
# add_product(inventory, 'eggs', 50, 0.1)
# 
#  Update stock quantities
# update_stock(inventory, 'milk', 10)   # Adding 10 more units of milk
# update_stock(inventory, 'eggs', -5)   # Selling 5 units of eggs
# 
#  Calculate the total value of the inventory
# calculate_inventory_value(inventory)
# Expected Output:
# 
# Total inventory value: $104.50
# 
# Explanation:
# 
# Milk: Initially, there are 30 units priced at 1.50 each. Adding 10 more units results in 40 units. The total value for milk is 40 x 1.50 = 60.00.
# 
# Bread: There are 20 units priced at 2.00 each. The total value for bread is 20 x 2.00 = 40.00.
# 
# Eggs: Initially, there are 50 units priced at $0.10 each. Selling 5 units reduces the quantity to 45 units. The total value for eggs is 45 x 0.10 = 4.50. Summing these values gives the total inventory value: 60.00 + 40.00 + 4.50 = 104.50.
# 
# 

# In[45]:


def add_product(inventory, product_name, quantity, price):
    if product_name in inventory:
        print(f"{product_name} already exists")
    inventory[product_name] = {'quantity': quantity, 'price': price}
    
def update_stock(inventory, product_name, quantity_change):
    inventory[product_name]['quantity'] += quantity_change
    
def calculate_inventory_value(inventory):
        total_value = sum(item['quantity'] * item['price'] for item in inventory.values())
        print(f"Total inventory value: ${total_value}")
inventory = {}
add_product(inventory, 'apple', 50, 0.5)
add_product(inventory, 'banana', 100, 0.2)
update_stock(inventory, 'apple', 25)
calculate_inventory_value(inventory)


# -------------------------------------------------------------------------------------------------------------------
# Scenario 2: Student Grades Analysis
# 
# Develop a system to manage and analyze student grades. The system should allow:
# Adding student names with their corresponding grades.
# Calculating the average grade of the class.
# Determining the highest and lowest grades.
# 
# Instructions:
# Create a function add_student that adds a student's name and grade to a dictionary.
# Create a function calculate_average_grade that calculates and prints the average grade of all students.
# Create a function find_highest_and_lowest_grade that finds and prints the highest and lowest grades among students.
# 
# Sample Test Case 1
# 
# Input:
# grades = {}
# 
# add_student(grades, 'Alice', 85)
# 
# add_student(grades, 'Bob', 92)
# 
# add_student(grades, 'Charlie', 78)
# 
# calculate_average_grade(grades)
# 
# find_highest_and_lowest_grade(grades)
# 
# Expected Output:
# Average grade: 85.00  
# Highest grade: 92  
# Lowest grade: 78  
# 
# Explanation:
# Three students are added with grades: Alice (85), Bob (92), and Charlie (78).
# The average grade is calculated as (85 + 92 + 78) / 3 = 85.00.
# The highest grade is 92 (Bob), and the lowest grade is 78 (Charlie).
# 
# Sample Test Case 2
# 
# Input:
# grades = {}
# 
# add_student(grades, 'David', 88)
# 
# add_student(grades, 'Eva', 95)
# 
# add_student(grades, 'Frank', 67)
# 
# calculate_average_grade(grades)
# 
# find_highest_and_lowest_grade(grades)
# 
# Expected Output:
# Average grade: 83.33  
# Highest grade: 95  
# Lowest grade: 67  
# 
# Explanation:
# Three students are added with grades: David (88), Eva (95), and Frank (67).
# The average grade is calculated as (88 + 95 + 67) / 3 = 83.33.
# The highest grade is 95 (Eva), and the lowest grade is 67 (Frank).

# In[32]:


def add_student(grades, student_name, grade):
        grades[student_name] = grade
        
def calculate_average_grade(grades):
    total_grade = sum(grades.values())
    average_grade = total_grade / len(grades)
    print("Average Grade: ",f"{average_grade:.2f}")
    
def find_highest_and_lowest_grade(grades):
    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())
    print("Highest Grade: ", highest_grade )
    print("Lowest Grade: ", lowest_grade )
    
grades= {}
add_student(grades, 'Alice', 85)
add_student(grades, 'Bob', 92)
add_student(grades, 'Charlie', 78)
calculate_average_grade(grades)
find_highest_and_lowest_grade(grades)


# ------------------------------------------------------------------------------------------------------
# Scenario 3: Library Book Catalog
#     
# Create a system to manage a library's book catalog. The system should allow:
# Adding new books with their titles, authors, and publication years.
# Retrieving all books written by a specific author.
# 
# Instructions:
# Create a function add_book that adds a new book to the catalog. The catalog should be a list of dictionaries, each containing 'title', 'author', and 'year'.
# Create a function find_books_by_author that returns all books written by a specific author.
# 
# Sample Test Case 1:
#     
# catalog = []
# 
# add_book(catalog, 'To Kill a Mockingbird', 'Harper Lee', 1960)
# 
# add_book(catalog, '1984', 'George Orwell', 1949)
# 
# add_book(catalog, 'Animal Farm', 'George Orwell', 1945)
# 
# find_books_by_author(catalog, 'George Orwell')
# 
# Expected Output:
# Books by George Orwell:
# - 1984 (1949)
# - Animal Farm (1945)
# 
# Explanation:
# The function add_book stores the books in a list.
# The function find_books_by_author searches for books by "George Orwell" and returns the matching results.
# 
# Sample Test Case 2:
#     
# catalog = []
# 
# add_book(catalog, 'Pride and Prejudice', 'Jane Austen', 1813)
# 
# add_book(catalog, 'Sense and Sensibility', 'Jane Austen', 1811)
# 
# add_book(catalog, 'Moby-Dick', 'Herman Melville', 1851)
# 
# find_books_by_author(catalog, 'Jane Austen')
# 
# Expected Output:
# Books by Jane Austen:
# - Pride and Prejudice (1813)
# - Sense and Sensibility (1811)
# 
# Explanation:
# The function find_books_by_author filters books by "Jane Austen" and lists her books along with their publication years.

# In[80]:


def add_book(catalog, title, author, year):
    book = {'title':title,'author':author,'year':year}
    catalog.append(book)
def find_books_by_author(catalog, author):
    books_by_author = [book for book in catalog if book['author'] == author]
    if books_by_author:
        print(f"Books by {author}: ")
        for book in books_by_author:
            print(f"- {book['title']}  ({book['year']})")
   
        


# In[81]:


catalog = []
add_book(catalog, 'Pride and Prejudice', 'Jane Austen', 1813)
add_book(catalog, 'Sense and Sensibility', 'Jane Austen', 1811)
add_book(catalog, 'Moby-Dick', 'Herman Melville', 1851)
find_books_by_author(catalog, 'Jane Austen')


# ------------------------------------------------------------------------------------------------------------
# Scenario 4: Employee Record System
# 
# Develop an employee record system for a company. The system should allow:
# Adding new employees with their names, departments, and salaries.
# Finding employees who belong to a specific department.
# Calculating the average salary of all employees.
# 
# Instructions:
# 
# Create a function add_employee that adds an employee to the record. The record should be a list of dictionaries, where each dictionary contains 'name', 'department', and 'salary'.
# Create a function find_employees_by_department that retrieves all employees belonging to a given department.
# Create a function calculate_average_salary that calculates and prints the average salary of all employees.
# 
# Sample Test Case 1:
# 
# employees = []
# 
# add_employee(employees, 'Alice', 'HR', 60000)
# 
# add_employee(employees, 'Bob', 'IT', 75000)
# 
# add_employee(employees, 'Charlie', 'IT', 80000)
# 
# find_employees_by_department(employees, 'IT')
# 
# calculate_average_salary(employees)
# 
# Expected Output:
# 
# Employees in IT:
# - Bob (Salary: $75000
# 
# - Charlie (Salary: $80000)
# 
# Average salary: $71666.67
# 
# Explanation:
# The function find_employees_by_department retrieves all employees in the IT department.
# The function calculate_average_salary computes the mean salary of all employees.
# 
# Sample Test Case 2:
# 
# employees = []
# 
# add_employee(employees, 'David', 'Finance', 85000)
# 
# add_employee(employees, 'Emma', 'Finance', 90000)
# 
# add_employee(employees, 'Frank', 'Marketing', 65000)
# 
# find_employees_by_department(employees, 'Finance')
# 
# calculate_average_salary(employees)
# 
# Expected Output:
# 
# Employees in Finance:
# - David (Salary: $85000)
# 
# - Emma (Salary: $90000)
# 
# Average salary: $80000.00
# 
# Explanation:
# 
# The function find_employees_by_department retrieves employees working in the Finance department.
# The function calculate_average_salary finds the average of all employees' salaries

# In[38]:


def add_employee(employees, name, department, salary):
    if isinstance(salary, (int,float)) and salary>0:
        employee = {'name':name,'department':department,'salary':salary}
        employees.append(employee)
    else:
        print("Salary must be positive number")
def find_employees_by_department(employees, department):
    employees_by_department = [employee for employee in employees if employee['department'] == department]
    if employees_by_department:
        print(f"Employees in {department}: ")
        for employee in employees_by_department:
            print(f"- {employee['name']}  (Salary: ${employee['salary']})")
    else:
        print(f"No employees found in the {department} department.")
            
def calculate_average_salary(employees):
    if len(employees)==0:
        print("No employees in the employees book")
    else:
        total_salary = sum(employee['salary'] for employee in employees)
        no_of_employees = len(employees)
        average_salary = total_salary / no_of_employees
        print("Average Salary : ", f"${average_salary:.2f}")
        


# In[39]:


employees = []
add_employee(employees, 'Alice', 'HR', 60000)
add_employee(employees, 'Bob', 'IT', 75000)
add_employee(employees, 'Charlie', 'IT', 80000)
find_employees_by_department(employees, 'IT')
calculate_average_salary(employees)


# ------------------------------------------------------------------------------------------------------------
# Scenario 5: Online Shopping Cart
# 
# Develop an online shopping cart system that allows customers to:
# Add items to their cart with their prices and quantities.
# Remove items from the cart.
# Calculate the total cost of the cart.
# 
# Instructions:
# 
# Create a function add_to_cart that adds an item to the shopping cart. The cart should be a dictionary where keys are item names and values are dictionaries containing 'quantity' and 'price'.
# Create a function remove_from_cart that removes an item from the cart.
# Create a function calculate_total_cost that calculates and prints the total cost of all items in the cart.
# 
# Sample Test Case 1:
# 
# cart = {}
# 
# add_to_cart(cart, 'Laptop', 1, 1200)
# 
# add_to_cart(cart, 'Headphones', 2, 150)
# 
# calculate_total_cost(cart)
# 
# remove_from_cart(cart, 'Headphones')
# 
# calculate_total_cost(cart)
# 
# Expected Output:
# 
# Total cost: $1500.00
# 
# Item 'Headphones' removed.
# 
# Total cost: $1200.00
# 
# Explanation:
# 
# The function calculate_total_cost sums up the total value of items in the cart.
# The function remove_from_cart removes 'Headphones' and recalculates the total cost.
# 
# Sample Test Case 2:
# 
# cart = {}
# 
# add_to_cart(cart, 'Phone', 1, 800)
# 
# add_to_cart(cart, 'Charger', 1, 50)
# 
# add_to_cart(cart, 'Tablet', 2, 500)
# 
# calculate_total_cost(cart)
# 
# remove_from_cart(cart, 'Charger')
# 
# calculate_total_cost(cart)
# 
# Expected Output:
# 
# Total cost: $1850.00
# 
# Item 'Charger' removed.
# 
# Total cost: $1800.00
# 
# Explanation:
# 
# The function calculate_total_cost initially calculates the total cost of all items.
# After removing the 'Charger', the function updates the total cost.

# In[89]:


def add_to_cart(cart, item, quantity, price):
    if item in cart:
        cart[item]['quantity'] += quantity
        print(f"{item} already exists and its updated ")
    else:
        cart[item] = {'quantity': quantity, 'price': price}
        
def remove_from_cart(cart, item):
    if item in cart:
        del cart[item]
        print(f"Item {item} removed")
    else:
        print(f"{item} doesn't exists")
        
def calculate_total_cost(cart):
    total_cost = 0
    for item, details in cart.items():
        total_cost += details['quantity'] * details['price']
    print(f"Total cost: ${total_cost}")
        


# In[90]:


cart = {}
add_to_cart(cart, 'Laptop', 1, 1200)
add_to_cart(cart, 'Headphones', 2, 150)
calculate_total_cost(cart)
remove_from_cart(cart, 'Headphones')
calculate_total_cost(cart)


# In[ ]:





# In[ ]:




