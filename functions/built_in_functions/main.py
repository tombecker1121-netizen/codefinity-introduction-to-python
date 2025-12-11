# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
total_sum = 0
for items in products:
    price, quantity_sold = products[items]
    price = float(price)
    quantity_sold = int(quantity_sold)
    total_sales = price * quantity_sold
    total_sales_list.append(total_sales)
    print(f"Total sales for {items}: $", total_sales)
    total_sum = sum(total_sales_list)
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
print(f"Total sum of all sales: $",total_sum)
print(f"Minimum sales: $", min_sales)
print(f"Maximum sales: $", max_sales)
    
    