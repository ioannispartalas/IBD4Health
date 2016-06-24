import pandas as pd
import matplotlib.pyplot as plt
import cPickle as pickle

__data = None
__colidx = None
features = None
with open("ibd4health_diabetes.pkl", 'r') as f:
    pkl = pickle.load(f)
    __data = pkl['data']
    features = pkl['features']
    __colidx = dict([(k, v) for v, k in enumerate(features)])

def column(name, data=None):
    """Returns the data column with given name."""
    if data:
        return data[:, __colidx[name]]
    else:
        return __data[:, __colidx[name]]

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
    fig = plt.figure()
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
    return fig
