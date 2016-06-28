import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

npdata = np.load('ibd4health_diabetes.npz')
data = npdata['data']
__data = data
features = npdata['features']
labels = npdata['labels']
colidx = dict([(k.decode("utf-8"), v) for v, k in enumerate(features)])
npdata.close()

def column(name, data=None):
    """Returns the data column with given name."""
    if data is None:
        data = __data
    return data[:, colidx[name]]

def correlation(cola, colb, data=None):
    """Computes the correlation between columns cola and colb.

    :param cola: name of the first column to use
    :type cola: string
    :param colb: name of the second column to use
    :type colb: string
    :returns: correlation between cola and colb

    """
    dfa = pd.DataFrame(column(cola, data))
    dfb = pd.DataFrame(column(colb, data))
    return dfa.corrwith(dfb)

def histogram(col, *args):
    if args:
        cols = [col]
        for i in args:
            cols.append(i)
        xs = map(column, cols)
    else:
        cols = col
        xs = column(col)

    print(cols)
    plt.hist(xs, histtype='step', bins=50)
    plt.legend(cols[::-1])
