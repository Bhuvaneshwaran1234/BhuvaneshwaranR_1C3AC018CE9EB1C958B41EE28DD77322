def linearSearchProduct(productList, targetProduct):
    indices = []

    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)

    return indices

#Example usage:
products = ["bhuvan", "Bala", "magizhan", "sureshbabu", "Magizhan", "bala", "bhuvan", "Supra", "Bugatti"]
target = "Bugatti"
result = linearSearchProduct(products, target)
print(result)
