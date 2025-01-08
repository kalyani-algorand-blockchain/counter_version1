from algopy import ARC4Contract, UInt64
from algopy.arc4 import abimethod

class Assignment(ARC4Contract):
    @abimethod()
    def increment(self, a : UInt64) -> UInt64:
        return a + 1
    @abimethod()
    def decrement(self, a : UInt64) -> UInt64:
        return a - 1
    
