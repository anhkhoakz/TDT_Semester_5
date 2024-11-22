class ElementPHMN:
    """
    This class represents an element with transaction id, itemset utility, and remaining utility.
    """

    def __init__(self, tid, iutils, rutils):
        """
        Constructor.
        :param tid: the transaction id
        :param iutils: the itemset utility
        :param rutils: the remaining utility
        """
        self.tid = tid
        self.iutils = iutils
        self.rutils = rutils