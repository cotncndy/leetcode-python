def isValid(s):
    decodeCount = [0] # syntax hack to make this variable accessible in dfs
                      # it does not need to be a list

    def dfs(s):
        if s == '':
            decodeCount[0] += 1 # if reaches end, it there is a decoding way
        if not s[0].isdigit():
            return
        count = 0
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c.isdigt():
                # action 1 take current as a count
                count = count * 10 + int(c)
                dfs(s[idx+count:]) # depth first search along this action

                # ation 2 continue adding
                count = count * 10 + int(c)
                idx += 1

            else:
                # if not integer, we cannot move on
                break

    dfs(s)

    # return True if and only if there is only one way of decoding
    return decodeCount[0] == 1


print isValid('3aaa2bb3ccc');
print isValid('135small6bosses')
