# Write a function calculate_total that takes any number
# of item prices and an optional discount percentage (default to 0).
# Return the total cost after applying the discount.

def calculate_total(*args, discount=0):
    total = sum(args)
    discounted_total = total - discount
    return discounted_total


print(calculate_total(10, 10, 20, 30, discount=50))
