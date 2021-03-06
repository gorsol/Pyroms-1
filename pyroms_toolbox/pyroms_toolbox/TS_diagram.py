import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import cm
import pyroms
import pyroms_toolbox


def TS_diagram(temp, salt, depth=None, dens_lev=None, fmt='%2.2f', pal=cm.spectral, \
               outfile=None):

    if dens_lev is None:
        dens_lev = np.arange(10,36,1)

    if depth is None: 
        diag = plt.scatter(salt.flatten(), temp.flatten(), s=2, edgecolors='none')
    else:
        diag = plt.scatter(salt.flatten(), temp.flatten(), c=depth.flatten(), \
                    s=2, edgecolors='none', cmap=pal)
        plt.colorbar(diag, shrink=0.9, aspect=40)

    ax = plt.gca()
    slim = ax.get_xlim()
    tlim = ax.get_ylim()
    s = np.arange(slim[0],slim[1]+0.01,0.01)
    t = np.arange(tlim[0],tlim[1]+0.1,0.1)
    T, S = np.meshgrid(t,s)
    density = pyroms_toolbox.seawater.dens(S,T) - 1000.
    dc = plt.contour(s,t,density.T, levels=dens_lev, colors='k')
    plt.clabel(dc, inline=1, fontsize=10, fmt=fmt)
    
    if outfile is not None:
        if outfile.find('.png') != -1 or outfile.find('.svg') != -1 or \
           outfile.find('.eps') != -1:
            print 'Write figure to file', outfile
            plt.savefig(outfile, dpi=200, facecolor='w', edgecolor='w', \
                        orientation='portrait')
        else:
            print 'Unrecognized file extension. Please use .png, .svg or .eps file extension.'
