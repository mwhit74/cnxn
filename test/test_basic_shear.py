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
