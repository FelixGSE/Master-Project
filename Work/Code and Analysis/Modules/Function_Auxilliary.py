####################################################################################################

####################################################################################################

#---------------------------------------------------------------------------------------------------
# Permutation functions
#---------------------------------------------------------------------------------------------------


def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

"""
for p in permute([1, 2, 3, 4]):
    print p
"""

#---------------------------------------------------------------------------------------------------
# Repeat function
#---------------------------------------------------------------------------------------------------

def rep( item, n ):
    new = []
    for i in range(n):
        new.append(item)
    return new

#---------------------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------------------



####################################################################################################

####################################################################################################