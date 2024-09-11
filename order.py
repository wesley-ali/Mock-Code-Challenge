class Order:
    all_orders = []  # Track all order instances

    def _init_(self, customer, coffee, price):
        from customer import Customer  # Local import to avoid circular dependency
        from coffee import Coffee  # Local import to avoid circular dependency

        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)  # Add the order to the class attribute list

    @property
    def price(self):
        return self._price

    def _repr_(self):
        return (f"Order(customer={self._customer.name!r}, coffee={self._coffee.name!r}, "
                f"price={self.price:.2f})")