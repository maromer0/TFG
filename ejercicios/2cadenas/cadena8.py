price = input("price: ")
print(f"{price[:price.find('.')]} euros and {price[price.find('.') + 1:]} cents")