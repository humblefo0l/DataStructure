

def findTruckCargo(maxCargoWeight, cargoList):


    # for l in cargoList:
    #     if l[1] > maxCargoWeight:
    #         cargoList.remove(l)
    #
    # maxProfit = 0
    # maxWeight = 0
    # uniqueNum = []
    #
    #
    # for l in cargoList.copy():
    #     for j in cargoList.copy():
    #         if l != j:
    #             w = l[1] + j[1]
    #             p = l[2] + j[2]
    #             if  w <= maxCargoWeight:
    #                 if p > maxProfit:
    #                     uniqueNum = [l[0], j[0]]
    #                     maxProfit = p
    #
    #
    #
    # uniqueNum.append(maxProfit)
    # return uniqueNum


    # dp = [ 0 for i in cargoList]+[0]
    #
    # c=1
    # for i in cargoList[1:]:
    #
    #     d = cargoList[c][1] + cargoList[c-1][1]
    #     if d <= maxCargoWeight:
    #         dp[c] = d
    #     c += 1
    #
    # print(c)



a = findTruckCargo(300, [
                        [38,130,500],
                        [21,280,1800],
                        [13,120,1500],
                        [1,1,1111],
                        [11,1,111111]
            ])

