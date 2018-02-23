def foo():
    print("foo!")


class InjectionMold:
    def __init__(self, customer, partNumber, cavities):
        self.customer = customer
        self.cavities = cavities
        self.partNumber = partNumber
        self.partWidth = partWidth
        self.partHeight = partHeight
        self.numberSlides = numberSlides
        self.numberLifters = numberLifters
        self.coreComplexity = coreComplexity
        self.cavComplexity = cavComplexity
        self.slideComplexity = slideComplexity
        self.lifterComplexity = lifterComplexity

    def moldWidth(self):
        return partWidth
