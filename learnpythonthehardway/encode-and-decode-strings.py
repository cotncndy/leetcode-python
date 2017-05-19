# Time:  O(n)
# Space: O(1)

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encode_str = ""
        for s in strs:
            # >>> "%0*x" % (8,3)
            # '00000003'
            # >>> "%0*x" % (8,13)
            # '0000000d'
            # >>> "%0*x" % (8,16)
            # '00000010'
            # >>> "%0*x" % (8,32)
            # '00000020'
            # >>> "%0*x" % (16,32)
            # '0000000000000020'

            # http://stackoverflow.com/questions/5661725/format-ints-into-string-of-hex
            # encode_str += "%0*x" % (8, len(s)) + s
            encode_str += "%08x" % (len(s)) + s

        return encode_str

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i, strs = 0, []
        while i < len(s):
            l = int(s[i:i + 8], 16)
            strs.append(s[i + 8:i + 8 + l])
            i = i + 8 + l

        return strs

    def encode2(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encode_str = ""
        for s in strs:
            encode_str += str(len(s)) + "/" + s

        return encode_str

    def decode2(self, str):
        i, j, strs = 0, 0, []
        j = str.find("/", i)
        while j != -1:
            l = int(s[i:j])
            i = j + 1 + l
            strs.append(s[j + 1: i])
            j = str.find("/", i)

        return strs

if __name__ == "__main__":
    strs = ["a", "ab", "abc"]
    s = Codec().encode2(strs)
    print s
    print Codec().decode2(s)
