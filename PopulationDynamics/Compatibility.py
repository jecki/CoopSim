# Compatibility

"""Provides code snipplets for ompatibility with older python versions.
"""

from functools import reduce

#-------------------------------------------------------------------------------
#
# define jython flag
#
#-------------------------------------------------------------------------------

try:
    import java
    jython = True
except:
    jython = False



#-------------------------------------------------------------------------------
#
# numerical arrays
#
#-------------------------------------------------------------------------------


try:
    from numpy import array, ravel, dot, concatenate, diagonal, \
        putmask, identity, asarray, zeros, all, any
    from numpy.random import uniform
    HAS_NUMERIC = True
except ImportError:
    from ArrayWrapper import array, ravel, dot, concatenate, diagonal, \
        asarray, zeros, all, any, uniform
    HAS_NUMERIC = False
