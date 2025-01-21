"""Sum of Prices:

Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop."""

products = {
    "pencile":10,
    "Earaser":5,
"scale":5
} 
total=0
for products, price in products.items():
    total = total + price

print("Total Price of Products:",total)

#2
dict = {"book":10, "pen":20, "pencil":15, "notebook":50, "ruler":15}
total=0
for dict, price in dict.items():
    total = total + price
print("Total Price of Products:",total)



