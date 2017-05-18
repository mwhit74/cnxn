import demand
import unittest
import pdb

class TestDemand(unittest.TestCase):
    def setUp(self):
        d = 1.25
        self.bolts = []
        for x in xrange(0,10):
            for y in xrange(0,10):
                bolt_num = float(x+y)
                self.bolts.append({bolt_num:[(float(x),float(y)),d,
                                    [None, None, None]]})

        self.force = ((20.0, 25.0, 5.0),(7.54, 2.34, 4.37),[None, None, None])

    def tearDown(self):
        del self.force
        del self.bolts

    def test_shear(self):
        pass

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

        demand.calc_moments(self.force)

        self.assertEqual(cMx, self.force[2][0])
        self.assertEqual(cMy, self.force[2][1])
        self.assertEqual(cMz, self.force[2][2])

