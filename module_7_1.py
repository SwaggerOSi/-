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
        """Считывает всю информацию из файла и возвращает её как единую строку."""
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        """Добавляет новые продукты в файл, если их ещё нет."""
        existing_products = set()

        
        for line in self.get_products().splitlines():
            product_name = line.split(',')[0].strip()
            existing_products.add(product_name)


        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')
                    existing_products.add(product.name)


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)
    print(s1.get_products())