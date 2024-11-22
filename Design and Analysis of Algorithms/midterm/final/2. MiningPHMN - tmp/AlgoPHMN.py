import time
from collections import defaultdict


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


class UtilityListPHMN:
    def __init__(self, item):
        """
        :param item: the item that is used for this utility list
        """
        self.item = item  # the item
        self.sumIutils = 0  # the sum of item utilities
        self.sumRutils = 0  # the sum of remaining utilities
        self.elements = []  # the elements
        self.largestPeriodicity = 0
        self.smallestPeriodicity = float("inf")

    def getLargestPeriodicity(self):
        """
        Get the periodicity of this pattern.
            :return: the periodicity
        """
        return self.largestPeriodicity

    def addElement(self, element):
        """Add an element to this utility list.
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


class AlgoPHMN:
    def __init__(self):
        self.phuiCount = 0
        self.candidateCount = 0
        self.mapItemToTWU = {}
        self.mapTidtoMapItemToUtility = defaultdict(dict)
        self.mapItemToItemInfo = {}
        self.writer = None
        self.mapEUCS = None
        self.mapESCS = None
        self.improve = False
        self.minUtil = 0
        self.ENABLE_LA_PRUNE = True
        self.ENABLE_EUCP = True
        self.ENABLE_ESCP = True
        self.DEBUG = False
        self.BUFFERS_SIZE = 200
        self.itemsetBuffer = None
        self.databaseSize = 0
        self.minPeriodicity = 0
        self.maxPeriodicity = 0
        self.minAveragePeriodicity = 0
        self.maxAveragePeriodicity = 0
        self.minimumLength = 0
        self.maximumLength = float("inf")
        self.supportPruningThreshold = 0
        self.totalExecutionTime = 0
        self.maximumMemoryUsage = 0
        self.findingIrregularItemsets = False
        self.xx = 1

    class IMP:
        def __init__(self):
            self.tid = 0
            self.item = 0

    class Pair:
        def __init__(self):
            self.item = 0
            self.utility = 0

    class ItemInfo:
        def __init__(self):
            self.support = 0
            self.largestPeriodicity = 0
            self.smallestPeriodicity = float("inf")
            self.lastSeenTransaction = 0

    def runAlgorithm(
        self,
        improve: bool,
        input: str,
        output: str,
        minUtility: int,
        minPeriodicity: int,
        maxPeriodicity: int,
        minAveragePeriodicity: int,
        maxAveragePeriodicity: int,
    ):
        """Execute the periodic high-utility mining (PHM) algorithm.

        Args:
            improve (bool): Flag to enable or disable improved pruning strategies.
                - If True, additional pruning based on item relationships is performed.
            input (str): Path to the input transaction file.
                - Format: Each line contains:
                    - A list of item IDs separated by spaces.
                    - A colon (`:`) separating the transaction utility value.
                    - A list of utility values corresponding to each item.
            output (str): Path to the output file to save results.
                - The output will include discovered high-utility patterns and associated metrics.
            minUtility (int): The minimum utility threshold for patterns to be considered.
            minPeriodicity (int): The minimum periodicity threshold (frequency of occurrence).
            maxPeriodicity (int): The maximum periodicity threshold (upper limit on the interval).
            minAveragePeriodicity (int): The minimum average periodicity threshold (mean occurrence frequency).
            maxAveragePeriodicity (int): The maximum average periodicity threshold (mean occurrence interval).

        Returns:
            None: The function writes results to the output file and does not return a value.
        """
        self.minUtil = minUtility
        self.maxPeriodicity = maxPeriodicity
        self.minPeriodicity = minPeriodicity
        self.minAveragePeriodicity = minAveragePeriodicity
        self.maxAveragePeriodicity = maxAveragePeriodicity
        self.improve = improve
        self.itemsetBuffer = [0] * self.BUFFERS_SIZE

        if self.ENABLE_EUCP:
            self.mapEUCS = defaultdict(dict)
        if self.ENABLE_ESCP:
            self.mapESCS = defaultdict(dict)

        startTimestamp = time.time()
        self.writer = open(output, "w")

        self.mapItemToTWU = {}
        self.mapItemToItemInfo = {}

        self.databaseSize = 0
        sumOfTransactionLength = 0

        with open(input, "r") as file:
            for line in file:
                if line.strip() == "" or line[0] in "#%@":
                    continue

                self.databaseSize += 1
                parts = line.split(":")
                if len(parts) < 2:
                    continue

                items = parts[0].split()
                transactionUtility = int(parts[1])

                sumOfTransactionLength += len(items)

                for item in items:
                    item = int(item)
                    twu = self.mapItemToTWU.get(item, 0) + transactionUtility
                    self.mapItemToTWU[item] = twu

                    itemInfo = self.mapItemToItemInfo.get(item, self.ItemInfo())
                    itemInfo.support += 1

                    periodicity = self.databaseSize - itemInfo.lastSeenTransaction
                    if itemInfo.largestPeriodicity < periodicity:
                        itemInfo.largestPeriodicity = periodicity
                    itemInfo.lastSeenTransaction = self.databaseSize

                    if (
                        itemInfo.support != 1
                        and periodicity < itemInfo.smallestPeriodicity
                    ):
                        itemInfo.smallestPeriodicity = periodicity

                    self.mapItemToItemInfo[item] = itemInfo

        self.supportPruningThreshold = (
            self.databaseSize / self.maxAveragePeriodicity
        ) - 1

        for item, itemInfo in self.mapItemToItemInfo.items():
            periodicity = self.databaseSize - itemInfo.lastSeenTransaction
            if itemInfo.largestPeriodicity < periodicity:
                itemInfo.largestPeriodicity = periodicity

        listOfUtilityLists = []
        mapItemToUtilityList = {}

        for item, twu in self.mapItemToTWU.items():
            itemInfo = self.mapItemToItemInfo[item]
            if (
                itemInfo.support >= self.supportPruningThreshold
                and itemInfo.largestPeriodicity <= self.maxPeriodicity
                and twu >= self.minUtil
            ):
                uList = UtilityListPHMN(item)
                mapItemToUtilityList[item] = uList
                listOfUtilityLists.append(uList)
                uList.largestPeriodicity = itemInfo.largestPeriodicity
                uList.smallestPeriodicity = itemInfo.smallestPeriodicity

        # listOfUtilityLists.sort(key=lambda x: x.item)

        listOfUtilityLists.sort(key=lambda x: self.mapItemToTWU[x.item])

        with open(input, "r") as file:
            tid = 0
            for line in file:
                if line.strip() == "" or line[0] in "#%@":
                    continue

                items, transactionUtility, utilityValues = line.split(":")
                items = items.split()
                utilityValues = utilityValues.split()

                revisedTransaction = []
                remainingUtility = 0
                newTWU = 0

                mmap = {}
                for item, utility in zip(items, utilityValues):
                    item = int(item)
                    utility = int(utility)
                    itemInfo = self.mapItemToItemInfo[item]
                    if (
                        itemInfo.support >= self.supportPruningThreshold
                        and itemInfo.largestPeriodicity <= self.maxPeriodicity
                        and self.mapItemToTWU[item] >= self.minUtil
                    ):
                        pair = self.Pair()
                        pair.item = item
                        pair.utility = utility
                        revisedTransaction.append(pair)
                        remainingUtility += utility
                        newTWU += utility

                    if self.improve:
                        mmap[item] = utility

                self.mapTidtoMapItemToUtility[tid] = mmap

                revisedTransaction.sort(key=lambda x: self.mapItemToTWU[x.item])

                for i, pair in enumerate(revisedTransaction):
                    remainingUtility -= pair.utility
                    utilityListOfItem = mapItemToUtilityList[pair.item]
                    element = ElementPHMN(tid, pair.utility, remainingUtility)
                    utilityListOfItem.addElement(element)

                    if self.ENABLE_EUCP:
                        mapFMAPItem = self.mapEUCS[pair.item]
                        for j in range(i + 1, len(revisedTransaction)):
                            pairAfter = revisedTransaction[j]
                            mapFMAPItem[pairAfter.item] = (
                                mapFMAPItem.get(pairAfter.item, 0) + newTWU
                            )

                    if self.ENABLE_ESCP:
                        mapESItem = self.mapESCS[pair.item]
                        for j in range(i + 1, len(revisedTransaction)):
                            pairAfter = revisedTransaction[j]
                            mapESItem[pairAfter.item] = (
                                mapESItem.get(pairAfter.item, 0) + 1
                            )

                tid += 1

        self.mapItemToItemInfo = None
        self.mapItemToTWU = None
        self.mapItemToUtilityList = None

        self.phm(self.itemsetBuffer, 0, None, listOfUtilityLists, self.minUtil)

        self.writer.close()
        self.totalExecutionTime = time.time() - startTimestamp

    def phm(
        self,
        prefix: list[int],
        prefixLength: int,
        pUL: UtilityListPHMN,
        ULs: list[UtilityListPHMN],
        minUtility: int,
    ) -> None:
        """
        Perform periodic high-utility mining (PHM) recursively to explore and identify
        high-utility itemsets that satisfy utility and periodicity constraints.

        Args:
            prefix (list[int]): The current prefix itemset being expanded.
            prefixLength (int): The current length of the prefix itemset.
            pUL (UtilityListPHMN): The utility list of the parent prefix itemset.
            ULs (list[UtilityListPHMN]): Utility lists of the current items being processed.
            minUtility (int): The minimum utility threshold for a pattern to be considered.

        Returns:
            None: Results are processed and stored within the algorithm, and patterns are written to output.
        """
        patternSize = prefixLength + 1

        for i, X in enumerate(ULs):
            if X.sumIutils + X.sumRutils >= minUtility:
                averagePeriodicity = self.databaseSize / (X.getSupport() + 1)

                if (
                    X.sumIutils >= minUtility
                    and averagePeriodicity <= self.maxAveragePeriodicity
                    and averagePeriodicity >= self.minAveragePeriodicity
                    and X.smallestPeriodicity >= self.minPeriodicity
                    and X.largestPeriodicity <= self.maxPeriodicity
                ):
                    if (
                        patternSize >= self.minimumLength
                        and patternSize <= self.maximumLength
                    ):
                        self.writeOut(prefix, prefixLength, X, averagePeriodicity)

                if patternSize < self.maximumLength:
                    exULs = []
                    for j in range(i + 1, len(ULs)):
                        Y = ULs[j]

                        if self.ENABLE_EUCP:
                            mapTWUF = self.mapEUCS.get(X.item, {})
                            if mapTWUF.get(Y.item, 0) < minUtility:
                                continue

                        if self.ENABLE_ESCP:
                            mapSUPF = self.mapESCS.get(X.item, {})
                            if mapSUPF.get(Y.item, 0) < self.supportPruningThreshold:
                                continue

                        self.candidateCount += 1
                        if self.candidateCount % 10000 == 0:
                            print(self.xx)
                            self.xx += 1

                        temp = self.construct(pUL, X, Y, minUtility)
                        if temp is None and self.improve:
                            exULs = self.funcImprove(exULs, Y.item)
                        elif temp is not None:
                            exULs.append(temp)

                    prefix[prefixLength] = X.item
                    self.phm(prefix, prefixLength + 1, X, exULs, minUtility)

    def funcImprove(
        self, exULs: list[UtilityListPHMN], item: int
    ) -> list[UtilityListPHMN]:
        """
        Apply an improvement function to enhance utility list pruning by reconstructing
        utility lists based on interactions between items in the revised transactions.

        Args:
            exULs (list[UtilityListPHMN]): The list of existing utility lists for current extensions.
            item (int): The item for which the utility lists are being improved.

        Returns:
            list[UtilityListPHMN]: A list of updated utility lists after applying the improvement logic.
        """
        ress = []
        for utilityListPHM in exULs:
            utilityListPHM1 = UtilityListPHMN(utilityListPHM.item)
            utilityListPHM1.largestPeriodicity = utilityListPHM.largestPeriodicity
            utilityListPHM1.smallestPeriodicity = utilityListPHM.smallestPeriodicity
            for element in utilityListPHM.elements:
                mmap = self.mapTidtoMapItemToUtility[element.tid]
                if item in mmap:
                    rUtil = element.rutils - mmap[item]
                    element1 = ElementPHMN(element.tid, element.iutils, rUtil)
                else:
                    element1 = ElementPHMN(element.tid, element.iutils, element.rutils)
                utilityListPHM1.addElement(element1)
            ress.append(utilityListPHM1)
        return ress

    def construct(
        self,
        P: UtilityListPHMN,
        px: UtilityListPHMN,
        py: UtilityListPHMN,
        minUtility: int,
    ) -> UtilityListPHMN | None:
        """
        Construct the utility list for the combined itemset (P ∪ {px.item, py.item}).

        Args:
            P (UtilityListPHMN): The utility list of the prefix itemset.
            px (UtilityListPHMN): The utility list of the first item in the extension.
            py (UtilityListPHMN): The utility list of the second item in the extension.
            minUtility (int): The minimum utility threshold for the combined itemset.

        Returns:
            UtilityListPHMN | None: The utility list of the combined itemset if it meets
            the utility and periodicity constraints, otherwise None.
        """
        pxyUL = UtilityListPHMN(py.item)
        lastTid = -1
        totalUtility = px.sumIutils + px.sumRutils
        totalSupport = px.getSupport()

        for ex in px.elements:
            ey = self.findElementWithTID(py, ex.tid)
            if ey is None:
                if self.ENABLE_LA_PRUNE:
                    totalUtility -= ex.iutils + ex.rutils
                    if totalUtility < minUtility:
                        return None
                    totalSupport -= 1
                    if totalSupport < self.supportPruningThreshold:
                        return None
                continue

            if P is None:
                periodicity = ex.tid - lastTid
                if periodicity > self.maxPeriodicity:
                    return None
                if periodicity >= pxyUL.largestPeriodicity:
                    pxyUL.largestPeriodicity = periodicity
                lastTid = ex.tid
                if pxyUL.elements and periodicity < pxyUL.smallestPeriodicity:
                    pxyUL.smallestPeriodicity = periodicity

                eXY = ElementPHMN(ex.tid, ex.iutils + ey.iutils, ey.rutils)
                pxyUL.addElement(eXY)
            else:
                e = self.findElementWithTID(P, ex.tid)
                if e is not None:
                    periodicity = ex.tid - lastTid
                    if periodicity > self.maxPeriodicity:
                        return None
                    if periodicity >= pxyUL.largestPeriodicity:
                        pxyUL.largestPeriodicity = periodicity
                    lastTid = ex.tid
                    if pxyUL.elements and periodicity < pxyUL.smallestPeriodicity:
                        pxyUL.smallestPeriodicity = periodicity

                    eXY = ElementPHMN(
                        ex.tid, ex.iutils + ey.iutils - e.iutils, ey.rutils
                    )
                    pxyUL.addElement(eXY)

        periodicity = (self.databaseSize - 1) - lastTid
        if periodicity > self.maxPeriodicity:
            return None
        if periodicity >= pxyUL.largestPeriodicity:
            pxyUL.largestPeriodicity = periodicity
        if pxyUL.getSupport() < self.supportPruningThreshold:
            return None

        return pxyUL

    def findElementWithTID(
        self, ulist: UtilityListPHMN, tid: int
    ) -> ElementPHMN | None:
        """
        Find an element in a utility list with a specific transaction ID (TID).

        Args:
            ulist (UtilityListPHMN): The utility list to search.
            tid (int): The transaction ID to find.

        Returns:
            ElementPHMN | None: The element with the matching transaction ID, or None if not found.
        """
        first, last = 0, len(ulist.elements) - 1
        while first <= last:
            middle = (first + last) // 2
            if ulist.elements[middle].tid < tid:
                first = middle + 1
            elif ulist.elements[middle].tid > tid:
                last = middle - 1
            else:
                return ulist.elements[middle]
        return None

    def writeOut(
        self,
        prefix: list[int],
        prefixLength: int,
        utilityList: UtilityListPHMN,
        averagePeriodicity: float,
    ) -> None:
        """
        Write the discovered high-utility itemset to the output file.

        Args:
            prefix (list[int]): The prefix itemset leading to the current itemset.
            prefixLength (int): The length of the prefix.
            utilityList (UtilityListPHMN): The utility list of the current itemset.
            averagePeriodicity (float): The average periodicity of the current itemset.

        Returns:
            None: Writes the formatted itemset details to the output file.
        """
        self.phuiCount += 1
        buffer = (
            " ".join(map(str, prefix[:prefixLength]))
            + f" {utilityList.item} #UTIL: {utilityList.sumIutils}"
        )
        if self.findingIrregularItemsets:
            buffer += f" #REG: {utilityList.largestPeriodicity}"
        else:
            buffer += f" #SUP: {utilityList.getSupport()} #MINPER: {utilityList.smallestPeriodicity} #MAXPER: {utilityList.largestPeriodicity} #AVGPER: {averagePeriodicity}"
        self.writer.write(buffer.strip() + "\n")

    def printStats(self) -> None:
        """
        Print detailed statistics about the execution of the algorithm, including:
        - Configuration settings (e.g., EUCP, ESCP, pattern type).
        - Database size and execution time.
        - Memory usage and discovered high-utility itemset counts.
        - Candidate generation statistics.

        Returns:
            None: Prints the statistics to the console.
        """
        print("===== CONTENT OF EUCP =====")
        for item, mapFMAPItem in self.mapEUCS.items():
            print(f"Item: {item} -- ", end="")
            for item2, twu in mapFMAPItem.items():
                print(f"{item2} ({twu})  ", end="")
            print()

        print("===== CONTENT OF ESCS =====")
        for item, mapESItem in self.mapESCS.items():
            print(f"Item: {item} -- ", end="")
            for item2, support in mapESItem.items():
                print(f"{item2} ({support})  ", end="")
            print()

        optimizationEUCP = " EUCP: true -" if self.ENABLE_EUCP else " EUCP: false -"
        optimizationESCP = " ESCP: true " if self.ENABLE_ESCP else " ESCP: false "
        name = "PHMN+" if self.improve else "PHMN"
        patternType = "Periodic"

        if self.findingIrregularItemsets:
            name += "_irregular"
            optimizationESCP = ""
            patternType = "Irregular"

        print(f"=============  {name} v2.38{optimizationEUCP}{optimizationESCP}=====")
        print(f" Database size: {self.databaseSize} transactions")
        print(f" Time : {self.totalExecutionTime} ms")
        print(f" Memory ~ {self.maximumMemoryUsage} MB")
        print(f" {patternType} High-utility itemsets count : {self.phuiCount}")
        print(f" Candidate count : {self.candidateCount}")

        if self.DEBUG and self.ENABLE_EUCP:
            pairCount = 0
            maxMemory = self.getObjectSize(self.mapEUCS)
            for item, mapFMAPItem in self.mapEUCS.items():
                maxMemory += self.getObjectSize(item)
                for item2, twu in mapFMAPItem.items():
                    pairCount += 1
                    maxMemory += self.getObjectSize(item2) + self.getObjectSize(twu)
            print(f"EUCS size {maxMemory} MB    PAIR COUNT {pairCount}")

        if self.DEBUG and self.ENABLE_ESCP:
            pairCount = 0
            maxMemory = self.getObjectSize(self.mapESCS)
            for item, mapESItem in self.mapESCS.items():
                maxMemory += self.getObjectSize(item)
                for item2, support in mapESItem.items():
                    pairCount += 1
                    maxMemory += self.getObjectSize(item2) + self.getObjectSize(support)
            print(f"ESCS size {maxMemory} MB    PAIR COUNT {pairCount}")

        print("===================================================")

    def getObjectSize(self, obj: object) -> float:
        """
        Calculate the approximate memory size of an object in megabytes.

        Args:
            obj (object): The Python object whose memory size is to be calculated.

        Returns:
            float: The size of the object in megabytes (MB).
        """
        import sys

        return sys.getsizeof(obj) / 1024 / 1024

    def setEnableEUCP(self, enable: bool) -> None:
        """
        Enable or disable the EUCP optimization for utility pruning.

        Args:
            enable (bool): Flag to enable (True) or disable (False) EUCP.

        Returns:
            None: Updates the EUCP setting.
        """
        self.ENABLE_EUCP = enable

    def setEnableESCP(self, enable: bool) -> None:
        """
        Enable or disable the ESCP optimization for support pruning.

        Args:
            enable (bool): Flag to enable (True) or disable (False) ESCP.

        Returns:
            None: Updates the ESCP setting.
        """
        self.ENABLE_ESCP = enable

    def setMinimumLength(self, minimumLength: int) -> None:
        """
        Set the minimum length constraint for high-utility itemsets.

        Args:
            minimumLength (int): The minimum length of itemsets to consider.

        Returns:
            None: Updates the minimum length setting.
        """
        self.minimumLength = minimumLength

    def setMaximumLength(self, maximumLength: int) -> None:
        """
        Set the maximum length constraint for high-utility itemsets.

        Args:
            maximumLength (int): The maximum length of itemsets to consider.

        Returns:
            None: Updates the maximum length setting.
        """
        self.maximumLength = maximumLength
