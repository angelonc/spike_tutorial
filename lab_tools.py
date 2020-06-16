"""LabTools Module
Contains commonly used functions for analysis."""

def ismember(A,B):
    """replaces values in A with the index of their matches in B.

    (ie. if A = [1 1 1 2 2] and B = [2 1], res = ismember(A,B) returns [2 2 2 1 1]
    
    Arguments:
    A -- array to be modified
    B -- modifier index
    
    Returns:
    res -- array with the positional index where B == A replacing values in A where A == B
    """

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


def makePSTH(spikes,triggers,edges):
    """makes a PSTH given spikes, event triggers, and temporal bin edges.
    
    """
    
    # preallocate
    raster = []
    trials = []
    psth = np.empty([len(triggers),len(edges)-1])

    for i,trig in enumerate(triggers):

        # zero spikes
        spks = spikes - trig

        # spike histogram appended to PSTH
        psth[i,:],_ = np.histogram(spks,bins=edges)
        psth[i,:] = psth[i,:] / np.diff(edges).mean()

        # extend raster (using only spikes within each trial range)
        spks = spks[(spks>edges[0]) & (spks<edges[-1])]
        raster.extend(spks)
        trials.extend(np.ones(len(spks))*(i+1))
    
    return [psth,raster,trials]