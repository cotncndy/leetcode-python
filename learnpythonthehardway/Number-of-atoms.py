import collections


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        def parse():  # return collections.Counter
            counter = collections.Counter()
            while self.i < len(formula):
                if formula[self.i] == '(':
                    self.i += 1
                    for name, v in parse().items():  # knowledge how to loop collections.counter
                        counter[name] += v
                elif formula[self.i] == ')':
                    self.i += 1  # bypass the ')', go to the next one
                    i_start = self.i
                    while self.i < len(formula) and formula[self.i].isdigit():  # search all digital
                        self.i += 1
                    times = int(formula[i_start:self.i] or 1)
                    for name, v in counter.items():
                        counter[name] = v * times
                    return counter

                else:
                    i_start = self.i  # i_start must be uppercase  because the code below bypassed all lowercase and
                    # digital
                    self.i += 1
                    while self.i < len(formula) and formula[self.i].islower():  # search all lowercase
                        self.i += 1
                    temp = formula[i_start:self.i]
                    i_start = self.i
                    while self.i < len(formula) and formula[self.i].isdigit():  # search all digital
                        self.i += 1
                    counter[temp] += int(formula[i_start:self.i] or 1)  # knowledge , a concise way

            return counter

        self.i, ans = 0, []
        count = parse()
        for name in sorted(count):  # knowledge how to sort items
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)

    def countOfAtoms2(self, formula):
        i, st = 0, []
        st.append(collections.Counter())
        while i < len(formula):
            if formula[i] == '(':
                st.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                counter = st.pop()
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                n = int(formula[i_start:i] or 1)
                for name, v in counter.items():
                    st[-1][name] += v * n
            else:
                i_start = i  # i_start must be uppercase  because the code below bypassed all lowercase and
                # digital
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1

                temp = formula[i_start:i]
                i_start = i
                while i < len(formula) and formula[i].isdigit():  # search all digital
                    i += 1
                st[-1][temp] += int(formula[i_start:i] or 1)  # knowledge , a concise way

        ans = []
        for name in sorted(st[-1]):  # knowledge how to sort items
            ans.append(name)
            multiplicity = st[-1][name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)


if __name__ == '__main__':
    print Solution().countOfAtoms("Mg(OH)2")
    print Solution().countOfAtoms2("Mg(OH)2")
    print Solution().countOfAtoms("H2O")
    print Solution().countOfAtoms2("H2O")
    print Solution().countOfAtoms("K4(ON(SO3)2)2")
    print Solution().countOfAtoms2("K4(ON(SO3)2)2")
