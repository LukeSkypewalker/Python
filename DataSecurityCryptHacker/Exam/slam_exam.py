import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
# np.set_printoptions(threshold=np.nan)

# def convert2xy(frame, fov, min_dist, dtype=np.float64):
#     """Converts scan data to list of XY points descarding values with distances
#     less than `min_dist`.
#
#     Examples
#     --------
#     >>> scan = np.load('test_data/data.npy')
#     >>> scan.shape
#     (250, 682)
#     >>> points0 = convert2xy(scan[0], 240, 20)
#     >>> points10 = convert2xy(scan[10], 240, 20)
#     >>> points100 = convert2xy(scan[100], 240, 20)
#
#     #ASK
#     Plotting points:
#     >>> _ = plt.title('convert2xy')
#     >>> _ = plt.plot(*points0.T, label='0', ls='', marker= '.')
#     >>> _ = plt.plot(*points10.T, label='10', ls='', marker= '.')
#     >>> _ = plt.plot(*points100.T, label='10', ls='', marker= '.')
#     >>> _ = plt.legend()
#     >>> plt.show()
#
#     Comparing with etalon element-wise:
#     >>> (points0 == np.load('test_data/points0.npy')).all()
#     True
#     >>> (points10 == np.load('test_data/points10.npy')).all()
#     True
#     >>> (points100 == np.load('test_data/points100.npy')).all()
#     True
#
#     Parameters
#     ----------
#     scan : array-like
#         List of scan measurments in mm
#     fov : scalar
#         Sensor Field Of View in degrees
#     min_dist : scalar
#         Minimal distance of measurment in mm for filtering out values
#     dtype : data-type, optional
#         The desired data-type for the output array, e.g., numpy.int8.
#         Default is numpy.float64
#
#     Returns
#     -------
#     points : ndarray
#         List of XY points
#     """
#     frame = frame[frame > min_dist]
#     angles = np.radians(np.linspace(-120, 120, len(frame)))
#     points = np.zeros((len(frame), 2))
#     points[:, 0] = frame * np.cos(angles)
#     points[:, 1] = frame * np.sin(angles)
#
#     return points
#
#
# def rot(points, angle):
#     """Rotates points to given angle clockwise
#
#     Examples
#     --------
#     >>> points = np.load('test_data/points0.npy')
#     >>> rot63_points = rot(points, np.radians(63))
#     >>> rot128_points = rot(points, np.radians(128))
#
#     Plotting rotated points:
#     >>> _ = plt.title('rot')
#     >>> _ = plt.plot(*points.T, label='0', ls='', marker= '.')
#     >>> _ = plt.plot(*rot63_points.T, label='63', ls='', marker= '.')
#     >>> _ = plt.plot(*rot128_points.T, label='128', ls='', marker= '.')
#     >>> _ = plt.legend()
#     >>> plt.show()
#
#     Comparing with etalon element-wise:
#     >>> (rot63_points == np.load('test_data/points0_rot63.npy')).all()
#     True
#     >>> (rot128_points == np.load('test_data/points0_rot128.npy')).all()
#     True
#
#
#     Parameters
#     ----------
#     points : ndarray
#         List of XY points
#     angle : float
#         Rotation angle, radians
#
#     Returns
#     -------
#     points : ndarray
#         List of rotated XY points
#     """
#     # WTF
#     rotMatrix = np.array([[np.cos(angle), -np.sin(angle)],
#                           [np.sin(angle), np.cos(angle)]])
#     z = points.dot(rotMatrix)
#     return z


def convert2map(points, map_pix):
    """Converts list of XY points to map 2D array in which 1 stands for
    free space and -1 to obstacles which can be viewed as an image with white
    color for free space, black for obstacles and grey for unknown. This
    function first sets 1 for every pixel between zero point (sensor position)
    and all measured points, after that for every point it sets pixel
    coresponding to this point to -1

    Examples
    --------
    >>> points = np.load('test_data/points0.npy')
    >>> map_pix = 50
    >>> scan_map, min_coor = convert2map(points, map_pix)
    >>> min_coor
    array([ -6, -10], dtype=int8)
    >>> (scan_map == np.load('test_data/map0.npy')).all()
    True

    # Plotting map and points:
    # >>> _ = plt.title('convert2map')
    # >>> extent = np.array( \
    #         [min_coor[0],min_coor[0] + scan_map.shape[0], \
    #         min_coor[1], min_coor[1] + scan_map.shape[1]] \
    #     )*map_pix
    # >>> _ = plt.imshow(scan_map.T, cmap=plt.cm.Greys, interpolation='none', \
    #     origin='lower', extent=extent)
    # >>> _ = plt.plot(*points.T, ls='', marker= '.')
    # >>> plt.show()



    Parameters
    ----------
    points : ndarray
        List of XY points
    map_pix : int
        Size of map pixel in mm

    Returns
    -------
    map_array : ndarray
        2D map array with dtype numpy.int8
    min_coor : ndarray
        XY coordinates of top left angle of map (i.e. shift of map from zero)
    """
    pixelMap = (points // map_pix).astype(np.int8)
    # print(pixelMap)
    minCoord = pixelMap.min(0)
    maxCoord = pixelMap.max(0)
    mapSize = maxCoord-minCoord

    print(mapSize)

    z = pixelMap[minCoord[0]:maxCoord[0]][minCoord[1]:maxCoord[1]]
    print(z)

    return z, minCoord


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    points = np.load('test_data/points0.npy')
    map_pix = 50
    scan_map, min_coor = convert2map(points, map_pix)
