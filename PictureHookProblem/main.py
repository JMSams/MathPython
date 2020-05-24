import unittest

class Tester(unittest.TestCase):
    def testCanceling(self):
        A  = Hook('A', False)
        Ai = Hook('A', True)
        B  = Hook('B', False)
        Bi = Hook('B', True)

        self.assertTrue(A.DoesCancel(Ai))
        self.assertTrue(Ai.DoesCancel(A))
        self.assertTrue(B.DoesCancel(Bi))
        self.assertTrue(Bi.DoesCancel(B))

        self.assertFalse(A.DoesCancel(A))
        self.assertFalse(A.DoesCancel(Bi))
        self.assertFalse(Bi.DoesCancel(Ai))

class Hook:
    def __init__(self, n, i):
        self.n = n
        self.inverse = i
    
    def DoesCancel(self, other):
        return ((self.n == other.n) and (self.inverse != other.inverse))

class HookSet:
    def __init__(self, hooks):
        self.hooks = hooks
    
    def CancelOut(self):
        

if __name__ == '__main__':
    unittest.main()