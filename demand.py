import math

def shear(bolts, force):
    """Calculate the direct shear force in each direction on each bolt.

    For each bolt the force in the x and y directions is divided by total number
    of bolts and the resultant reaction is stored as the x and y reaction for
    each bolt.

    rx = px/num_bolts
    ry = py/num_bolts

    Args:
        bolts (list): List of the bolts in the connetion conforming to the
                        prescribed data structure for a bolt
        force (data struct): Data structure using a list to hold the force
                                attributes
    Returns:
        None
    """
    num_bolts = len(bolts)
    for bolt in bolts:
        px = force[1][0]
        py = force[1][1]

        rex = -px/num_bolts
        rey = -py/num_bolts

        bolt[4][0] = rex
        bolt[4][1] = rey

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
        bolts (list): List of the bolts in the connetion conforming to the
                        prescribed data structure for a bolt
        force (data struct): Data structure using a list to hold the force
                                attributes
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

        bolt[4][0] = rex
        bolt[4][1] = rey

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
    """Calculate the centroid of the bolt group."""
    sum_x = 0.0
    sum_y = 0.0
    num_bolts = len(bolts)
    for bolt in bolts:
        x = bolt[1][0]
        y = bolt[1][1]
        sum_x = sum_x + x
        sum_y = sum_y + y

    return sum_x/num_bolts, sum_y/num_bolts

def calc_local_bolt_coords(bolts):
    """Calculate bolt coords with the centroid of the bolt group as the origin."""
    x_cent, y_cent = calc_centroid(bolts)

    for bolt in bolts:
        user_x = bolt[1][0]
        user_y = bolt[1][1]
        local_x = user_x - x_cent
        local_y = user_y - y_cent
        bolt[3][0] = local_x
        bolt[3][1] = local_y

def calc_local_force_coords(bolts, force):
    """Calculate force coords with the centroid of the bolt group as origin."""
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
    """Calculate the 2nd moment of area of the bolt pattern about the x-axis."""
    sum_ixx = 0.0
    for bolt in bolts:
        y = bolt[3][1]
        sum_ixx = sum_ixx + math.pow(y,2)
    return sum_ixx

def calc_iyy(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the y-axis."""
    sum_iyy = 0.0
    for bolt in bolts:
        x = bolt[3][0]
        sum_iyy = sum_iyy + math.pow(x,2)
    return sum_iyy

def calc_j(bolts):
    """Calculate the polar moment of area of bolt pattern about the z-axis."""
    ixx = calc_ixx(bolts)
    iyy = calc_iyy(bolts)
    return ixx + iyy

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
        d = bolt[6]
        dx = bolt[5][0]
        dy = bolt[5][1]
        r = bolt[8]

        rult = -mp/sum_m
        rux = -dy/d*r*rult
        ruy = dx/d*r*rult

        sum_rux = sum_rux + rux
        sum_ruy = sum_ruy + ruy
        
        bolt[9][0] = rux #updating reaction based on new ic location
        bolt[9][1] = ruy #updating reaction based on new ic location

    return sum_rux, sum_ruy, sum_m

def calc_moment_about_ic(bolts):
    """Calculate the moment about the IC of bolt force divided by Rult."""
    sum_m = 0.0
    d_max = calc_d_max(bolts)
    for bolt in bolts:
        d = bolt[6]

        delta = 0.34*d/d_max
        r = math.pow((1 - math.exp(-10*delta)),0.55) #ri/rult
        m = r*d

        sum_m = sum_m + m
        
        bolt[7] = delta
        bolt[8] = r

    return sum_m


def calc_d(bolts, x_ic, y_ic):
    """Calculate the distance from the bolt to the instanteous center."""

    for bolt in bolts:
        dx = bolt[3][0] - x_ic
        dy = bolt[3][1] - y_ic

        d = math.sqrt(math.pow(dx,2) + math.pow(dy,2))

        bolt[5][0] = dx
        bolt[5][1] = dy
        bolt[6] = d

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

