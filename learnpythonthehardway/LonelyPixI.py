class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        w,h=len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in xrange(w):
            for y in xrange(h):
                if picture[x][y] == 'B' :
                    rows[x] += 1
                    cols[y] += 1

        res = 0
        for x in xrange(w) :
            for y in xrange(h):
                if picture[x][y] == 'B' and rows[x] == 1 and cols[y] == 1:
                    res += 1


        return res

if __name__=="__main__":
    print Solution().findLonelyPixel(['WWB','WBW','BWW'])
    print Solution().findLonelyPixel(["WWB","WBW","BWW"])




