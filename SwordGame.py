class Solution():
    def __init__(self):
        tc = int(input())
        t = 1

        while tc > 0:
            n, k, s = map(int, input().split())

            mins = k
            case1 = mins + n
            case2 = mins + (k-s) +  (n-s)

            if k < s:
                print("Case #" + str(t) + ": " + str(n))
            elif case1 < case2:
                print("Case #" + str(t) + ": " + str(case1))
            elif case2 < case1:
                print("Case #" + str(t) + ": " + str(case2))


            tc -= 1
            t += 1

soln = Solution()

    