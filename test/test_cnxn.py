import demand
import unittest
import pdb
import os.path

class TestDemand(unittest.TestCase):
    def setUp(self):
        d = 1.25
        self.bolts = []
        for x in xrange(0,10):
            for y in xrange(0,10):
                bolt_num = float(x+y+1)
                self.bolts.append([bolt_num,(float(x),float(y)),d,[None, None],
                                    [None, None, None]])

        self.force = [(20.0, 25.0, 5.0),(7.54, 2.34, 4.37),[None, None, None],
                [None, None, None]]

    def tearDown(self):
        del self.force
        del self.bolts

    def test_shear(self):
        num_bolts = 100.0
        crx = -7.54/num_bolts
        cry = -2.34/num_bolts

        demand.shear(self.bolts, self.force)

        for bolt in self.bolts:
            rx = bolt[4][0]
            ry = bolt[4][1]
            self.assertEqual(crx, rx)
            self.assertEqual(cry, ry)

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_px = [(7.0, 6.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_px)

        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_nx = [(7.0, 6.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]
        
        demand.ecc_in_plane_elastic(self.bolts, force_nx)

        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_py = [(7.0, 6.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_py)

        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_ny = [(7.0, 6.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_px = [(2.0, 6.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_nx = [(2.0, 6.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_py = [(2.0, 6.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_ny = [(2.0, 6.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_px = [(2.0, 2.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_nx = [(2.0, 2.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_py = [(2.0, 2.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_ny = [(2.0, 2.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_px = [(7.0, 2.5, 5.0),(7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_px)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_nx = [(7.0, 2.5, 5.0),(-7.54, 0.0, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_nx)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_py = [(7.0, 2.5, 5.0),(0.0, 2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_py)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        demand.calc_moments(self.bolts, self.force)
        demand.calc_local_bolt_coords(self.bolts)

        force_ny = [(7.0, 2.5, 5.0),(0.0, -2.34, 0.0),[None, None, None],
                            [None, None, None]]

        demand.ecc_in_plane_elastic(self.bolts, force_ny)
    
        bolt_q1_rx = self.bolts[88][4][0]
        bolt_q1_ry = self.bolts[88][4][1]
        bolt_q2_rx = self.bolts[18][4][0]
        bolt_q2_ry = self.bolts[18][4][1]
        bolt_q3_rx = self.bolts[11][4][0]
        bolt_q3_ry = self.bolts[11][4][1]
        bolt_q4_rx = self.bolts[81][4][0]
        bolt_q4_ry = self.bolts[81][4][1]

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
        
    def test_calc_moments(self):
        cmx = 77.885
        cmy = -30.0349
        cmz = -118.3

        demand.calc_local_force_coords(self.bolts, self.force)

        demand.calc_moments(self.bolts, self.force)

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

    def test_local_bolt_coords(self):
        cx_coords = []
        cy_coords = []
        __location__ = os.path.realpath(
                        os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, r'local_bolt_coords.txt'), 'rb') as ifile:
            data = ifile.readlines()
            for line in data:
                x = float(line.split("\t")[0].strip())
                y = float(line.split("\t")[1].strip())
                cx_coords.append(x)
                cy_coords.append(y)
            ifile.close()


        demand.calc_local_bolt_coords(self.bolts)
        
        for bolt,cx,cy in zip(self.bolts, cx_coords, cy_coords):
            x = bolt[3][0]
            y = bolt[3][1]
            self.assertEqual(cx,x)
            self.assertEqual(cy,y)

    def test_local_force_coords(self):
        cx = 20.0 - 4.50
        cy = 25.0 - 4.50
        cz = 5.0

        demand.calc_local_force_coords(self.bolts, self.force)

        x = self.force[3][0]
        y = self.force[3][1]
        z = self.force[3][2]

        self.assertEqual(cx, x)
        self.assertEqual(cy, y)
        self.assertEqual(cz, z)

    def test_calc_ixx(self):
        cixx = 825.0

        demand.calc_local_bolt_coords(self.bolts)

        ixx = demand.calc_ixx(self.bolts)

        self.assertEqual(cixx, ixx)

    def test_calc_iyy(self):
        ciyy = 825.0

        demand.calc_local_bolt_coords(self.bolts)

        iyy = demand.calc_iyy(self.bolts)

        self.assertEqual(ciyy, iyy)

    def test_calc_j(self):
        cj = 1650.0

        demand.calc_local_bolt_coords(self.bolts)

        j = demand.calc_j(self.bolts)

        self.assertEqual(cj, j)

