stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 135, "AMZN": 125}
portfolio = {}

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Stock not found in the price list.")

total_investment = 0
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print(f"\nTotal investment value: ${total_investment}")

save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
        f.write(f"Total Investment, , ,{total_investment}")
