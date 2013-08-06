'''
Created on 26/07/2013

@author: dominik
'''
import unittest
from lib.UICasilla import _cIdToGroup


class Test(unittest.TestCase):

    def test_cIdToGroup(self):
        res1 = _cIdToGroup(0)
        self.assertEqual(res1[0], 0, "cId 0 was not in group 0")
        self.assertEqual(res1[1], 0, "cId 0 had no excess of 0")

        res2 = _cIdToGroup(80)
        self.assertEqual(res2[0], 8, "cId 80 was not in group 8")
        self.assertEqual(res2[1], 8, "cId 80 had no excess of 8")
       
        res3 = _cIdToGroup(7)
        self.assertEqual(res3[0], 2, "cId 7 was not in group 2")
        self.assertEqual(res3[1], 1, "cId 7 had no excess of 1")

        res4 = _cIdToGroup(68)
        self.assertEqual(res4[0], 7, "cId 68 was not in group 7")
        self.assertEqual(res4[1], 5, "cId 68 had no excess of 5")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()