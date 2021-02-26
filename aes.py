from typing import NewType

state = NewType()

def expandKey(key: str):
    pass

def addRoundKey():
    pass

def subBytes(state: list) -> list:
    
    pass

def shiftRows():
    pass

def mixColumns():
    pass

""" """
def makeStateMatrix(m: str) -> list:
    pass

def initializeSBox() -> list:
    for i in range(255):
        n = format(i, '08b')
        
    pass

def gmul_inverse():
    pass

def multiplicateInGF(p1: int, p2: int):

    pass

def aes(message: str):
    state = makeStateMatrix(message)

    pass
