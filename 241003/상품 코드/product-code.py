class Product:
    def __init__ (self, name="codetree", code="50"):
        self.name = name
        self.code = code


pro1 = Product()

name, code = tuple(map(str, input().split()))
pro2 = Product(name, code)

print(f'product {pro1.code} is {pro1.name}')
print(f'product {pro2.code} is {pro2.name}')