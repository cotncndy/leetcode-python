class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        while True:
            collision, temp = False, []
            for i in xrange(len(asteroids)):
                if i > 0 and asteroids[i] < 0 and asteroids[i - 1] > 0:
                    collision, k, t = True, i, i - 1
                    while k < len(asteroids) and asteroids[k] < 0 and asteroids[t] + asteroids[k] > 0:
                        k = k + 1
                    while t >= 0 and k < len(asteroids) and asteroids[t] > 0 and asteroids[t] + asteroids[k] < 0:
                        t = t - 1
                    while t >= 0 and k < len(asteroids) and asteroids[k] < 0 and asteroids[t] > 0 \
                            and asteroids[t] + asteroids[k] == 0:
                        t, k = t - 1, k + 1
                    if t >= 0:
                        temp = asteroids[0:t + 1]
                    if k < len(asteroids):
                        temp += asteroids[k:]
            if collision:
                asteroids = temp
            else:
                return asteroids


        return asteroids

    def asteroidCollision2(self, asteroids):
        res = []
        for k in asteroids:
            if len(res) == 0 or k >= 0:
                res.append(k)
            elif k + res[-1] > 0:
                continue
            elif k + res[-1] < 0:
                while len(res) > 0 and res[-1] > 0 and k + res[-1] < 0:
                    res.pop()
                if len(res) == 0 or res[-1] < 0 == 0:
                    res.append(k)
                elif res[-1] + k > 0:
                    continue
                elif res[-1] + k == 0:
                    res.pop()
                    continue
                else:
                    res.append(k)
            else:  # k + res[-1] == 0
                res.pop()
                continue

        return res


if __name__ == '__main__':
    print Solution().asteroidCollision2([5, 10, -5])
    print Solution().asteroidCollision2([8, -8])
    print Solution().asteroidCollision2([10, 2, -5])
    print Solution().asteroidCollision2([-2, 1, -2, -2])
    print Solution().asteroidCollision2([-2, 2, -1, -2])
    print Solution().asteroidCollision2([-2, 1, -1, 2])
    print Solution().asteroidCollision2([1, -2, -2, -2])
