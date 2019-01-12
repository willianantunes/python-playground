def apply_discount(product, discount):
    price = int(product['price']) * (1.0 - discount)
    assert 0 <= price <= product['price'], "iago parrot"
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes, 0.25))

# Assert is mainly used to speed up debugging efforts if you have an error
print(apply_discount(shoes, 2.0))
