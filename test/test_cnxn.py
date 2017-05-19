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
        crx = 7.54/num_bolts
        cry = 2.34/num_bolts
        demand.shear(self.bolts, self.force)

        for bolt in self.bolts:
            rx = bolt[4][0]
            ry = bolt[4][1]
            self.assertEqual(crx, rx)
            self.assertEqual(cry, ry)

    def test_calc_moments(self):
        x = self.force[0][0]
        y = self.force[0][1]
        z = self.force[0][2]

        Px = self.force[1][0]
        Py = self.force[1][1]
        Pz = self.force[1][2]

        cMx = Pz*y - Py*z
        cMy = Px*z - Pz*x
        cMz = Py*x - Px*y

        demand.calc_moments(self.bolts, self.force)

        self.assertEqual(cMx, self.force[2][0])
        self.assertEqual(cMy, self.force[2][1])
        self.assertEqual(cMz, self.force[2][2])
    
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

        ixx = demand.calc_ixx(self.bolts)

        self.assertEqual(cixx, ixx)

    def test_calc_iyy(self):
        ciyy = 825.0

        iyy = demand.calc_iyy(self.bolts)

        self.assertEqual(ciyy, iyy)

    def test_calc_j(self):
        cj = 1650.0

        j = demand.calc_j(self.bolts)

        self.assertEqual(cj, j)

