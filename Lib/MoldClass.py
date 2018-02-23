def foo():
    print("foo!")


class InjectionMold:
    def __init__(self, customer, partNumber, cavities):
        self.customer = customer
        self.cavities = cavities
        self.partNumber = partNumber
