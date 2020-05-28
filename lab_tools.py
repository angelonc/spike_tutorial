"""LabTools Module
Contains commonly used functions for analysis."""

def ismember(A,B):
    """replaces values in A with the index of their matches in B"""

    # This function takes two arrays, A and B, and checks for matches.
    # Where A matches B, those values of A are replaced by their index in B.
    # This index is returned in res.

    # convert both A and B to np arrays
    A = np.asarray(A).astype(int)
    B = np.asarray(B).astype(int)

    # preallocate res
    res = np.zeros(A.shape)

    # loop through unique values of A
    for i in np.unique(A):

        # where A == i, replace them with the index of i in B
        res[A == i] = np.argwhere(B == i).squeeze()

    return res
