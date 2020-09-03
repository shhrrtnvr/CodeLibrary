def KMPSearch(lps, pat, txt):
    M, N = len(pat), len(txt)
    j = 0


    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat):
    M = len(pat)
    lps = [0] * M
    l = 0  # length of the previous longest prefix suffix
    i = 1
    while i < M:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"

    lps = computeLPSArray(pat)

    KMPSearch(lps, pat, txt)
