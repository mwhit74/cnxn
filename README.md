The sbc package is designed to assist in the analysis of simple bolted
connections. A simple bolt connection transfers tension and shear from one
component to another through bolts. This program is limited to bolt analysis. It
does not currently consider the member capacity in the vacinity of the connection
including but not limited to bearing, excessive deformation, block shear
rupture, yielding of the gross cross-section, and fracture of the net
cross-section. 

A simple bolt connection is not a partial moment connection (PMC) or a full 
moment connection (FMC). Those connections require a different analysis not
covered by this program.

The initial goal of this program is to develop the demand functionality. The
next priority would be the capacity followed by the analysis and finally the
design. 


user input
bolt
    - bolt num
    - x-coord
    - y-coord
    - diameter
force
    - x-coord
    - y-coord
    - z-coord
    - px
    - py
    - pz
analysis type
    - shear
    - tension?
    - ecc_in_plane_elastic
    - ecc_in_plane_plastic
    - ecc_out_plane_find_na
    - ecc_out_plane_na
    - ecc_out_plane_init_ten

assumptions
1. it is up to the user to determine the x and y coordinates of their origin and
stick to it
2. the x and y axes are parallel to the faying surface. x is positive to the
right and y is positive up.
3. the z-axis is perpendicular to the faying surface. z is positive by the right
hand rule or pointing out of the page
4. bolt direction is taken as the axis parallel to the longitudinal axis of the
bolt
5. all bolts are perpendicular to the faying surface, i.e. the bolts are
parallel to the z-axis
6. the faying surface is the origin of the z-axis
7. only one faying surface is allowed
