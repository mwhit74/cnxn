import demand
import unittest
import pdb

class TestDemandPlasticInPlane(unittest.TestCase):

    def setUp(self):
        self.bolts1 = [[1,(0.0, 0.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [2,(0.0, 3.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [3,(0.0, 6.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]]]

        self.force1 = [(4.0, 0.0, 0.0), (0.0, -1.0, 0.0), [None, None, None],
                        [None, None, None]]

        self.bolts2 = [[1,(0.0, 0.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [2,(0.0, 3.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [3,(0.0, 6.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [4,(6.0, 0.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [5,(6.0, 3.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]],
                      [6,(6.0, 6.0), 1.0, [None, None], [None, None, None],
                       [None, None], None, None, None, [None, None]]]
        self.force2 = [(23.0, 8.0, 0.0), (0.6, -0.8, 0.0), [None, None, None],
                        [None, None, None]]

    def tearDown(self):
        del self.bolts1
        del self.force1
        del self.bolts2
        del self.force2

    def test_calc_instanteous_center_1(self):
        demand.calc_local_bolt_coords(self.bolts1)
        demand.calc_local_force_coords(self.bolts1, self.force1)
        demand.calc_moments_about_centroid(self.bolts1, self.force1)

        cx_ic = -1.5
        cy_ic = 0.0

        fx = self.force1[1][0]
        fy = self.force1[1][1]
        mo = self.force1[2][2]

        x_ic, y_ic = demand.calc_instanteous_center(self.bolts1, fx, fy, mo)

        self.assertAlmostEqual(cx_ic, x_ic, places=3)
        self.assertAlmostEqual(cy_ic, y_ic, places=3)


    def test_calc_instanteous_center_2(self):
        demand.calc_local_bolt_coords(self.bolts2)
        demand.calc_local_force_coords(self.bolts2, self.force2)
        demand.calc_moments_about_centroid(self.bolts2, self.force2)

        cx_ic = -0.632 
        cy_ic = -0.474 

        fx = self.force2[1][0]
        fy = self.force2[1][1]
        mo = self.force2[2][2]

        x_ic, y_ic = demand.calc_instanteous_center(self.bolts2, fx, fy, mo)

        self.assertAlmostEqual(cx_ic, x_ic, places=3)
        self.assertAlmostEqual(cy_ic, y_ic, places=3)

    def test_calc_d_1(self):
        demand.calc_local_bolt_coords(self.bolts1)
        demand.calc_local_force_coords(self.bolts1, self.force1)
        demand.calc_moments_about_centroid(self.bolts1, self.force1)
        fx = self.force1[1][0]
        fy = self.force1[1][1]
        mo = self.force1[2][2]
        x_ic, y_ic = demand.calc_instanteous_center(self.bolts1, fx, fy, mo)

        demand.calc_d(self.bolts1, x_ic, y_ic)

        cd  = [3.354, 1.5, 3.354]

        for bolt, d in zip(self.bolts1, cd):
            self.assertAlmostEqual(bolt[6], d, places=3)

    def test_calc_d_2(self):
        demand.calc_local_bolt_coords(self.bolts2)
        demand.calc_local_force_coords(self.bolts2, self.force2)
        demand.calc_moments_about_centroid(self.bolts2, self.force2)
        fx = self.force2[1][0]
        fy = self.force2[1][1]
        mo = self.force2[2][2]
        x_ic, y_ic = demand.calc_instanteous_center(self.bolts2, fx, fy, mo)

        demand.calc_d(self.bolts2, x_ic, y_ic)

        cd  = [3.463,2.415,4.204,4.424,3.662,5.025]

        for bolt, d in zip(self.bolts2, cd):
            self.assertAlmostEqual(bolt[6], d, places=3)

    def test_calc_mp_1(self):
        demand.calc_local_bolt_coords(self.bolts1)
        demand.calc_local_force_coords(self.bolts1, self.force1)
        demand.calc_moments_about_centroid(self.bolts1, self.force1)
        fx = self.force1[1][0]
        fy = self.force1[1][1]
        mo = self.force1[2][2]
        x_ic, y_ic = demand.calc_instanteous_center(self.bolts1, fx, fy, mo)

        
