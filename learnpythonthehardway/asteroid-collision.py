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


if __name__ == '__main__':
    print Solution().asteroidCollision([5, 10, -5])
    print Solution().asteroidCollision([8, -8])
    print Solution().asteroidCollision([10, 2, -5])
    print Solution().asteroidCollision([-2, 1, -2, -2])
    print Solution().asteroidCollision([-2, 2, -1, -2])
    print Solution().asteroidCollision([-2, 1, -1, 2])
