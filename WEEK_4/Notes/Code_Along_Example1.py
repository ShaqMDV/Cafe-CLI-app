def price_updater(prices: list[1.2,3.4,9.2], increase_rate: 0.5) -> list[float] | str:
    # Check if increase rate is within valid range
    if not (0 <= increase_rate <= 1):
        return "Invalid Increase Rate!"

    # Initialize a list to store the updated prices
    updated_prices = []
    
    for price in prices:
        # Check if each price is a float and within the valid range
        if not isinstance(price, float) or not (0 <= price <= 100000):
            return "Incorrect Price Detected!"
        
        # Calculate the updated price and add it to the list
        updated_prices.append(price * (1 + increase_rate))
    
    return updated_prices
print(price_updater)