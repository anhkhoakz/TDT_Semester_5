class UtilityListPHMN:
    def __init__(self, item):
        """
        Constructor.
        :param item: the item that is used for this utility list
        """
        self.item = item  # the item
        self.sumIutils = 0  # the sum of item utilities
        self.sumRutils = 0  # the sum of remaining utilities
        self.elements = []  # the elements
        self.largestPeriodicity = 0
        self.smallestPeriodicity = float('inf')

    def getLargestPeriodicity(self):
        """
        Get the periodicity of this pattern.
        :return: the periodicity
        """
        return self.largestPeriodicity

    def addElement(self, element):
        """
        Add an element to this utility list.
        :param element: the element to add
        """
        self.elements.append(element)
        self.sumIutils += element.iutils
        self.sumRutils += element.rutils

    def getSupport(self):
        """
        Get the support of this utility list.
        :return: the support
        """
        return len(self.elements)