import math

def shear(bolts, force):
    """Calculate the direct shear force in each direction on each bolt.

    For each bolt the force in the x and y directions is divided by total number
    of bolts and the resultant reaction is stored as the x and y reaction for
    each bolt.

    Args:
        bolts (list): List of the bolts in the connetion conforming to the
                        prescribed data structure for a bolt
        force (data struct): Data structure using a list to hold the force
                                attributes
    Returns:
        None
    """
    calc_moments(force)
    num_bolts = len(bolts)
    for bolt in bolts:
        bolt_reacs = bolt[3]
        px = force[1][0]
        py = force[1][1]
        bolt_reacs[0] = px/num_bolts #rx
        bolt_reacs[1] = py/num_bolts #ry

def tension(bolts, force):
    pass

def ecc_in_plane_elastic(bolts, force):
    pass

def calc_moments(force):
    """Calculate the x, y, and z moments.

    MX = Pz(y) - Py(z)
    MY = Px(z) - Pz(x)
    MZ = Py(x) - Px(y)

    Args:
        force (data struct): Data structure using a list to hold the force
                                attributes
    Returns:
        None
    """
    force = calc_local_force_coords(force)
    x = force[0][0]
    y = force[0][1]
    z = force[0][2]

    Px = force[1][0]
    Py = force[1][1]
    Pz = force[1][2]

    force[2][0] = Pz*y - Py*z
    force[2][1] = Px*z - Pz*x
    force[2][2] = Py*x - Px*y

def calc_instanteous_center(bolts):

def calc_neutral_axis(bolts):

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
        bolt[1][0] = local_x
        bolt[1][1] = local_y

def calc_local_force_coords(bolts, force):
    """Calculate force coords with the centroid of the bolt group as origin."""
    x_cent, y_cent = calc_centroid(bolts)

    user_x = force[0][0]
    user_y = force[0][1]
    user_z = force[0][2]

    local_x = user_x - x_cent
    local_y = user_y - y_cent
    local_z = user_z

    force[0][0] = local_x
    force[0][1] = local_y
    force[0][2] = local_z

def calc_ixx(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the x-axis."""
    bolts = calc_local_bolts_coords(bolts)
    sum_ixx = 0.0
    for bolt in bolts:
        y = bolt[1][1]
        sum_ixx = sum_ixx + math.pow(y,2)
    return sum_ixx

def calc_iyy(bolts):
    """Calculate the 2nd moment of area of the bolt pattern about the y-axis."""
    bolts = calc_local_bolts_coords(bolts)
    sum_iyy = 0.0
    for bolt in bolts:
        x = bolt[1][0]
        sum_iyy = sum_iyy + math.pow(x,2)
    return sum_iyy

def calc_j(bolts):
    """Calculate the polar moment of area of bolt pattern about the z-axis."""
    ixx = calc_ixx(bolts)
    iyy = calc_iyy(bolts)
    return math.pow(ixx,2) + math.pow(iyy,2)
