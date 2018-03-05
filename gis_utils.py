import csv
import math

def get_feature_class(base_name, workspace):
    """
    Creates a valid ESRI reference to a shapefile or geodatabase feature class
    base_name: the name of the feature class, without any extension
    workspace: the name of the folder (for shapefiles) or geodatabase (for gdb feature classes)
    return: a text string referring to the location of the feature class
    """
    if workspace[-4:] != '.gdb':
        fc = workspace + '\\' + base_name + '.shp'
    else:
        fc = workspace + '\\' + base_name
    return fc




def save_to_CSV(attribute_names, data_vals, out_file):
    """
    Writes tabular data to a comma-separated-value (csv) file
    attribute_names: the headers of each column in table
    data_vals: a list of tuples, where each tuple contains values in one table row
    return: function has no return value. data is written to out_file.
    """
    with open(out_file,"w") as ofile:
        writer = csv.writer(ofile) #creates csv writer object
        writer.writerow(attribute_names) #writes header
        for data in data_vals: #iterate through the data values and writes each row.
            writer.writerow(data)




def traverse_survey_line(from_pt, distance, bearing):
    """
    Determines the point at the given distance and bearing from from_pt
    from_pt: a tuple with two floats (x & y coords of start pt)
    distance: distance of survey line
    bearing: direction of survey line, in degrees clockwise from North
    return: a tuple with two floats (x & y coords of end pt)
    """
    x0 = from_pt[0]
    y0 = from_pt[1]
    bearing = math.radians(bearing) #converts from degree to radians

    x1 = x0 + distance*math.cos(bearing) #finds target x coordinate
    y1 = y0 + distance*math.sin(bearing) #finds target y coordinate

    return (x1,y1)




def polygon_area(polygon):
    """
    Computes the area of a polygon.
    polygon: list of tuples representing points (x, y).
             first and last point should be the same.
    return: the polygon area
    """

    w=0
    for count in range(len(polygon)-1):
        y = polygon[count+1][1] + polygon[count][1]
        x = polygon[count+1][0] - polygon[count][0]
        z = y * x
        w += z
    return abs(w/2.0)
#reference https://www.mathsisfun.com/geometry/area-irregular-polygons.html
#reference https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates#answer-43659322





def circle(center_pt, radius):
    """
    Creates a polygon with the given center point and radius
    center_pt: center of circle, as tuple (x, y)
    radius: radius of circle
    return: list of tuples representing points on circle boundary.
             first and last point should be the same.
    """


    circle_points = [(radius*math.cos(i)+center_pt[0],radius*math.sin(i)+center_pt[0]) for i in range(0,360)]
    return circle_points
#reference https://en.wikipedia.org/wiki/Circle#Equations