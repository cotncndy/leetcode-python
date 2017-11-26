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
                    collision = True
                    if asteroids[i - 1] + asteroids[i] > 0:
                        temp = asteroids[0:i] + asteroids[i + 1:]
                        if i + 1 < len(asteroids):
                            temp += asteroids[i + 1:]
                    elif asteroids[i - 1] + asteroids[i] < 0:
                        temp = asteroids[0:i - 1] + [asteroids[i]]
                        if i + 1 < len(asteroids):
                            temp += asteroids[i + 1:]
                    else:
                        temp = asteroids[0:i - 1] + asteroids[i + 1:]
            if collision:
                asteroids = temp
            else:
                return asteroids


        return asteroids


if __name__ == '__main__':
    # print Solution().asteroidCollision([5, 10, -5])
    # print Solution().asteroidCollision([8,-8])
    # print Solution().asteroidCollision([10, 2, -5])
    print Solution().asteroidCollision([-2, 1, -2, -2])
