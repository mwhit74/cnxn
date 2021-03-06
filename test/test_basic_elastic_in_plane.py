import demand
import unittest
import pdb
import os.path

class TestDemandElasticInPlane(unittest.TestCase):
    def setUp(self):
        diameter = 1.25
        self.bolts = []
        for x in xrange(0,10):
            for y in xrange(0,10):
                bolt_num = float(x+y+1)
                self.bolts.append([bolt_num,
                                   (float(x),float(y)),
                                   diameter, 
                                   [None, None],
                                   [None, None],
                                   [None, None],
                                   [None, None],
                                   None,
                                   None,
                                   None,
                                   [None, None]])

        self.force = [(20.0, 25.0, 5.0),(7.54, 2.34, 4.37),[None, None, None],
                     [None, None, None], None, [None, None], None]

    def tearDown(self):
        del self.force
        del self.bolts

#ECCENTRIC SHEAR IN THE PLANE OF THE CONNECTION - ELASTIC

#This test will place a force application point in each quadrant
#assuming the centroid is the origin. At each force application point a
#a force will be applied in each direction +x, -x, +y, and -y. This set of
#forces will include all possible combinations of direction in the x and
#y directions.
#
#This set needs to be applied in each quandrant to vary the signs on the
#eccentricities associated with the force application point.
#
#The purpose of this test is to make sure the sign convention is correct
#and consistent for all possible force application points and directions.

#QUADRANT 1 
    def test_ecc_in_plane_elastic_q1_fpx(self):
        force_px = [(7.0, 6.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_px)
        demand.calc_moments_about_centroid(force_px)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)

        demand.ecc_in_plane_elastic(self.bolts, force_px)

        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.03198
        cbolt_q1_ry = 0.03198
        cbolt_q2_rx = -0.03198
        cbolt_q2_ry = -0.03198
        cbolt_q3_rx = 0.03198
        cbolt_q3_ry = -0.03198
        cbolt_q4_rx = 0.03198
        cbolt_q4_ry = 0.03198

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q1_fnx(self):
        force_nx = [(7.0, 6.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_nx)
        demand.calc_moments_about_centroid(force_nx)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)

        
        demand.ecc_in_plane_elastic(self.bolts, force_nx)

        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.03198
        cbolt_q1_ry = -0.03198
        cbolt_q2_rx = 0.03198
        cbolt_q2_ry = 0.03198
        cbolt_q3_rx = -0.03198
        cbolt_q3_ry = 0.03198
        cbolt_q4_rx = -0.03198
        cbolt_q4_ry = -0.03198

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q1_fpy(self):
        force_py = [(7.0, 6.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_py)
        demand.calc_moments_about_centroid(force_py)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_py)

        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.012409 
        cbolt_q1_ry = -0.012409
        cbolt_q2_rx = 0.012409
        cbolt_q2_ry = 0.012409
        cbolt_q3_rx = -0.012409
        cbolt_q3_ry = 0.012409
        cbolt_q4_rx = -0.012409
        cbolt_q4_ry = -0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q1_fny(self):
        force_ny = [(7.0, 6.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_ny)
        demand.calc_moments_about_centroid(force_ny)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.012409
        cbolt_q1_ry = 0.012409
        cbolt_q2_rx = -0.012409
        cbolt_q2_ry = -0.012409
        cbolt_q3_rx = 0.012409
        cbolt_q3_ry = -0.012409
        cbolt_q4_rx = 0.012409
        cbolt_q4_ry = 0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

#QUADRANT 2
    def test_ecc_in_plane_elastic_q2_fpx(self):
        force_px = [(2.0, 6.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_px)
        demand.calc_moments_about_centroid(force_px)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.031988
        cbolt_q1_ry = 0.031988
        cbolt_q2_rx = -0.031988
        cbolt_q2_ry = -0.031988
        cbolt_q3_rx = 0.031988
        cbolt_q3_ry = -0.031988
        cbolt_q4_rx = 0.031988
        cbolt_q4_ry = 0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q2_fnx(self):
        force_nx = [(2.0, 6.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_nx)
        demand.calc_moments_about_centroid(force_nx)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.031988
        cbolt_q1_ry = -0.031988
        cbolt_q2_rx = 0.031988
        cbolt_q2_ry = 0.031988
        cbolt_q3_rx = -0.031988
        cbolt_q3_ry = 0.031988
        cbolt_q4_rx = -0.031988
        cbolt_q4_ry = -0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q2_fpy(self):
        force_py = [(2.0, 6.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_py)
        demand.calc_moments_about_centroid(force_py)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.012409
        cbolt_q1_ry = 0.012409
        cbolt_q2_rx = -0.012409
        cbolt_q2_ry = -0.012409
        cbolt_q3_rx = 0.012409
        cbolt_q3_ry = -0.012409
        cbolt_q4_rx = 0.012409
        cbolt_q4_ry = 0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q2_fny(self):
        force_ny = [(2.0, 6.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_ny)
        demand.calc_moments_about_centroid(force_ny)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.012409
        cbolt_q1_ry = -0.012409
        cbolt_q2_rx = 0.012409
        cbolt_q2_ry = 0.012409
        cbolt_q3_rx = -0.012409
        cbolt_q3_ry = 0.012409
        cbolt_q4_rx = -0.012409
        cbolt_q4_ry = -0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

#QUADRANT 3
    def test_ecc_in_plane_elastic_q3_fpx(self):
        force_px = [(2.0, 2.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_px)
        demand.calc_moments_about_centroid(force_px)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.031988
        cbolt_q1_ry = -0.031988
        cbolt_q2_rx = 0.031988
        cbolt_q2_ry = 0.031988
        cbolt_q3_rx = -0.031988
        cbolt_q3_ry = 0.031988
        cbolt_q4_rx = -0.031988
        cbolt_q4_ry = -0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q3_fnx(self):
        force_nx = [(2.0, 2.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_nx)
        demand.calc_moments_about_centroid(force_nx)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.031988
        cbolt_q1_ry = 0.031988
        cbolt_q2_rx = -0.031988
        cbolt_q2_ry = -0.031988
        cbolt_q3_rx = 0.031988
        cbolt_q3_ry = -0.031988
        cbolt_q4_rx = 0.031988
        cbolt_q4_ry = 0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q3_fpy(self):
        force_py = [(2.0, 2.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_py)
        demand.calc_moments_about_centroid(force_py)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.012409
        cbolt_q1_ry = 0.012409
        cbolt_q2_rx = -0.012409
        cbolt_q2_ry = -0.012409
        cbolt_q3_rx = 0.012409
        cbolt_q3_ry = -0.012409
        cbolt_q4_rx = 0.012409
        cbolt_q4_ry = 0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q3_fny(self):
        force_ny = [(2.0, 2.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_ny)
        demand.calc_moments_about_centroid(force_ny)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.012409
        cbolt_q1_ry = -0.012409
        cbolt_q2_rx = 0.012409
        cbolt_q2_ry = 0.012409
        cbolt_q3_rx = -0.012409
        cbolt_q3_ry = 0.012409
        cbolt_q4_rx = -0.012409
        cbolt_q4_ry = -0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

#QUADRANT 4
    def test_ecc_in_plane_elastic_q4_fpx(self):
        force_px = [(7.0, 2.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_px)
        demand.calc_moments_about_centroid(force_px)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.031988
        cbolt_q1_ry = -0.031988
        cbolt_q2_rx = 0.031988
        cbolt_q2_ry = 0.031988
        cbolt_q3_rx = -0.031988
        cbolt_q3_ry = 0.031988
        cbolt_q4_rx = -0.031988
        cbolt_q4_ry = -0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q4_fnx(self):
        force_nx = [(7.0, 2.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_nx)
        demand.calc_moments_about_centroid(force_nx)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.031988
        cbolt_q1_ry = 0.031988
        cbolt_q2_rx = -0.031988
        cbolt_q2_ry = -0.031988
        cbolt_q3_rx = 0.031988
        cbolt_q3_ry = -0.031988
        cbolt_q4_rx = 0.031988
        cbolt_q4_ry = 0.031988

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q4_fpy(self):
        force_py = [(7.0, 2.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_py)
        demand.calc_moments_about_centroid(force_py)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = 0.012409
        cbolt_q1_ry = -0.012409
        cbolt_q2_rx = 0.012409
        cbolt_q2_ry = 0.012409
        cbolt_q3_rx = -0.012409
        cbolt_q3_ry = 0.012409
        cbolt_q4_rx = -0.012409
        cbolt_q4_ry = -0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)

    def test_ecc_in_plane_elastic_q4_fny(self):
        force_ny = [(7.0, 2.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None], None, [None, None], None]
        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        j = demand.calc_j(self.bolts)
        demand.calc_force_coords_wrt_centroid(self.bolts,force_ny)
        demand.calc_moments_about_centroid(force_ny)
        demand.calc_bolt_coords_wrt_centroid(self.bolts)


        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][5][0]
        bolt_q1_ry = self.bolts[88][5][1]
        bolt_q2_rx = self.bolts[18][5][0]
        bolt_q2_ry = self.bolts[18][5][1]
        bolt_q3_rx = self.bolts[11][5][0]
        bolt_q3_ry = self.bolts[11][5][1]
        bolt_q4_rx = self.bolts[81][5][0]
        bolt_q4_ry = self.bolts[81][5][1]

        cbolt_q1_rx = -0.012409
        cbolt_q1_ry = 0.012409
        cbolt_q2_rx = -0.012409
        cbolt_q2_ry = -0.012409
        cbolt_q3_rx = 0.012409
        cbolt_q3_ry = -0.012409
        cbolt_q4_rx = 0.012409
        cbolt_q4_ry = 0.012409

        self.assertAlmostEqual(bolt_q1_rx, cbolt_q1_rx, places=3)
        self.assertAlmostEqual(bolt_q1_ry, cbolt_q1_ry, places=3)
        self.assertAlmostEqual(bolt_q2_rx, cbolt_q2_rx, places=3)
        self.assertAlmostEqual(bolt_q2_ry, cbolt_q2_ry, places=3)
        self.assertAlmostEqual(bolt_q3_rx, cbolt_q3_rx, places=3)
        self.assertAlmostEqual(bolt_q3_ry, cbolt_q3_ry, places=3)
        self.assertAlmostEqual(bolt_q4_rx, cbolt_q4_rx, places=3)
        self.assertAlmostEqual(bolt_q4_ry, cbolt_q4_ry, places=3)
       
#HELPER FUNCTIONS
    def test_calc_moments_about_centroid(self):
        cmx = 77.885
        cmy = -30.0349
        cmz = -118.3

        demand.calc_force_coords_wrt_centroid(self.bolts, self.force)

        demand.calc_moments_about_centroid(self.force)

        mx = self.force[2][0]
        my = self.force[2][1]
        mz = self.force[2][2]

        self.assertAlmostEqual(cmx, mx, places=3)
        self.assertAlmostEqual(cmy, my, places=3)
        self.assertAlmostEqual(cmz, mz, places=3)
    
    def test_calc_centroid(self):
        cx_cent = 4.50
        cy_cent = 4.50

        x_cent, y_cent = demand.calc_centroid(self.bolts)

        self.assertEqual(cx_cent, x_cent)
        self.assertEqual(cy_cent, y_cent)

    def test_calc_bolt_coords_wrt_centroid(self):
        
        cx_coords = [-4.50,-4.50,-4.50,-4.50,-4.50,-4.50,-4.50,-4.50,-4.50,-4.50,
                    -3.50,-3.50,-3.50,-3.50,-3.50,-3.50,-3.50,-3.50,-3.50,-3.50,
                    -2.50,-2.50,-2.50,-2.50,-2.50,-2.50,-2.50,-2.50,-2.50,-2.50,
                    -1.50,-1.50,-1.50,-1.50,-1.50,-1.50,-1.50,-1.50,-1.50,-1.50,
                    -0.50,-0.50,-0.50,-0.50,-0.50,-0.50,-0.50,-0.50,-0.50,-0.50,
                    0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,
                    1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50,
                    2.50,2.50,2.50,2.50,2.50,2.50,2.50,2.50,2.50,2.50,
                    3.50,3.50,3.50,3.50,3.50,3.50,3.50,3.50,3.50,3.50,
                    4.50,4.50,4.50,4.50,4.50,4.50,4.50,4.50,4.50,4.50]	
        cy_coords = [-4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50,
                     -4.50,-3.50,-2.50,-1.50,-0.50,0.50,1.50,2.50,3.50,4.50]

        demand.calc_bolt_coords_wrt_centroid(self.bolts)
        
        for bolt,cx,cy in zip(self.bolts, cx_coords, cy_coords):
            x = bolt[3][0]
            y = bolt[3][1]
            self.assertEqual(cx,x)
            self.assertEqual(cy,y)

    def test_calc_force_coords_wrt_centroid(self):
        cx = 20.0 - 4.50
        cy = 25.0 - 4.50
        cz = 5.0
        cec = 24.173

        demand.calc_force_coords_wrt_centroid(self.bolts, self.force)

        x = self.force[3][0]
        y = self.force[3][1]
        z = self.force[3][2]
        ec = self.force[4]

        self.assertAlmostEqual(cx, x, places=3)
        self.assertAlmostEqual(cy, y, places=3)
        self.assertAlmostEqual(cz, z, places=3)
        self.assertAlmostEqual(cec, ec, places=3)

    def test_calc_ixx(self):
        cixx = 825.0

        demand.calc_bolt_coords_wrt_centroid(self.bolts)

        ixx = demand.calc_ixx(self.bolts)

        self.assertEqual(cixx, ixx)

    def test_calc_iyy(self):
        ciyy = 825.0

        demand.calc_bolt_coords_wrt_centroid(self.bolts)

        iyy = demand.calc_iyy(self.bolts)

        self.assertEqual(ciyy, iyy)

    def test_calc_j(self):
        cj = 1650.0

        demand.calc_bolt_coords_wrt_centroid(self.bolts)

        j = demand.calc_j(self.bolts)

        self.assertEqual(cj, j)

