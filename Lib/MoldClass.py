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

    def moldWidth(self, runnerSteel = 4, moldSteel = 4, slideSteel = 6):
        return ((partWidth*(cavities/2))+runnerSteel+moldSteel+slideSteel)

    def moldHeight(self, runnerSteel = 4, moldSteel = 4, slideSteel = 6, spacingSteel = 2):
        return ((partHeight*(cavities-(cavities/2)))+runnerSteel+moldSteel+slideSteel+(spacingSteel*((cavities-(cavities/2))-1)))
