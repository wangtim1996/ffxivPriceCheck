
from marketboard import *

def test_bicolor():
    retval = get_best_bicolor()
    assert(retval)

def test_fail():
    assert(False)
