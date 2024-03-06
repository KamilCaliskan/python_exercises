from collections import Counter

def calculate_earned_money(shoe_count, shoe_sizes, customer_count, customer_data):
    available_shoes = Counter(shoe_sizes)
    total_earned_money = 0
    
    for i in range(customer_count):
        size, price = customer_data[i]
        if available_shoes[size] > 0:
            total_earned_money += price
            available_shoes[size] -= 1
    
    return total_earned_money

# Reading input
shoe_count = int(input())
shoe_sizes = list(map(int, input().split()))
customer_count = int(input())
customer_data = [tuple(map(int, input().split())) for _ in range(customer_count)]

# Calculate and print the earned money
earned_money = calculate_earned_money(shoe_count, shoe_sizes, customer_count, customer_data)
print(earned_money)
