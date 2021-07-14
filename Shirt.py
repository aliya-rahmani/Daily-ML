# Use the Shirt Class

You've seen what a class looks like and how to instantiate an object. Now it's your turn to write code that insantiates a shirt object.

# Explanation of the Code
This exercise using Jupyter notebook includes three files:
- shirt_exercise.ipynb, which is the file you are currently looking at
- answer.py containing answers to the exercise
- tests.py, tests for checking your code - you can run these tests using the last code cell at the bottom of this notebook

# Your Task
The shirt_exercise.ipynb file, which you are currently looking at if you are reading this, has an exercise to help guide you through coding with an object in Python.

Fill out the TODOs in each section of the Jupyter notebook. You can find a solution in the answer.py file.

First, run this code cell below to load the Shirt class.

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)
      ### TODO:
#    - insantiate a shirt object with the following characteristics:
#        - color red, size S, style long-sleeve, and price 25
#    - store the object in a variable called shirt_one
#
#
###
    shirt_one= Shirt('red','S','long-sleeve',25)
    print(shirt_one.size)
    ### TODO:
#     - print the price of the shirt using the price attribute
#     - use the change_price method to change the price of the shirt to 10
#     - print the price of the shirt using the price attribute
#     - use the discount method to print the price of the shirt with a 12% discount
#
###
    print(shirt_one.price)
    shirt_one.change_price(10)
    shirt_one.discount(.12)
    ### TODO:
#
#    - instantiate another object with the following characteristics:
# .       - color orange, size L, style short-sleeve, and price 10
#    - store the object in a variable called shirt_two
#
###
    shirt_two= Shirt('orange','L','short-sleeve',10)
    total = shirt_one.price + shirt_two.price
    ### TODO:
#
#    - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
#    - store the results in a variable called total_discount
###
    total_discount=shirt_one.discount(.14) + shirt_two.discount(.06)
    print(total_discount)
    
