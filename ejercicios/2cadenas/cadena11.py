product = input("product name: ")
price = float(input("product price: "))
quantity = int(input("product quantity: "))
print("{product}: {quantity:3d} x {price:9.2f} = {total:11.2f}".format(product = product, price = price, quantity = quantity, total = price * quantity))