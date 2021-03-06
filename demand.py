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

TODO:
    There is also consideration to use an object oriented approach for the
    bolts, forces, and bolt pattern. This would require a major refactoring of
    the code and will not happen immediately. 

    The delta angle at a minimum should be part of the force data structure and
    if oop is implemented in the future should be part of the force class. It is
    currently to much of a hassle to implement. 
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
        Populates the direct shear reactions Rsx and Rsy in the bolt data
        structure
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
        
    Notes:
        Populates the elastic eccentric force in the plane reations Rex and Rey
        in the bolt data structure
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


def calc_moments_about_centroid(force):
    """Calculate the x, y, and z moments about the centroid of the bolt group.

    mx = pz(y) - py(z)
    my = px(z) - pz(x)
    mz = py(x) - px(y)

    Args:
        force (data struct): single force data structure attributes

    Returns:
        None

    Notes:
        Populates the moments about each axis Mx, My, and Mz in the force data
        structure
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


def calc_bolt_coords_wrt_centroid(bolts):
    """Calculate bolt coords with respect to the centroid of the bolt group.
    
    Args:
        bolts (data struct): list of the bolt data structure

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


def calc_force_coords_wrt_centroid(bolts, force):
    """Calculate force coords with respect to the centroid of the bolt group.
    
    Args:
        bolts (data struct): list of the bolt data structure
        force (data struct): single force data structure attributes

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

    cx = user_x - x_cent
    cy = user_y - y_cent
    cz = user_z

    force[3][0] = cx
    force[3][1] = cy
    force[3][2] = cz

    px = force[1][0]
    py = force[1][1]

    delta_angle = calc_delta_angle(px, py)

    ec = abs(cx*math.cos(delta_angle) + cy*math.sin(delta_angle))

    force[4] = ec

def calc_delta_angle(px, py):
    """Calculate the angle between the vertical and the force line of action.

    Args:
        px (float): Applied horizontal force component
        py (float): Applied vertical force component

    Returns:
        delta_angle (float): angle between vertical and the line of action of
                             the force
    """
    try:
        delta_angle = -1*math.atan(px/py)
    except:
        delta_angle = math.pi/2

    return delta_angle

def calc_ixx(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the x-axis.
   
    Assumes all bolts are the same diameter.

    Args:
        bolts (data struct): list of the bolt data structure

    Returns:
        sum_ixx (float): 2nd moment of area of bolt pattern about the x-axis

    Raises:

    Notes:
        Must call calc_force_coords_wrt_centroid to populate the y-coordinate with
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
        bolts (data struct): list of the bolt data structure

    Returns:
        sum_iyy (float): 2nd moment of area of the bolt pattern about the y-axis

    Raises:

    Notes:
        Must call calc_force_coords_wrt_centroid to populate the x-coordinate with
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
        bolts (data struct): list of the bolt data structure

    Returns:
        j (float): polar moment of area of the bolt pattern about the z-axis

    Raises:

    Notes:
        Must call calc_force_coords_wrt_centroid to populate the x and y coordinate
        with respect to the centroid in the bolt data structure before calling
        this function.
    """
    ixx = calc_ixx(bolts)
    iyy = calc_iyy(bolts)
    j = ixx + iyy
    return j


def iterate_to_ic(bolts, force):
    """Iterate to the location of the instantaneous center.
    
    This function starts at the centroid (0.0, 0.0) and calculates the first
    approximation of the instantaneous center, or what's known as the elastic
    instantaneous center in the first iteration. This is the starting point
    for subsequent iterations of the instantaneous center.

    After each iteration force equilibrium is used to determine if the
    approximated IC is close enough to reduce error to a minimum. The applied
    force and the reaction of the bolts are summed about the IC.

    Args:
        bolts ():
        force ():

    Returns:
        x (float):
        y (float):

    Notes:
        a seperate but unncessary convergence test
        r = force[6]
        if delta_angle == 0.0:
            pfx = 0.0
        else:
            pfx = sum_rux/math.sin(delta_angle)

        if delta_angle == math.pi/2:
            pfy = 0.0
        else:
            pfy = sum_ruy/math.cos(delta_angle)

        pm = sum_m/r

        diff_xy = abs(pfx - pfy)
        diff_ym = abs(pfy - pm)
        diff_mx = abs(pm - pfx)
         
    """
    px = force[1][0]
    py = force[1][1]
    mo = force[2][2]
    delta_angle = calc_delta_angle(px, py)
    x0 = 0.0 #coordinate system centered on centroid
    y0 = 0.0 #coordinate system centered on centroid

    fx = px
    fy = py
    count = 0

    while True:
        x_ic, y_ic = calc_instanteous_center(bolts, fx, fy, mo, x0, y0)
        calc_bolt_location_wrt_ic(bolts, x_ic, y_ic)
        calc_force_location_wrt_ic(force, x_ic, y_ic, delta_angle)
        mp = calc_mp(force)

        sum_rux, sum_ruy, sum_m = calc_bolt_fraction_reactions(bolts, mp)

        if count == 0:
            sum_d_squared = calc_sum_d_squared(bolts)
            d_max = calc_d_max(bolts)
            ce = sum_d_squared/(d_max*mp)
   
        cu = mp/sum_m

        fx = px + sum_rux
        fy = py + sum_ruy

        error = max(abs(fx), abs(fy))

        if error < 0.01:
            break
        elif count == 50:
            raise 
        else:
            x0 = x_ic
            y0 = y_ic

        count += 1

    return x_ic, y_ic, ce, cu


def calc_bolt_reactions(bolts, rult):
    """Calculate the actual force on each bolt.
    
    Now that the approximate location of instantaneous center is known from the 
    iterate_to_instantaneous_center the deflection of each bolt is known. The
    deflection for each bolt is stored in the bolt data structure and is updated
    during the iteration. 

    With the deformation of each bolt known and the ultimate capacity of the bolt
    provided by the user one can calculate the actual shear force on each bolt
    using the equation below.

    ri = rult*(1 - e^(-10*delta))^(0.55)
    rux = ri*dy/d_max
    ruy = ri*dx/d_max

    Defintions of variables:
        ri - total shear reaction on bolt
        delta - deformation of bolt
        rux - x-component of shear reaction on bolt
        ruy - y-component of shear reaction on bolt

    Args:
        bolts (data struct): list of the bolt data structure
        rult (float): ultimate capacity of a single bolt

    Returns:
        None

    Notes:
        Must execute the iterate_to_instantaneous_center function before calling
        this function.

        Populates the Rux and Ruy in the bolt data structure.
    """
    d_max = calc_d_max(bolts)
    for bolt in bolts:
        delta = bolt[9]
        dx = bolt[6]
        dy = bolt[6]
        ri = rult*math.pow((1 - math.exp(-10*delta)),0.55)
        rux = ri*dy/d_max
        ruy = ri*dx/d_max

        bolt[11][0] = rux
        bolt[11][1] = ruy


def calc_bolt_fraction_reactions(bolts, mp):
    """Calculate the resisting bolt force fraction."""
    sum_m = calc_moment_about_ic(bolts)

    sum_rux = 0.0
    sum_ruy = 0.0
    
    for bolt in bolts:
        d = bolt[7]
        dx = bolt[6][0]
        dy = bolt[6][1]
        r = bolt[9]

        rult = -1*mp/sum_m
        rux = -1*dy/d*r*rult
        ruy = dx/d*r*rult

        sum_rux = sum_rux + rux
        sum_ruy = sum_ruy + ruy

        
    return sum_rux, sum_ruy, sum_m


def calc_moment_about_ic(bolts):
    """Calculate the moment about the IC of bolt force fraction.
    
    This can be thought of as the resisting moment. 
    
    Args:
        bolts (data struct): list of the bolt data structure
            
    Returns:
        sum_m (float): The total resisting moment due to the bolt force fraction
                       acting about the IC
                       
    Notes:
        The function also populates the bolt data structure with the calculated
        bolt deflection, delta, and the bolt force fraction, ri_rult_ratio.
    """
    sum_m = 0.0
    d_max = calc_d_max(bolts)
    for bolt in bolts:
        d = bolt[7]

        delta = 0.34*d/d_max
        ri_rult_ratio = math.pow((1 - math.exp(-10*delta)),0.55) #ri/rult
        m = ri_rult_ratio*d

        sum_m = sum_m + m
        
        bolt[8] = delta
        bolt[9] = ri_rult_ratio

    return sum_m

def calc_bolt_location_wrt_ic(bolts, x_ic, y_ic):
    """Calculate the distance from the bolt to the instanteous center.
    
    Args:
        bolts (data struct): list of the bolt data structure
        x_ic (float): x-coordinate of the instantaneous center
        y_ic (float): y_coordinate of the instantaneous center

    Returns:
        None

    Notes:
        Populates the dx, dy, and d in the bolt data structure
    """
    for bolt in bolts:
        dx = bolt[3][0] - x_ic
        dy = bolt[3][1] - y_ic

        d = math.sqrt(math.pow(dx,2) + math.pow(dy,2))

        bolt[6][0] = dx
        bolt[6][1] = dy
        bolt[7] = d


def calc_force_location_wrt_ic(force, x_ic, y_ic, delta_angle):
    """Calculate the location of the load application point wrt the IC.
    
    Args:
        force (data struct): single force data structure attributes
        x_ic (float): x-component of the instantaneous center
        y_ic (float): y-component of the instantaneous center
        delta_angle (float): angle measured from vertical to the line of action,
                             clockwise taken as negative

    Returns:
        None

    Notes:
        Populates dx_f and dy_f in the force data structure.
    """
    cx = force[3][0]
    cy = force[3][1]

    dx_f = cx - x_ic
    dy_f = cy - y_ic

    force[5][0] = dx_f
    force[5][1] = dy_f


def calc_r(force, x_ic, y_ic, delta_angle):
    """Calculate the perpendicular distance from the line of application to the IC.
    
    This function calculates the "moment arm" of the applied force with respect
    to the instantaneous center. 

    This distance is different from the distance between the point of application
    to the instantaneous center because it accounts for the direction of the
    applied force. 

    Args:
        force (data struct): single force data structure attributes
        x_ic (float): x-component of the instantaneous center
        y_ic (float): y-component of the instantaneous center
        delta_angle (float): angle measured from vertical to the line of action,
                             clockwise taken as negative

    Returns:
        None

    Notes:
        Populates r in the force data structure
    """
    cx = force[3][0]
    cy = force[3][1]

    r = abs(cx*math.cos(delta_angle) + cy*math.sin(delta_angle) - 
            x_ic*math.cos(delta_angle) - y_ic*math.sin(delta_angle))

    force[6] = r


def calc_mp(force):
    """Calculate the moment due to the applied force about the IC.
    
    Args:
        force (data struct): single force data structure attributes

    Returns:
        mp (float): moment due to the applied force about the IC
    """
    px = force[1][0]
    py = force[1][1]

    dx_f = force[5][0]
    dy_f = force[5][1]

    mp = py*dx_f - px*dy_f

    return mp


def calc_instanteous_center(bolts, fx, fy, mo, x0, y0):
    """Calculate the instanteous center with respect to another coordinate point.

    The distance to the next IC is calculated based on the differential of
    force between the applied force and the resistance of the bolt group about
    the current IC. 
    
    Args:
        bolts (data struct): list of the bolt data structure
        fx (float): x-component of the applied force
        fy (float): y-component of the applied force
        mo (float): moment about the centroid of the applied force
        x0 (float): x-component of the previous approximation of the IC
        x0 (float): y-component of the previous approximation of the IC

    Returns
        x1 (float): x-component of the current approximation of the IC
        y1 (float): y-component of the current approximation of the IC

    Notes:
    """
    j = calc_j(bolts)

    num_bolts = len(bolts)

    ax = -fy/num_bolts*j/mo
    ay = fx/num_bolts*j/mo

    x1 = x0 + ax
    y1 = y0 + ay

    return x1, y1


def calc_d_max(bolts):
    """Return the maximum distance from the IC of any bolt in the bolt group.

    This function loops through the bolt data structures looking for the bolt
    with the maximum distance from the IC. It returns the maximum distance
    found. 

    Args:
        bolts (data struct): list of the bolt data structure

    Returns:
        d_max (float): Maximum distance from IC of any bolt in the bolt group

    Notes:
        Must execute 
    """
    d_max = 0.0
    for bolt in bolts:
        d = bolt[7]
        if d > d_max:
            d_max = d

    return d_max

def calc_sum_d_squared(bolts):
    """Return the sum of the squared bolt distances."""
    sum_d_squared = 0.0
    for bolt in bolts:
        d = bolt[7]
        sum_d_squared = sum_d_squared + math.pow(d, 2)

    return sum_d_squared

def calc_neutral_axis(bolts):
    pass

