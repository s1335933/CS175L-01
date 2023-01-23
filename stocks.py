#Aidan Moxham
#Profesor Eckert
#CS-175L-01
#January 23rd, 2023

    #Stocks Program

# Initialize variables
stock_purchase_price = float(input("Amount paid for the stock: "))
purchase_commission = float(input("Commission paid on the purchase: "))
stock_sale_price = float(input("Amount the stock sold for: "))
sale_commission = float(input("Commission paid on the sale: "))


# Calculate profit and net amount sold for
profit = stock_sale_price - stock_purchase_price - purchase_commission - sale_commission
net_amount_sold_for = stock_sale_price - purchase_commission - sale_commission

# Print results
print("Amount paid for the stock: ", stock_purchase_price)
print("Commission paid on the purchase: ", purchase_commission)
print("Amount the stock sold for: ", stock_sale_price)
print("Commission paid on the sale: ", sale_commission)
print("Profit (or loss): ", profit)
