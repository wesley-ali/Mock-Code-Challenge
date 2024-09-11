class Coffee:
    all_coffees = []  # Track all coffee instances

    def _init_(self, name, price):
        self._name = None  # Initialize to None for validation in setter
        self.price = price
        self.name = name  # Use property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Cannot change coffee name after it is set.")
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = value
        Coffee.all_coffees.append(self)

    @classmethod
    def display_menu(cls):
        menu = "\n".join(f"{coffee.name}: ${coffee.price:.2f}" for coffee in cls.all_coffees)
        return menu or "No coffee available."

    def _repr_(self):
        return f"Coffee(name={self.name!r}, price={self.price:.2f})"