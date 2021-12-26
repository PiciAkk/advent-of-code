def solutionFinder(inputText):
    bits = []
    epsilonRate = ""
    gammaRate = ""
    for i in range(len(list(inputText[0]))):
        bits.append({1: 0, 0: 0})
    for i in inputText:
        currentLine = list(i)
        # végigiterálunk az input szöveg minden sorának minden számán
        for j in range(len(currentLine)):
            # megnézzük, hogy a `bits` listában létezik-e már j. elem
            bits[j][int(currentLine[j])] += 1
    # végigiterálunk a `bits` listán
    for i in bits:
        # megnézzük, hogy a jelenlegi értéken egyesekből több van-e, mint nullásokból
        if i[1] > i[0]:
            # ha igen, a gammaRatehez hozzáadunk egy egyest (mert ezen a pozíción az egyes volt a gyakoribb)
            gammaRate += "1"
            # az epsilonRate-hez pedig hozzáadunk egy nullást (mert ezen a pozíción a nullás volt a kevésbé gyakori)
            epsilonRate += "0"
        # megnézzük, hogy a jelenlegi értéken nullásokból több van-e mint egyesekből
        else:
            # ha igen, a gammaRatehez hozzáadunk egy nullást (mert ezen a pozíción a nullás volt a gyakoribb)
            gammaRate += "0"
            # az epsilonRate-hez pedig hozzáadunk egy egyest (mert ezen a pozíción az egyes volt a kevésbé gyakori)
            epsilonRate += "1"
    return gammaRate, epsilonRate