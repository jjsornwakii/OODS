def move(n, A, C, B, maxn):
    if n == maxn:
        
        global lA, lB, lC
        global iA, iB, iC

        lA, lB, lC = [], [], []
        iA, iB, iC = maxn-1, -1, -1
        tempA, tempB, tempC = [], [], []

        lA = createTower(maxn, tempA, 0)
        lB = createTower(maxn, tempB, 1)
        lC = createTower(maxn, tempC, 1)
        showTower(lA, lB, lC, maxn)
    if n == 1:
        print("move", n, 'from ', A, 'to', C)
        changeTower(A, C)
        showTower(lA, lB, lC, maxn)
    else:
        move(n-1, A, B, C, maxn)
        print("move", n, 'from ', A, 'to', C)
        changeTower(A, C)
        showTower(lA, lB, lC, maxn)
        move(n-1, B, C, A, maxn)


def showTower(lA, lB, lC, n):
    if n >= 0:
        print(str(lA[n]) + "  " + lB[n] + "  " + lC[n])
        showTower(lA, lB, lC, n-1)


def createTower(n, l, empty):
    if empty == 0:
        if n > 0:
            l.append(str(n))
            return createTower(n-1, l, empty)
        elif n == 0:
            l.append('|')
            return createTower(n-1, l, empty)
        else:
            return l
    else:
        if n >= 0:
            l.append('|')
            return createTower(n-1, l, empty)
        else:
            return l


def changeTower(list1, list2):

    global lA, lB, lC

    global iA, iB, iC

    if list1 == 'A' and list2 == 'B':
        ti = lB.index('|')
        lB[ti] = lA[iA]
        lA[iA] = '|'
        iA -= 1
        iB += 1

    elif list1 == 'A' and list2 == 'C':
        ti = lC.index('|')
        lC[ti] = lA[iA]
        lA[iA] = '|'
        iA -= 1
        iC += 1

    elif list1 == 'B' and list2 == 'C':
        ti = lC.index('|')
        lC[ti] = lB[iB]
        lB[iB] = '|'
        iB -= 1
        iC += 1

    elif list1 == 'B' and list2 == 'A':
        ti = lA.index('|')
        lA[ti] = lB[iB]
        lB[iB] = '|'
        iB -= 1
        iA += 1

    elif list1 == 'C' and list2 == 'A':
        ti = lA.index('|')
        lA[ti] = lC[iC]
        lC[iC] = '|'
        iC -= 1
        iA += 1

    elif list1 == 'C' and list2 == 'B':
        ti = lB.index('|')
        lB[ti] = lC[iC]
        lC[iC] = '|'
        iC -= 1
        iB += 1


n = int(input("Enter Input : "))
move(n, 'A', 'C', 'B', n)