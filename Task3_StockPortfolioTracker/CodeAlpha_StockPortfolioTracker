import csv


print("welcome to stock portfolio tracker")
total_investment=0
portfolio=[]
stocks={
    "AAPL":180,
    "TSLA":250,
    "GOOG":140,
    "MSFT":320,
    "AMZN":135,
    "NFLX":420,
    "META":300,
    "VNDA":450
}
while True:
 stock_name=input("Enter Stock Name(or type 'stop'): ").upper()

 if stock_name=="STOP":
     break
 
 if stock_name not in stocks:
    print("Stock not found")
    continue
 
 quantity=int(input("Enter Quantity: "))

 price=stocks[stock_name]
 total_price=price*quantity

 total_investment+=total_price
 print(f"Total price for {quantity} shares of {stock_name} at ${price} each = ${total_price}")
 portfolio.append((stock_name, quantity, price, total_price))
print(f"Total Investment: ${total_investment}")


file=open("portfolio.csv","w",newline="")
writer=csv.writer(file)

writer.writerow(["Stock Name","Quantity","Price per Share","Total Price"])

writer.writerows(portfolio)

writer.writerow(["Total Investment", total_investment])

file.close()
