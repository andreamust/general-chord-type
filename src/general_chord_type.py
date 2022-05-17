"""

"""

from itertools import combinations

import numpy as np


def find_subsets(m):
    s = set(m)
    subsets = sum(map(lambda r: list(combinations(s, r)), range(1, len(s) + 1)),
                  [])  # find all the possible compinations
    subsRev = list(reversed(subsets))  # reversed to bring max length subset first
    subs = []

    # sort the subsRev
    for i in subsRev:
        subs.append(sorted(i))
    # print("Subsets: ", subs)
    return subs


# find consonant intervals between pitches
def find_consonant_sequences_subsets(consWeights, subs):
    cons = []  # empty list
    for s in subs:
        d = [[0] * len(s)] * (len(s))  # make a 2d list of zeros
        dBin = np.array([[0] * len(s)] * (
            len(s)))  # make a second 2d list of zeros for appending ones. This is going to be the 2d array with the
        # distances of notes of the chord
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                d[i][j] = abs(s[j] - s[i])  # find the distance between two pitches of the subset
                while d[i][j] < 0:  # if the distance is negative, add 12
                    d[i][j] = d[i][j] + 12
                if consWeights[d[i][j]] == 1:  # if the consWeight is consonant
                    dBin[i][j] = 1  # put an 1 into the dBin list
        if np.all(dBin) == 1:  # all values of the list equals one, the pitch sequence is consonant
            cons.append(s)
    # print("Consonant: ", cons)
    return cons


# keep only consonant subsets with max length
def find_maximal_consonant_subsets(consonant):
    maxConSubs = []
    for i in consonant:
        if len(i) == len(max(consonant, key=len)):
            maxConSubs.append(i)
    # maxConSubsNp = np.array(maxConSubs)
    # maxConSubs = np.concatenate(maxConSubs)
    # print("Maximal Consonant Subsets: ", maxConSubs)
    return maxConSubs


def HARM_findExtentions(m, maxConSubs):
    chEx = []
    for s in maxConSubs:
        chEx.append(list(m[[not (m[i] in s) for i in range(len(m))]]))
    # chEx = np.concatenate(chEx) #works for one. try it with many chords with more extentions!!
    # print('Chord Extentions: ', chEx)
    return chEx


def shortest_form_subsets(maxConSubs):
    maxConSubss = list(maxConSubs)
    lastFirstInterval = []  # [[0]*len(maxConSubss)*len(maxConSubss[0])]
    shiftedChords = []

    for i in range(0, len(maxConSubss)):

        shiftedCh = []
        lastFirstInterval1 = []
        n = 0
        while n < len(maxConSubss[i]):
            shiftedCh1 = []
            # mCSDeq = deque(maxConSubss[i])
            # mCSDeq.rotate(1)
            # mCS = mCSDeq.popleft()
            maxConSubss[i].insert((len(maxConSubss[i]) - 1), maxConSubss[i].pop(0))  # circlular shifting
            shiftedCh1.extend(maxConSubss[i])  # put it in shoftedCh1 array
            lastFirstInt = maxConSubss[i][-1] - maxConSubss[i][
                0]  # find interval between first and last pitch of the max sconsonand chord
            if lastFirstInt < 0:  # if < 0 add 12 to move it to the next octave
                lastFirstInt = lastFirstInt + 12
            # lastFirstInterval[i][n] = lastFirstInt #put it in lastFirstInterval array
            lastFirstInterval1.append(lastFirstInt)
            shiftedCh.append(shiftedCh1)  # put it in shiftesCh array
            n = n + 1

        shiftedChords.append(shiftedCh)  # put in the shifted chords array for each
        lastFirstInterval.append(lastFirstInterval1)
    # print("shifted: ", shiftedChords)
    # print("Intervals between first and last pitrch (for each max consonant): ", lastFirstInterval)

    shortestAll = []
    for i in range(len(lastFirstInterval)):
        shortestChOfEach = []
        shortest = min(lastFirstInterval[i])
        for j in range(len(lastFirstInterval[i])):
            if lastFirstInterval[i][j] == shortest:
                shortestChOfEach.append(shiftedChords[i][j])  # put it in an array
                shortestAll.append(shortestChOfEach)  # make array with all shortest chords
    # print("Shortest Chords: ", shortestAll)

    # NEEDS TESTING
    # if the shortest forms are more than one, you have to choose somehow
    for i in range(0, len(shortestAll)):
        for j in range(0, len(shortestAll[i])):
            # for k in range(0, len(shortestAll[i][j])):
            if len(shortestAll[i]) >= 2:  # if there are more than one shortest forms for one chord
                for j in range(len(shortestAll[i]) - 1):
                    baseLengthj = shortestAll[i][j][1] - shortestAll[i][j][
                        0]  # find the base length (first and second interval) of a shortest form of a chord
                    baseLengthjNext = shortestAll[i][j + 1][1] - shortestAll[i][j + 1][
                        0]  # find the base length of the next shortest form of a chord
                    if baseLengthj < 0:
                        baseLengthj = baseLengthj + 12  # if < 0 move it to the next octave
                    if baseLengthjNext < 0:
                        baseLengthjNext = baseLengthjNext + 12
                    if (baseLengthj) < (baseLengthjNext):  # find the shortest form with shortest baselength
                        shortestBaseLength = shortestAll[i][j]  # and that's the form I want
                        print("Shortest with minimum baselength:", shortestBaseLength)  # NA TO TSEKARW ME POLLA CHORDS
                        # KAI PREPEI NA FTIAKSW ARRAY GIA OLA TA BASELENGTHS
    return shortestAll


def root_extension_form(shortest, chExtentions):
    firstsPitches = []
    for i in range(len(shortest)):
        for j in range(len(shortest[0])):
            firstsPitches.append(shortest[i][j][0])
            pClList = []
            for k in range(len(shortest[0][0])):
                pCl = shortest[i][j][k] - shortest[i][j][0]
                if pCl < 0:
                    pCl = pCl + 12
                pClList.append(pCl)
            shortest[i][j] = pClList
    # move extention relatively to 0
    for i in range(len(chExtentions)):
        for j in range(len(chExtentions[i])):
            chExtentions[i][j] = chExtentions[i][j] - firstsPitches[i]
            if chExtentions[i][j] < 0:
                chExtentions[i][j] = chExtentions[i][j] + 12
    for i in range(len(shortest)):
        shortest[i].insert(0, firstsPitches[i])
        shortest[i].append(chExtentions[i])
        # for j in range(len(shortest[0][0])):
        # shortest[i].extend()
    # notation = np.array(shortest, dtype=object)

    notation = shortest
    for i in range(len(notation)):
        maxNot = max(notation[i][1])
        for j in range(len(notation[i][2])):
            if notation[i][2][j] < maxNot:
                notation[i][2][j] = notation[i][2][j] + 12

    # with np arrays
    '''for i in range(len(notation)):
        notation[i][0] = np.array(notation[1][0])
        notation[i][2] = np.array(notation[i][2])
        notation[i][1] = np.array(notation[i][1])
        j = notation[i][2]< np.max(notation[i][1])
        notation[i][2][j] = notation[i][2][j]+12'''

    print("Chord: ", notation)
    return (notation)


def consonance_chord_recognizer(chord, cons_weights):
    modChord = [i % 12 for i in chord]  # modulo 12 to chord list to take the pitch classes
    m = np.unique(modChord)  # take only unique values
    # print("Pitches: ", m)

    # allPaths = np.size((dBin),0) #number of paths (in the tree)

    # find subsets/possible combinations between pitches
    subs = find_subsets(m)

    # find consonant intervals between pitches
    consonant = find_consonant_sequences_subsets(cons_weights, subs)

    # find Maximal Consonant Subsets
    maxConSubs = find_maximal_consonant_subsets(consonant)

    # find extentions
    chExtentions = HARM_findExtentions(m, maxConSubs)

    # find shortest form func
    shortest = shortest_form_subsets(maxConSubs)

    # normal order invertion function
    # noi = normalOrderInversion(maxConSubs)

    # MAKE HERE A FUNCTIONS FOR CHOOSING THE SHORTEST FORM DEPENDING THE BASELENGTH (code ready in
    # HARM_shortestFormOfSubsets(maxConSubs))

    chordForm = root_extension_form(shortest, chExtentions)
