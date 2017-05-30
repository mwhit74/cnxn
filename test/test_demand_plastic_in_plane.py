import demand
import unittest
import pdb

class TestDemandPlasticInPlane(unittest.TestCase):

    def setUp(self):
        self.bolts1 = []
        self.force1 = []

        self.bolts2 = []
        self.force2 = []

    def tearDown(self):
