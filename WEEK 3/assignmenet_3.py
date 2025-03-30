def calculate_discount(price, discount_percent):
    """calculates the final price after applying a discount"""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price


# get the price and discount percentage from the user
price = float(input("Enter the price of the item:"))
discount_percent = float(input("Enter the discount percentage: "))

# calculate the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# The code calculates the final price of an item after applying a discount
print(f"The final price after applying the discount is: {final_price:.2f}")
