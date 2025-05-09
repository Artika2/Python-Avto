from smartphone import Smartphone

# Создаем каталог с пятью разными экземплярами класса Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("OnePlus", "11", "+79567890123")
]

# Печатаем каталог в заданном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")