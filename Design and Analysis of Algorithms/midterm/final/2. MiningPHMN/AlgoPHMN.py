import time
from collections import defaultdict
from ElementPHMN import ElementPHMN
from UtilityListPHMN import UtilityListPHMN

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
        self.maximumLength = float('inf')
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
            self.smallestPeriodicity = float('inf')
            self.lastSeenTransaction = 0

    def runAlgorithm(self, improve, input, output, minUtility, minPeriodicity, maxPeriodicity, minAveragePeriodicity, maxAveragePeriodicity):
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
        self.writer = open(output, 'w')

        self.mapItemToTWU = {}
        self.mapItemToItemInfo = {}

        self.databaseSize = 0
        sumOfTransactionLength = 0

    
        with open(input, 'r') as file:
            for line in file:
                if line.strip() == '' or line[0] in '#%@':
                    continue

                self.databaseSize += 1
                parts = line.split(':')
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

                    if itemInfo.support != 1 and periodicity < itemInfo.smallestPeriodicity:
                        itemInfo.smallestPeriodicity = periodicity

                    self.mapItemToItemInfo[item] = itemInfo

       

        self.supportPruningThreshold = (self.databaseSize / self.maxAveragePeriodicity) - 1

        for item, itemInfo in self.mapItemToItemInfo.items():
            periodicity = self.databaseSize - itemInfo.lastSeenTransaction
            if itemInfo.largestPeriodicity < periodicity:
                itemInfo.largestPeriodicity = periodicity

        listOfUtilityLists = []
        mapItemToUtilityList = {}

        for item, twu in self.mapItemToTWU.items():
            itemInfo = self.mapItemToItemInfo[item]
            if itemInfo.support >= self.supportPruningThreshold and itemInfo.largestPeriodicity <= self.maxPeriodicity and twu >= self.minUtil:
                uList = UtilityListPHMN(item)
                mapItemToUtilityList[item] = uList
                listOfUtilityLists.append(uList)
                uList.largestPeriodicity = itemInfo.largestPeriodicity
                uList.smallestPeriodicity = itemInfo.smallestPeriodicity

        # listOfUtilityLists.sort(key=lambda x: x.item)

        listOfUtilityLists.sort(key=lambda x: self.mapItemToTWU[x.item])
        
        


        with open(input, 'r') as file:
            tid = 0
            for line in file:
                if line.strip() == '' or line[0] in '#%@':
                    continue

                items, transactionUtility, utilityValues = line.split(':')
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
                    if itemInfo.support >= self.supportPruningThreshold and itemInfo.largestPeriodicity <= self.maxPeriodicity and self.mapItemToTWU[item] >= self.minUtil:
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
                            mapFMAPItem[pairAfter.item] = mapFMAPItem.get(pairAfter.item, 0) + newTWU

                    if self.ENABLE_ESCP:
                        mapESItem = self.mapESCS[pair.item]
                        for j in range(i + 1, len(revisedTransaction)):
                            pairAfter = revisedTransaction[j]
                            mapESItem[pairAfter.item] = mapESItem.get(pairAfter.item, 0) + 1

                tid += 1

        self.mapItemToItemInfo = None
        self.mapItemToTWU = None
        self.mapItemToUtilityList = None


        self.phm(self.itemsetBuffer, 0, None, listOfUtilityLists, self.minUtil)

        self.writer.close()
        self.totalExecutionTime = time.time() - startTimestamp

    def phm(self, prefix, prefixLength, pUL, ULs, minUtility):
        patternSize = prefixLength + 1

        for i, X in enumerate(ULs):
            if X.sumIutils + X.sumRutils >= minUtility:
                averagePeriodicity = self.databaseSize / (X.getSupport() + 1)

                if X.sumIutils >= minUtility and averagePeriodicity <= self.maxAveragePeriodicity and averagePeriodicity >= self.minAveragePeriodicity and X.smallestPeriodicity >= self.minPeriodicity and X.largestPeriodicity <= self.maxPeriodicity:
                    if patternSize >= self.minimumLength and patternSize <= self.maximumLength:
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

    def funcImprove(self, exULs, item):
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

    def construct(self, P, px, py, minUtility):
        pxyUL = UtilityListPHMN(py.item)
        lastTid = -1
        totalUtility = px.sumIutils + px.sumRutils
        totalSupport = px.getSupport()

        for ex in px.elements:
            ey = self.findElementWithTID(py, ex.tid)
            if ey is None:
                if self.ENABLE_LA_PRUNE:
                    totalUtility -= (ex.iutils + ex.rutils)
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

                    eXY = ElementPHMN(ex.tid, ex.iutils + ey.iutils - e.iutils, ey.rutils)
                    pxyUL.addElement(eXY)

        periodicity = (self.databaseSize - 1) - lastTid
        if periodicity > self.maxPeriodicity:
            return None
        if periodicity >= pxyUL.largestPeriodicity:
            pxyUL.largestPeriodicity = periodicity
        if pxyUL.getSupport() < self.supportPruningThreshold:
            return None

        return pxyUL

    def findElementWithTID(self, ulist, tid):
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

    def writeOut(self, prefix, prefixLength, utilityList, averagePeriodicity):
        self.phuiCount += 1
        buffer = ' '.join(map(str, prefix[:prefixLength])) + f' {utilityList.item} #UTIL: {utilityList.sumIutils}'
        if self.findingIrregularItemsets:
            buffer += f' #REG: {utilityList.largestPeriodicity}'
        else:
            buffer += f' #SUP: {utilityList.getSupport()} #MINPER: {utilityList.smallestPeriodicity} #MAXPER: {utilityList.largestPeriodicity} #AVGPER: {averagePeriodicity}'
        self.writer.write(buffer.strip() + '\n')

    def printStats(self):
        print("===== CONTENT OF EUCP =====")
        for item, mapFMAPItem in self.mapEUCS.items():
            print(f"Item: {item} -- ", end='')
            for item2, twu in mapFMAPItem.items():
                print(f"{item2} ({twu})  ", end='')
            print()

        print("===== CONTENT OF ESCS =====")
        for item, mapESItem in self.mapESCS.items():
            print(f"Item: {item} -- ", end='')
            for item2, support in mapESItem.items():
                print(f"{item2} ({support})  ", end='')
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

    def getObjectSize(self, obj):
        import sys
        return sys.getsizeof(obj) / 1024 / 1024

    def setEnableEUCP(self, enable):
        self.ENABLE_EUCP = enable

    def setEnableESCP(self, enable):
        self.ENABLE_ESCP = enable

    def setMinimumLength(self, minimumLength):
        self.minimumLength = minimumLength

    def setMaximumLength(self, maximumLength):
        self.maximumLength = maximumLength
