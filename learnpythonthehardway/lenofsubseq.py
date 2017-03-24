def lengestSubseqWord(s, d):
    """

    :rtype: object
    """
    rlt = ''
    cachedS = buildCachedS(s)
    for word in d:
        if isSubsqeunce(cachedS, word) and len(word) > len(rlt):
            rlt = word
    return rlt

def buildCachedS(s):
    cachedS = [{} for _ in s]
    l = len(s)
    for idx in range(0,l):
        c = s[idx]
        cachedS[idx][c] = idx
        for pos in range(idx):
            if c not in cachedS[pos]:
                cachedS[pos][c] = idx
            # if c already in cachedS[pos], it showed up before and we do nothing. 1point3acres.com/bbs
    return cachedS

def isSubsqeunce(cachedS, w):
    pos = 0
    for c in w:
        if c not in cachedS[pos]:
            return False
        pos = cachedS[pos][c]
    return True

d = ['abcadef', 'abc', 'cde']
s = 'tabcadefga'

print lengestSubseqWord(s,d)
