class DMXItem:
    def __init__(self, name, price, url, discount, regular_price):
        self.name = name
        self.price = price
        self.url = url
        self.discount = discount
        self.regular_price = regular_price

    def get_info(self):
        return f"{self.name} | {self.price} | {self.url} | {self.discount} | {self.regular_price}"
