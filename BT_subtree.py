class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

def  equal(t1, t2):
    if t1 is None or t2 is None:
        return (t1 is None) and (t2 is None);
    else:
        return t1.value == t2.value and equal(t1.left, t2.left) and equal(t1.right, t2.right)

def isSubtree(S, T):
    if T is None:
        return True
    if S is None:
        return False
    if equal(S, T):
        return True
    return isSubtree(S.left, T) or isSubtree(S.right,T)
