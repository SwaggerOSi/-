class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        # Получаем текущие продукты из файла
        existing_products = self.get_products().splitlines()
        product_names = {line.split(", ")[0] for line in existing_products}
        product_weight = {line.split(", ")[1] for line in existing_products}
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in product_names and str(product.weight) in product_weight:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')
                    product_names.add(product.name)


# Пример использования:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод через __str__

s1.add(p1, p2, p3)

print(s1.get_products())