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
        force (data struct): Data structure using a list to hole the force
                                attributes
    Returns:
        None
    """
    x = force[0][0]
    y = force[0][1]
    z = force[0][2]

    Px = force[1][0]
    Py = force[1][1]
    Pz = force[1][2]

    force[2][0] = Pz*y - Py*z
    force[2][1] = Px*z - Pz*x
    force[2][2] = Py*x - Px*y


