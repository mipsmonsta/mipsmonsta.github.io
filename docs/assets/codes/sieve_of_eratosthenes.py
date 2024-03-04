import timeit

class Solution():
    def primeNumbersUpTo(self, n): # inclusive of n
        primeCandidates = set([i for i in range(2, n+1)])

        for i in range(2, n+1):

            # i is not prime
            if i not in primeCandidates:
                continue

            for multiple in range(i*i, n+1, i):
                if multiple in primeCandidates:
                    # sieved out
                    primeCandidates.remove(multiple)
        
        return list(primeCandidates)

s = Solution()
n = 100
print(s.primeNumbersUpTo(n))

s = Solution()
n = 1000
print(s.primeNumbersUpTo(n))

print(timeit.timeit(f's.primeNumbersUpTo({n})', number=10000, globals=globals()))
