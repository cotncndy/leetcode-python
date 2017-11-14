import collections


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        map, ele, level = collections.orderedDict(), "", 0

        for i in xrange(len(formula)):
            if formula[i].isdigit():
                map[ele], ele = (level, map[ele][1] * (ord(formula[i]) - ord('0'))), ""
            elif formula[i].islower():
                ele.append(formula[i])
            elif formula[i].isupper():
                if ele:
                    map[ele], ele = (level, 1), ""
                else:
                    ele.append(formula[i])
            elif formula[i] == '(':
                if not formula[i].isdigit():
                    map[ele] = 1
                ele = ""
                stack.append(formula[i])
