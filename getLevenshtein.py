import math

def characterCountChanges(s1, s2):
    math.fabs(len(s1) - len(s2))


def getLevenshteinDistance(s1, s2):
    d = []

    for i in range(len(s1) + 1):
        sublist = []
        for j in range(len(s2) + 1):
            sublist.append(0)
        d.append(sublist)

    for i in range(len(s1)+1):
        d[i][0] = i

    for j in range(len(s2)+1):
        d[0][j] = j

    for j in range(1, len(s2)+1):
        for i in range(1, len(s1)+1):
            cost = 0
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    # for i in range(len(s1)+1):
    #     for j in range(len(s2)+1):
    #         print(d[i][j], end=" ")
    #     print(" ")


    return d[len(s1)][len(s2)]


def getWordChanges(s1, s2):
    similarityThreshold = 1
    wordChanges = 0

    s1 = s1.lower().replace(".", "").replace(",", "").replace(";", "")
    s2 = s2.lower().replace(".", "").replace(",", "").replace(";", "")

    # Loop through each word in s1
    for i in range(len(s1.split(" "))):
        exists = False
        ##search for i'th word in s1 and s2
        for j in range(len(s2.split(" "))):
            # is the word misspelled?
            if (getLevenshteinDistance(s1.split(" ")[i], s2.split(" ")[j]) * 100 / len(s1.split(" ")[i])) < similarityThreshold:
                exists = True
                break

        ##If the word does not exist, increment wordChanges
        if exists == False:
            wordChanges += 1
    return wordChanges

def wordCountChanges(s1, s2):
    math.fabs(s1.split(" ").length() - s2.split(" ").length())

def stringSimilar(s1, s2):
    characterChanges = getLevenshteinDistance(s1, s2)
    wordChanges = getWordChanges(s1, s2)
    characterCountChange = math.fabs(len(s1) - len(s2))
    wordCountChange = math.fabs(len(s1.split(" ")) - len(s2.split(" ")))
    similarity1 = 100 - characterChanges * 100 / len(s1)
    similarity2 = 100 - wordChanges * 100 / len(s1.split(" ")) if len(s1.split(" ")) > len(s2.split(" ")) else len(s2.split(" "))
    similarity3 = 100 - characterCountChange * 100 / len(s1)
    similarity4 = 100 - wordCountChange * 100 / len(s1.split(" "))
    similarity = round(similarity1 + similarity2 * 2 + similarity3 + similarity4) / 5
    print("Character Changes: " + str(characterChanges))
    print("Word Changes: " + str(wordChanges))
    print("Character Count Change: " + str(characterCountChange))
    print("Word Count Change: " + str(wordCountChange))



stringSimilar("gambol b c", "gumbo a c")