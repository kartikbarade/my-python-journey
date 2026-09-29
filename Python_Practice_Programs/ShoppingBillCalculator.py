print("SHOPPING BILL CALCULATOR")
print("----------------------------")

num_products = int(input("Enter number of products: "))
total_bill = 0
product_name = []

for i in range(num_products):
    print("\nProduct",i + 1)
    name = input("Enter product name : ")
    price = float(input("Enter product price : "))
    quantity = int(input("Enter quantity :"))

    item_total = price * quantity

    print("Product Name :", name)
    print("Price :",price)
    print("Quantity :",quantity)
    print("Item Total :", item_total)

    total_bill = total_bill + item_total
    product_name.append(name)

    print("--BILL SUMMARY--")
    print("------------------")

    print("Products purchased: ", product_name)
    print("Total Bill :",total_bill)

    if total_bill >= 5000:
        discount = total_bill * 0.20
        print("Discount (20%):",discount)

    elif total_bill >=3000:
        discount = total_bill * 0.10
        print("Discount (10%):",discount)

    elif total_bill >=1000:
        discount = total_bill * 0.05
        print("Discount (5%):", discount)

    else:
        discount = 0
        print("Discount :",discount)

    final_amount = total_bill - discount
    print("-----------------------------")
    print("Final Amount :",final_amount)

