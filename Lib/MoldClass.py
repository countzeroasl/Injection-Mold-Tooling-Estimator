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

    def moldWidth(self, runnerSteel = 4, moldSteel = 4, slideSteel = 0):

        """Returns the moldWidth in inches from the part height, steel needed for the runner system, outside mold support steel, and the steel for slides."""
        
        return ((partWidth*(cavities/2))+runnerSteel+moldSteel+slideSteel)

    def moldHeight(self, moldSteel = 4, spacingSteel = 2, slideSteel = 0):

        """Returns the moldHeight in inches from the part height, outside mold support steel, the steel in between cavities, and the steel for slides"""

        return ((partHeight*(cavities-(cavities/2)))+runnerSteel+moldSteel+slideSteel+(spacingSteel*((cavities-(cavities/2))-1)))
