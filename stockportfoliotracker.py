import csv

# Hardcoded dictionary of available stock prices (USD)
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "AMZN": 175.0,
    "MSFT": 420.0
}

portfolio = []

print("=== Stock Portfolio Tracker ===")
print("Available stocks and prices:")
for symbol, price in STOCK_PRICES.items():
    print(f"  • {symbol}: ${price:.2f}")
print("===============================\n")

# Data entry loop
while True:
    symbol = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
    
    if symbol == "DONE":
        break
        
    if symbol not in STOCK_PRICES:
        print(f"'{symbol}' is not in the price list. Available: {', '.join(STOCK_PRICES.keys())}\n")
        continue

    # Input validation for quantity
    try:
        quantity = int(input(f"Enter quantity of {symbol}: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue
    except ValueError:
        print("Invalid input. Please enter an integer quantity.\n")
        continue

    price_per_share = STOCK_PRICES[symbol]
    total_val = quantity * price_per_share
    
    portfolio.append({
        "symbol": symbol,
        "quantity": quantity,
        "price": price_per_share,
        "total": total_val
    })
    print(f"Added {quantity} shares of {symbol} (${total_val:.2f})\n")

# Display portfolio summary
if not portfolio:
    print("\nNo stocks entered. Exiting program.")
else:
    grand_total = sum(item["total"] for item in portfolio)
    
    print("\n" + "=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<12}{'Total':<12}")
    print("-" * 45)
    for item in portfolio:
        print(f"{item['symbol']:<8}{item['quantity']:<8}${item['price']:<11.2f}${item['total']:<11.2f}")
    print("-" * 45)
    print(f"Total Portfolio Value: ${grand_total:.2f}")
    print("=" * 45)

    # Optional file export
    save_choice = input("\nSave results to file? (txt / csv / no): ").strip().lower()

    if save_choice == "txt":
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 40 + "\n")
            for item in portfolio:
                f.write(f"{item['symbol']}: {item['quantity']} shares @ ${item['price']:.2f} = ${item['total']:.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total Portfolio Value: ${grand_total:.2f}\n")
        print("Saved successfully to 'portfolio_summary.txt'.")

    elif save_choice == "csv":
        with open("portfolio_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price Per Share", "Total Value"])
            for item in portfolio:
                writer.writerow([item["symbol"], item["quantity"], item["price"], item["total"]])
            writer.writerow([])
            writer.writerow(["Grand Total", "", "", grand_total])
        print("Saved successfully to 'portfolio_summary.csv'.")

    else:
        print("Results not saved to file.")