import collections


# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the
# name.
#
# 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is
# 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3
# are formulas.
#
# Given a formula, output the count of all elements as a string in the following form: the first name (in sorted
# order), followed by its count (if that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
#
# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:
#
# All atom names consist of lowercase letters, except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

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
                    return counter  # must return

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
