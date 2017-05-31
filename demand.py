# -*- coding: utf-8 -*-
"""The demand module assists in calculating the demand on each bolt due to
different loading geometries for simple bolt connections. The different
geometries include:
    * shear
    * eccentricity in the plane of the faying surface
        + elastic
        + plastic
    * eccentricity normal to the plane of the faying surface
        + neutral axis not at c.g.
        + neutral axis assumed at c.g.
        + considerting initial tension

Definitions:
    bolt (data struct): [bolt_num,
                         (user_x, user_y),
                         diameter,
                         [xc, yc],
                         [Rsx, Rsy],
                         [Rex, Rey],
                         [dx, dy],
                         de,
                         delta,
                         r,
                         [Rux, Ruy]]

    bolt num (int): bolt number for user identification purposes
    user_x (float): user entered x-coordinate for bolt based on user coordinate
                    system
    user_y (float): user entered y-coordinate for bolt based on user coordinate
                    system
    diameter (float): diameter of bolt 
    xc (float): bolt x-coordinate with respect to the centroid of the bolt group
    yc (float): bolt y-coordinate with respect to the centroid of the bolt group
    Rsx (float): the elastic shear reaction on the bolt in the x-direction due
                 to a direct shear load
    Rsy (float): the elastic shear reaction on the bolt in the y-direction due
                 to a direct shear load
    Rex (float): the elastic shear reaction on the bolt in the x-direction due
                 to an eccentric load in the plane of the connection
    Rey (float): the elastic shear reaction on the bolt in the y-direction due
                 to an eccentric load in the plane of the connection
    dx (float): bolt x-coordinate with respect to the IC of the bolt group
    dy (float): bolt y-coordinate with respect to the IC of the bolt group
    d (float): distance from the IC to the bolt, sqrt(dx^2 + dy^2)
    delta (float): deformation of the fastner
    r (float): Ri/Rult ratio
    Rux (float): the plastic shear reaction on the bolt in the x-direction
    Ruy (float): the plastic shear reaction on the bolt in the y-direction

    force (data struct): [(user_x, user_y, user_z,
                          (Px, Py, Pz),
                          [Mx, My, Mz],
                          [local_x, local_y, local_z]]
    
    user_x (float): user entered x-coordinate of force application point based
                    on the user coordinate system
    user_y (float): user entered y-coordinate of force application point based
                    on the user coordinate system
    user_z (float): user entered z-coordinate of force application point based
                    on the user coordinate system
    Px (float): user entered force in the x-direction
    Py (float): user entered force in the y-direction
    Pz (float): user entered force in the z-direction
    Mx (float): elastic moment about the x-axis 
    My (float): elastic moment about the y-axis
    Mz (float): elastic moment about the z-axis passing thru the centroid of the
                bolt group

Notes:
    The idea behind the design of the data structure used for the bolt and force
    is the need to keep track of results calculated relative to each bolt or
    force. Properties of the bolt pattern can be calculated at any time based on
    the bolts in the pattern. 

    There has been consideration to create a third data structure called
    bolt pattern to keep track of the properties of the bolt pattern but at this
    time it does not seem necessary. 
"""
import math

def shear(bolts, force):
    """Calculate the direct shear force in each direction on each bolt.

    For each bolt the force in the x and y directions is divided by total number
    of bolts and the resultant reaction is stored as the x and y reaction for
    each bolt.

    rx = px/num_bolts
    ry = py/num_bolts

    Args:
        bolts (data struct): list of the bolt data structure
        force (data struct): single force data structure

    Returns:
        None

    Notes:
        Populates the 
    """
    num_bolts = len(bolts)
    for bolt in bolts:
        px = force[1][0]
        py = force[1][1]

        rsx = -px/num_bolts
        rsy = -py/num_bolts

        bolt[4][0] = rsx
        bolt[4][1] = rsy

def tension(bolts, force):
    pass

def ecc_in_plane_elastic(bolts, force):
    """Calc the bolt reactions in an elastic in plane eccentric shear connection.
    
    For each bolt the moment about the z-axis is proportioned based the
    distance from the centroid of the group to center of the bolt. The resultant
    reaction is stored in the x and y force for each bolt. See Salmon and
    Johnson 5th Edition pp. 118 for further details. 

    rx = mz*local_yb/j
    ry = -1*mz*local_xb/j

    The rx is multiplied by -1 due to the coordinate system used for this program. 

    Args:
        bolts (data struct): list of the bolt data structure
        force (data struct): single force data structure

    Returns:
        None

    """
    mz = force[2][2]

    j = calc_j(bolts)

    for bolt in bolts:
        local_xb = bolt[3][0]
        local_yb = bolt[3][1]

        #px = py*local_xf*local_yb/j - px*local_yf*local_yb/j
        #py = py*local_xf*local_xb/j - px*local_yf*local_xb/j
        rex = mz*local_yb/j
        rey = -1*mz*local_xb/j

        bolt[5][0] = rex
        bolt[5][1] = rey

def calc_moments_about_centroid(bolts, force):
    """Calculate the x, y, and z moments about the centroid of the bolt group.

    mx = pz(y) - py(z)
    my = px(z) - pz(x)
    mz = py(x) - px(y)

    Args:
        force (data struct): Data structure using a list to hold the force
                                attributes
    Returns:
        None
    """
    local_x = force[3][0]
    local_y = force[3][1]
    local_z = force[3][2]

    px = force[1][0]
    py = force[1][1]
    pz = force[1][2]

    mx = pz*local_y - py*local_z
    my = px*local_z - pz*local_x
    mz = py*local_x - px*local_y

    force[2][0] = mx
    force[2][1] = my
    force[2][2] = mz

def calc_centroid(bolts):
    """Calculate the centroid of the bolt group.
    
    Args:
        bolts (data struct): list of the bolt data structure

    Returns:
        x_centroid (float): x-coordinate of bolt group centroid
        y_centroid (float): y-coordinate of bolt group centroid

        This coordinate pair is returned as a tuple, as follows:
        (x_centroid, y_centroid)
    """
    sum_x = 0.0
    sum_y = 0.0
    num_bolts = len(bolts)
    for bolt in bolts:
        x = bolt[1][0]
        y = bolt[1][1]
        sum_x = sum_x + x
        sum_y = sum_y + y

    x_centroid = sum_x/num_bolts
    y_centroid = sum_y/num_bolts

    return x_centroid, y_centroid

def calc_local_bolt_coords(bolts):
    """Calculate bolt coords with the centroid of the bolt group as the origin.
    
    Args:
        bolts ():

    Returns:
        None

    Notes:
        Populates the x and y coordinate location of each bolt data structure
        with respect to the centroid of the bolt group
    """
    x_cent, y_cent = calc_centroid(bolts)

    for bolt in bolts:
        user_x = bolt[1][0]
        user_y = bolt[1][1]
        local_x = user_x - x_cent
        local_y = user_y - y_cent
        bolt[3][0] = local_x
        bolt[3][1] = local_y

def calc_local_force_coords(bolts, force):
    """Calculate force coords with the centroid of the bolt group as origin.
    
    Args:
        bolts ():
        force (data struct):

    Returns:
        None

    Notes:
        Populates the x, y, and z coordinate location of the force data
        structure with respect to the centroid of the bolt group
    """
    x_cent, y_cent = calc_centroid(bolts)

    user_x = force[0][0]
    user_y = force[0][1]
    user_z = force[0][2]

    local_x = user_x - x_cent
    local_y = user_y - y_cent
    local_z = user_z

    force[3][0] = local_x
    force[3][1] = local_y
    force[3][2] = local_z

def calc_ixx(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the x-axis.
   
    Assumes all bolts are the same diameter.

    Args:
        bolts ():

    Returns:
        sum_ixx (float): 2nd moment of area of bolt pattern about the x-axis

    Raises:
        ValueError

    Notes:
        Must call calc_local_force_coords to populate the y-coordinate with
        respect to the centroid in the bolt data structure before calling this
        function.
    """
    sum_ixx = 0.0
    for bolt in bolts:
        y = bolt[3][1]
        sum_ixx = sum_ixx + math.pow(y,2)
    return sum_ixx

def calc_iyy(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the y-axis.
   
    Assumes all bolts are the same diameter.

    Args:
        bolts ():

    Returns:
        sum_iyy (float): 2nd moment of area of the bolt pattern about the y-axis

    Notes:
        Must call calc_local_force_coords to populate the x-coordinate with
        respect to the centroid in the bolt data structure before calling this
        function.
    """
    sum_iyy = 0.0
    for bolt in bolts:
        x = bolt[3][0]
        sum_iyy = sum_iyy + math.pow(x,2)
    return sum_iyy

def calc_j(bolts):
    """Calculate the polar moment of area of bolt pattern about the z-axis.
    
    Args:
        bolts ():

    Returns:
        j (float): polar moment of area of the bolt pattern about the z-axis

    Notes:
        Must call calc_local_force_coords to populate the x and y coordinate
        with respect to the centroid in the bolt data structure before calling
        this function.
    """
    ixx = calc_ixx(bolts)
    iyy = calc_iyy(bolts)
    j = ixx + iyy
    return j

def ecc_in_plane_plastic(bolts, force):
    """Calculate the maximum bolt force based on plastic bolt deformation."""
    px = force[1][0]
    py = force[1][1]
    mo = force[2][2]
    p_vector = math.sqrt(math.pow(px,2) + math.pow(py,2))
    x1, y1 = calc_instanteous_center(bolts, px, py, mo)
    mp = calc_mp(bolts, force, x1, y1)
    calc_d(bolts, x_ic, y_ic)

    error = 1.0
    
    while error > 0.01:

        sum_rux, sum_ruy, sum_m = calc_plastic_reactions(bolts, mp)
    
        fx = px + sum_rux
        fy = py + sum_ruy
        f_vector = math.sqrt(math.pow(fx,2) + math.pow(fy,2))

        x2, y2 = calc_instanteous_center(bolts, fx, fy, mo)
        mp = calc_mp(force, x2, y2)

        fx_error = abs(fx/px)
        fy_error = abs(fy/py)
        fv_error = abs((p_vector-f_vector)/p_vector)

        error = max(fx_error, fy_error, fv_error)

def calc_plastic_reactions(bolts, mp):
    """Calculate the resisting bolt force."""
    sum_m = calc_moment_about_ic(bolts)

    sum_rux = 0.0
    sum_ruy = 0.0
    
    for bolt in bolts:
        d = bolt[7]
        dx = bolt[6][0]
        dy = bolt[6][1]
        r = bolt[9]

        rult = -mp/sum_m
        rux = -dy/d*r*rult
        ruy = dx/d*r*rult

        sum_rux = sum_rux + rux
        sum_ruy = sum_ruy + ruy
        
        bolt[10][0] = rux #updating reaction based on new ic location
        bolt[10][1] = ruy #updating reaction based on new ic location

    return sum_rux, sum_ruy, sum_m

def calc_moment_about_ic(bolts):
    """Calculate the moment about the IC of bolt force divided by Rult."""
    sum_m = 0.0
    d_max = calc_d_max(bolts)
    for bolt in bolts:
        d = bolt[7]

        delta = 0.34*d/d_max
        r = math.pow((1 - math.exp(-10*delta)),0.55) #ri/rult
        m = r*d

        sum_m = sum_m + m
        
        bolt[8] = delta
        bolt[9] = r

    return sum_m


def calc_d(bolts, x_ic, y_ic):
    """Calculate the distance from the bolt to the instanteous center."""

    for bolt in bolts:
        dx = bolt[3][0] - x_ic
        dy = bolt[3][1] - y_ic

        d = math.sqrt(math.pow(dx,2) + math.pow(dy,2))

        bolt[6][0] = dx
        bolt[6][1] = dy
        bolt[7] = d

def calc_mp(force, x_ic, y_ic):
    """Calculate the moment about the instanteous center."""
    x = force[3][0]
    y = force[3][1]

    px = force[1][0]
    py = force[1][1]

    x1 = x - x_ic
    y1 = y - y_ic

    mp = py*x1 - px*y1

    return mp

def calc_instanteous_center(bolts, fx, fy, mo):
    """Calculate the instanteous center with respect to the centroid."""
    x0 = 0.0
    y0 = 0.0
    j = calc_j(bolts)

    num_bolts = len(bolts)

    ax = -fy/num_bolts*j/mo
    ay = fx/num_bolts*j/mo

    x1 = x0 + ax
    y1 = y0 + ay

    return x1, y1

#def calc_d_max(bolts):
#    d_max = 0.0
#    for bolt in bolts:
#        d = bolt[6]
#        if d > d_max:
#            d_max = d
#
#    return d_max
#
#def calc_sum_d_squared(bolts):
#    sum_d_sqaured = 0.0
#    for bolt in bolts:
#        d = bolt[6]
#        sum_d_squared = sum_d_squared + math.pow(de, 2)
#
#    return sum_d_squared

def calc_neutral_axis(bolts):
    pass

