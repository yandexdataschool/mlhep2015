import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def preparePlot(xticks, yticks, figsize=(10.5, 6), hideLabels=False, gridColor='#999999',
                gridWidth=1.0):
    """Template for generating the plot layout."""
    plt.close()
    fig, ax = plt.subplots(figsize=figsize, facecolor='white', edgecolor='white')
    ax.axes.tick_params(labelcolor='#999999', labelsize='10')
    for axis, ticks in [(ax.get_xaxis(), xticks), (ax.get_yaxis(), yticks)]:
        axis.set_ticks_position('none')
        axis.set_ticks(ticks)
        axis.label.set_color('#999999')
        if hideLabels: axis.set_ticklabels([])
    plt.grid(color=gridColor, linewidth=gridWidth, linestyle='-')
    map(lambda position: ax.spines[position].set_visible(False), ['bottom', 'top', 'left', 'right'])
    return fig, ax

def draw_component(component):

    image = component.reshape(230, 202).T

    fig, ax = preparePlot(numpy.arange(0, 10, 1), numpy.arange(0, 10, 1), figsize=(9.0, 7.2), hideLabels=True)
    ax.grid(False)
    image = plt.imshow(image,interpolation='nearest', aspect='auto', cmap=cm.gray)
    plt.show()
# Adapted from python-thunder's Colorize.transform where cmap='polar'.
# Checkout the library at: https://github.com/thunder-project/thunder and
# http://thunder-project.org/
import numpy as np
def polarTransform(scale, img):
    """Convert points from cartesian to polar coordinates and map to colors."""
    from matplotlib.colors import hsv_to_rgb

    img = np.asarray(img)
    dims = img.shape

    phi = ((np.arctan2(-img[0], -img[1]) + np.pi/2) % (np.pi*2)) / (2 * np.pi)
    rho = np.sqrt(img[0]**2 + img[1]**2)
    saturation = np.ones((dims[1], dims[2]))

    out = hsv_to_rgb(np.dstack((phi, saturation, scale * rho)))

    return np.clip(out * scale, 0, 1)

def draw_two_components(*components):
    # Show the polar mapping from principal component coordinates to colors.
    components = [i.reshape(230, 202).T for i in components]

    imageOneScaled,imageTwoScaled =components
    x1AbsMax = np.max(np.abs(imageOneScaled))
    x2AbsMax = np.max(np.abs(imageTwoScaled))

    numOfPixels = 300
    x1Vals = np.arange(-x1AbsMax, x1AbsMax, (2 * x1AbsMax) / numOfPixels)
    x2Vals = np.arange(x2AbsMax, -x2AbsMax, -(2 * x2AbsMax) / numOfPixels)
    x2Vals.shape = (numOfPixels, 1)

    x1Data = np.tile(x1Vals, (numOfPixels, 1))
    x2Data = np.tile(x2Vals, (1, numOfPixels))

    polarMap = polarTransform(2.0, [x1Data, x2Data])

    gridRange = np.arange(0, numOfPixels + 25, 25)

    fig, ax = preparePlot(gridRange, gridRange, figsize=(9.0, 7.2), hideLabels=True)
    image = plt.imshow(polarMap, interpolation='nearest', aspect='auto')
    ax.set_xlabel('Principal component one'), ax.set_ylabel('Principal component two')
    gridMarks = (2 * gridRange / float(numOfPixels) - 1.0)
    x1Marks = x1AbsMax * gridMarks
    x2Marks = -x2AbsMax * gridMarks
    ax.get_xaxis().set_ticklabels(map(lambda x: '{0:.1f}'.format(x), x1Marks))
    ax.get_yaxis().set_ticklabels(map(lambda x: '{0:.1f}'.format(x), x2Marks))
    plt.show()
    # Try changing the first parameter to lower values

    
    
    # Use the same transformation on the image data
    # Try changing the first parameter to lower values
    intensities = (np.sum(np.abs(components),axis=0)/(x1AbsMax+x2AbsMax))**.5
    brainmap = polarTransform(2.0, components)*intensities.reshape(intensities.shape[0],intensities.shape[1],1)

    # generate layout and plot data
    fig, ax = preparePlot(np.arange(0, 10, 1), np.arange(0, 10, 1), figsize=(9.0, 7.2), hideLabels=True)
    ax.grid(False)
    image = plt.imshow(brainmap,interpolation='nearest', aspect='auto')
    plt.show()
    