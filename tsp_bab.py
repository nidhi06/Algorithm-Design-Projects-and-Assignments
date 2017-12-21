import time

INF = 100000000

best_cost = 0

def reduce(size, w, row, col, rowred, colred):
    rvalue = 0
    for i in range(size):
        temp = INF
        for j in range(size):
            temp = min(temp, w[row[i]][col[j]])
        if temp > 0:
            for j in range(size):
                if w[row[i]][col[j]] < INF:
                    w[row[i]][col[j]] -= temp
            rvalue += temp
        rowred[i] = temp
    for j in range(size):
        temp = INF
        for i in range(size):
            temp = min(temp, w[row[i]][col[j]])
        if temp > 0:
            for i in range(size):
                if w[row[i]][col[j]] < INF:
                    w[row[i]][col[j]] -= temp
            rvalue += temp
        colred[j] = temp
    return rvalue


def bestEdge(size, w, row, col):
    mosti = -INF
    ri = 0
    ci = 0
    for i in range(size):
        for j in range(size):
            if not w[row[i]][col[j]]:
                minrowwelt = INF
                zeroes = 0
                for k in range(size):
                    if not w[row[i]][col[k]]:
                        zeroes += 1
                    else:
                        minrowwelt = min(minrowwelt, w[row[i]][col[k]])
                if zeroes > 1: minrowwelt = 0
                mincolwelt = INF
                zeroes = 0
                for k in range(size):
                    if not w[row[k]][col[j]]:
                        zeroes += 1
                    else:
                        mincolwelt = min(mincolwelt, w[row[k]][col[j]])
                if zeroes > 1: mincolwelt = 0
                if minrowwelt + mincolwelt > mosti:
                    mosti = minrowwelt + mincolwelt
                    ri = i
                    ci = j
    return mosti, ri, ci


def explore(n, w, edges, cost, row, col, best, fwdptr, backptr):
    global best_cost

    colred = [0 for _ in range(n)]
    rowred = [0 for _ in range(n)]
    size = n - edges
    cost += reduce(size, w, row, col, rowred, colred)
    if cost < best_cost:
        if edges == n - 2:
            for i in range(n): best[i] = fwdptr[i]
            if w[row[0]][col[0]] >= INF:
                avoid = 0
            else:
                avoid = 1
            best[row[0]] = col[1 - avoid]
            best[row[1]] = col[avoid]
            best_cost = cost
        else:
            mostv, rv, cv = bestEdge(size, w, row, col)
            lowerbound = cost + mostv
            fwdptr[row[rv]] = col[cv]
            backptr[col[cv]] = row[rv]
            last = col[cv]
            while fwdptr[last] != INF: last = fwdptr[last]
            first = row[rv]
            while backptr[first] != INF: first = backptr[first]
            colrowval = w[last][first]
            w[last][first] = INF
            newcol = [INF for _ in range(size)]
            newrow = [INF for _ in range(size)]
            for i in range(rv): newrow[i] = row[i]
            for i in range(rv, size - 1): newrow[i] = row[i + 1]
            for i in range(cv): newcol[i] = col[i]
            for i in range(cv, size - 1): newcol[i] = col[i + 1]
            explore(n, w, edges + 1, cost, newrow, newcol, best, fwdptr, backptr)
            w[last][first] = colrowval
            backptr[col[cv]] = INF
            fwdptr[row[rv]] = INF
            if lowerbound < best_cost:
                w[row[rv]][col[cv]] = INF
                explore(n, w, edges, cost, row, col, best, fwdptr, backptr)
                w[row[rv]][col[cv]] = 0

    for i in range(size):
        for j in range(size):
            w[row[i]][col[j]] = w[row[i]][col[j]] + rowred[i] + colred[j]


def atsp(w):
    global best_cost
    size = len(w)
    col = [i for i in range(size)]
    row = [i for i in range(size)]
    best = [0 for _ in range(size)]
    route = [0 for _ in range(size)]
    fwdptr = [INF for _ in range(size)]
    backptr = [INF for _ in range(size)]
    best_cost = INF

    explore(size, w, 0, 0, row, col, best, fwdptr, backptr)

    index = 0
    for i in range(size):
        route[i] = index
        index = best[index]
    index = []
    cost = 0

    for i in range(size):
        if i != size - 1:
            src = route[i]
            dst = route[i + 1]
        else:
            src = route[i]
            dst = 0
        cost += w[src][dst]
        index.append([src, dst])
    return cost, index


def main():
    # matrix

    m = [
        [INF, 514, 230, 92, 172, 201, 320, 205, 329, 285, 404, 128, 352, 357, 190, 269, 484, 237, 567, 209, 413, 404,
         333, 480, 371, 175, 470, 281, 423, 328],
        [452, INF, 359, 410, 450, 401, 315, 293, 244, 200, 275, 446, 469, 143, 278, 362, 399, 344, 544, 644, 335, 381,
         248, 457, 626, 375, 551, 258, 397, 305],
        [414, 360, INF, 90, 170, 42, 90, 46, 282, 238, 186, 126, 320, 198, 31, 267, 437, 190, 358, 623, 246, 345, 286,
         271, 267, 16, 326, 222, 421, 119],
        [324, 427, 269, INF, 80, 109, 359, 113, 263, 233, 312, 36, 260, 265, 98, 177, 418, 257, 475, 533, 321, 312, 281,
         388, 279, 83, 378, 189, 331, 236],
        [244, 382, 312, 226, INF, 335, 402, 246, 197, 153, 334, 262, 486, 466, 231, 315, 352, 297, 670, 453, 241, 538,
         201, 583, 505, 309, 298, 415, 350, 431],
        [448, 318, 355, 216, 268, INF, 445, 111, 240, 196, 288, 252, 385, 156, 96, 358, 395, 148, 691, 640, 348, 528,
         244, 455, 373, 299, 566, 405, 393, 452],
        [330, 437, 126, 216, 280, 119, INF, 123, 206, 315, 312, 252, 348, 275, 108, 324, 361, 267, 268, 539, 372, 255,
         242, 181, 393, 93, 236, 132, 478, 29],
        [495, 557, 521, 539, 313, 563, 469, INF, 406, 444, 543, 575, 274, 700, 440, 524, 442, 506, 729, 633, 554, 716,
         442, 642, 788, 537, 611, 593, 641, 490],
        [208, 256, 115, 168, 206, 157, 205, 49, INF, 148, 137, 204, 323, 313, 34, 118, 155, 100, 473, 417, 197, 460, 36,
         386, 382, 131, 441, 337, 272, 234],
        [252, 229, 159, 212, 250, 201, 249, 93, 44, INF, 181, 248, 367, 357, 78, 162, 199, 144, 517, 444, 241, 398, 48,
         430, 426, 175, 485, 275, 197, 278],
        [534, 568, 363, 453, 411, 250, 237, 254, 326, 344, INF, 225, 449, 406, 239, 366, 481, 398, 505, 547, 60, 375,
         362, 418, 623, 224, 473, 252, 520, 266],
        [445, 507, 334, 389, 469, 332, 393, 336, 413, 369, 276, INF, 224, 488, 321, 141, 392, 321, 659, 583, 336, 496,
         417, 572, 601, 306, 629, 373, 295, 420],
        [221, 283, 313, 313, 393, 314, 195, 263, 214, 170, 351, 349, INF, 426, 248, 325, 168, 314, 455, 359, 411, 442,
         218, 368, 580, 288, 431, 319, 367, 216],
        [309, 286, 216, 269, 307, 258, 306, 150, 101, 57, 132, 305, 326, INF, 135, 219, 256, 201, 574, 501, 192, 455,
         105, 487, 483, 232, 542, 332, 254, 335],
        [416, 554, 484, 398, 172, 507, 484, 15, 369, 325, 506, 434, 289, 638, INF, 487, 457, 469, 717, 625, 413, 554,
         373, 359, 677, 481, 470, 431, 522, 478],
        [514, 509, 193, 283, 352, 191, 252, 195, 306, 387, 379, 319, 469, 347, 180, INF, 461, 339, 518, 723, 249, 355,
         342, 431, 460, 165, 488, 232, 154, 279],
        [53, 115, 278, 145, 225, 254, 368, 212, 163, 119, 300, 181, 405, 258, 197, 281, INF, 263, 620, 262, 360, 457,
         167, 533, 424, 228, 523, 334, 316, 381],
        [300, 277, 207, 68, 148, 177, 297, 141, 92, 48, 229, 104, 328, 333, 126, 210, 247, INF, 543, 492, 289, 380, 96,
         456, 347, 151, 446, 257, 245, 304],
        [758, 471, 620, 710, 754, 593, 710, 597, 550, 671, 687, 746, 571, 614, 582, 668, 705, 650, INF, 930, 747, 599,
         586, 404, 887, 567, 915, 476, 822, 523],
        [39, 434, 269, 131, 211, 240, 359, 227, 178, 324, 315, 167, 391, 396, 212, 296, 333, 276, 452, INF, 375, 439,
         214, 365, 410, 214, 509, 316, 450, 213],
        [526, 513, 443, 496, 534, 485, 533, 377, 328, 284, 441, 165, 389, 641, 362, 306, 483, 428, 698, 487, INF, 535,
         332, 611, 710, 459, 769, 412, 460, 459],
        [784, 654, 691, 552, 604, 336, 781, 447, 576, 532, 624, 588, 721, 492, 432, 694, 731, 484, 1027, 976, 684, INF,
         580, 791, 709, 635, 902, 741, 729, 788],
        [435, 220, 576, 527, 607, 569, 450, 513, 464, 420, 495, 563, 689, 363, 498, 582, 619, 564, 718, 396, 555, 601,
         INF, 631, 806, 543, 686, 478, 617, 479],
        [354, 402, 216, 306, 350, 189, 306, 193, 146, 294, 283, 342, 167, 345, 178, 264, 301, 246, 358, 526, 343, 195,
         182, INF, 483, 163, 511, 72, 418, 119],
        [311, 288, 218, 79, 159, 188, 308, 152, 103, 59, 240, 115, 113, 344, 137, 221, 258, 11, 554, 472, 300, 391, 107,
         462, INF, 162, 457, 268, 256, 315],
        [431, 344, 186, 242, 187, 26, 276, 30, 266, 222, 314, 278, 304, 182, 15, 384, 421, 174, 544, 640, 374, 531, 270,
         374, 399, INF, 348, 408, 419, 305],
        [477, 454, 384, 437, 475, 426, 474, 318, 269, 225, 300, 473, 494, 168, 303, 387, 424, 369, 742, 669, 360, 623,
         273, 655, 651, 400, INF, 500, 422, 503],
        [282, 330, 144, 234, 280, 186, 234, 123, 74, 222, 211, 270, 366, 342, 108, 192, 229, 174, 286, 491, 271, 123,
         110, 199, 411, 160, 470, INF, 346, 47],
        [360, 399, 39, 129, 209, 81, 98, 85, 152, 277, 225, 165, 359, 237, 70, 270, 307, 229, 364, 569, 95, 201, 188,
         277, 306, 55, 334, 78, INF, 125],
        [301, 433, 97, 187, 267, 139, 187, 143, 177, 325, 283, 223, 319, 295, 128, 295, 332, 277, 239, 510, 343, 226,
         213, 152, 364, 113, 423, 103, 449, INF]
    ]

    start_time = time.time()
    cost, path = atsp(m)
    print ("Cost = ", cost)
    print ("Path = ", path)
    print ("Time (s)", time.time() - start_time)

if __name__ == "__main__":
    main()