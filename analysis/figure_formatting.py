import scipy.interpolate as interpolate
import matplotlib
import matplotlib.image as image
from matplotlib import rc, rcParams
import numpy as np

def get_ax_size(fig, ax):
    '''
    Returns the size of a given axis in pixels
    
    Args:
       fig (matplotlib figure)
       ax (matplotlib axes)
    
    '''
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    return width, height

def place_image(fig, ax, image_name, xsize, xpos, ypos, zorder=10):
    '''
    Places an image on a given axes whilst maintaining its aspect ratio
    
    Args:
        fig (matplotlib figure)
        ax (matplotlib axes)
        image_name (string): name of image to place on axes
        xsize(float): size of the x-dimension of object given as fraction of the axes length
        xpos(float): x-coordinate of image given as fraction of axes
        ypos(float): y-coordinate of image given as fraction of axes
    
    '''
    im = image.imread(image_name)
    
    xrange=ax.get_xlim()[1]-ax.get_xlim()[0]
    yrange=ax.get_ylim()[1]-ax.get_ylim()[0]

    ysize=(im.shape[0]/im.shape[1])*(xsize*get_ax_size(fig,ax)[0])/get_ax_size(fig,ax)[1]

    xsize *= xrange
    ysize *= yrange
    xpos = (xpos*xrange) + ax.get_xlim()[0]
    ypos = (ypos*yrange) + ax.get_ylim()[0]

    ax.imshow(im,aspect='auto',extent=(xpos,xpos+xsize,ypos,ypos+ysize),interpolation='none', zorder=zorder )

def interpolate_df(df,xrange,dx):
    '''
    Interpolates data in a panda dataframe
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       xrange(int): number of data points
       dx(float): interval for interpolated data outputted
    
    Returns:
       numpy array contating interpolated x,y data'''
    points=np.array( [(x[0],value) for x,value in np.ndenumerate(df.values)])
    x=points[:,0]
    y=points[:,1]
    spline = interpolate.splrep(points[:,0],y=points[:,1],s=0)
    xnew = np.arange(xrange[0],xrange[1],dx)
    ynew = interpolate.splev(xnew,spline,der=0)
    xnew=x    #  remove these lines to get spline
    ynew=y    #  not linear
    return xnew,ynew

def get_y_limits(size,zero_point):
    '''
    Interpolates data in a panda dataframe
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       xrange(int): number of data points
       dx(float): interval for interpolated data outputted
    
    Returns:
       numpy array contating interpolated x,y data'''
    y_top= size*(1.0-zero_point)
    y_bottom= -size*(zero_point)
    return y_bottom,y_top

def get_df_range(df,key):
    '''
    Filters a panda dataframe by key and returns its range
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       key(string): key of data to filter
    
    Returns:
       range of data (float)'''
    Channels = df.filter(regex=key)   
    return Channels.values.max()-Channels.values.min()

def get_df_max(df,key):
    '''
    Filters a panda dataframe by key and returns its max value
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       key(string): key of data to filter
    
    Returns:
       max of data (float)'''
    Channels = df.filter(regex=key)   
    return Channels.values.max()

def get_df_min(df,key):
    '''
    Filters a panda dataframe by key and returns its min
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       key(string): key of data to filter
    
    Returns:
       min of data (float)'''
    Channels = df.filter(regex=key)
    return Channels.values.min()

def get_y_range(df,key,dec_f,pad):
    '''
    Get a suitable range for the y-axis to hold data in a panda dataframe
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       key(string): key of data to filter
       dec_f(integer): number of digits to round to
       pad(float): padding either side
    
    Returns:
       suitable range of for y-data (float)'''
    return round(get_df_range(df,key),dec_f)+2.0*pad  

def get_y_axis_limits(df,key,zero_point,dec_f,pad):
    '''
    Set y-limits to hold a panda dataframe given a zero-point
    
    Args:
       df(panda dataframe): dataframe containing data to be interpolated
       key(string): key of data to filter
       zero_point(float): where to zero on y-axis
       dec_f(integer): number of digits to round to
       pad(float): padding either side
    
    Returns:
       y-limits for matplotlib axes (float)'''
    
    yrange=get_y_range(df,key,dec_f,pad)
    ymax=get_df_max(df,key)
    ymin=get_df_min(df,key)
        
    urange = max(ymax,(1.0-zero_point)*yrange)
    lrange = min(ymin,-(zero_point*yrange))
    
    total_range = round(max(urange/(1-zero_point),(-lrange/zero_point)),1)+(2*pad)
                              
    return get_y_limits(total_range,zero_point)

def line(x, m, c):
    return m * x + c

# Global formatting options

matplotlib.style.use('ggplot')

nearly_black = '#161616'
light_grey = '#EEEEEE'
lighter_grey = '#F5F5F5'

colours = { 'U':  '#62606f',
            'LM': '#f46d43',
            'LT': '#f2c23e' }

symbol = { 0.25: 'co',
           0.50:  'v' }

fontsize=16

master_formatting = { 'axes.formatter.limits': (-3,3),
                      'xtick.major.pad': 7,
                      'ytick.major.pad': 7,
                      'ytick.color': nearly_black,
                      'xtick.color': nearly_black,
                      'axes.labelcolor': nearly_black,
                      'legend.facecolor': light_grey,
                      'pdf.fonttype': 42,
                      'ps.fonttype': 42,
                      'mathtext.fontset': 'custom',
                      'font.size': fontsize,
                      'font.family': 'serif',
                      'mathtext.rm': 'Minion Pro',
                      'mathtext.it': 'Minion Pro:italic',
                      'mathtext.bf': 'Minion Pro:bold',
                      'savefig.bbox':'tight',
                      'axes.facecolor': lighter_grey,
                      'axes.labelpad': 10.0,
                      'axes.labelsize': fontsize,
                      'axes.titlepad': 25,
                      'axes.spines.top': False,
                      'axes.spines.left': False,
                      'axes.spines.right': False,
                      'axes.spines.bottom': False,
                      'lines.markersize': 5.0,
                      'lines.markeredgewidth': 0.0,
                      'lines.linewidth': 1.5,
                      'lines.scale_dashes': False }

def set_rcParams( formatting ):
    for k, v in formatting.items():
        rcParams[k] = v
