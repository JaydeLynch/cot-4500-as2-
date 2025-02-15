{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import unittest\
from src.main.assignment_2 import neville_method, newton_forward, divided_difference, cubic_spline\
\
class TestAssignment2(unittest.TestCase):\
    def test_neville_method(self):\
        x = [3.6, 3.8, 3.9]\
        y = [1.675, 1.436, 1.318]\
        target = 3.7\
        result = neville_method(x, y, target)\
        self.assertAlmostEqual(result, 1.554999999999995, places=10)\
    \
    def test_newton_forward(self):\
        x = [7.2, 7.4, 7.5, 7.6]\
        y = [23.5492, 25.3913, 26.8224, 27.4589]\
        target = 7.3\
        result = newton_forward(x, y, target)\
        self.assertAlmostEqual(result, 24.47718457889519, places=10)\
    \
    def test_divided_difference(self):\
        x = [3.6, 3.8, 3.9]\
        y = [1.675, 1.436, 1.318]\
        y_prime = [-1.195, -1.188, -1.180]\
        result = divided_difference(x, y, y_prime)\
        expected = np.array([\
            [3.6, 1.675, 0, 0, 0],\
            [3.6, 1.675, -1.195, 0, 0],\
            [3.8, 1.436, -1.195, -9.99200722e-15, 0],\
            [3.8, 1.436, -1.188, 3.50000000e-02, 1.75000000e-01],\
            [3.9, 1.318, -1.180, 8.00000000e-02, -1.28571429e-02],\
            [3.9, 1.318, -1.182, -2.00000000e-02, -1.00000000e+00]\
        ])\
        np.testing.assert_array_almost_equal(result, expected, decimal=10)\
    \
    def test_cubic_spline(self):\
        x = [2, 5, 8, 10]\
        y = [3, 5, 7, 9]\
        A, b, c = cubic_spline(x, y)\
        expected_A = np.array([\
            [1, 0, 0, 0],\
            [3, 12, 3, 0],\
            [0, 3, 10, 2],\
            [0, 0, 0, 1]\
        ])\
        expected_b = np.array([0, -0.02702703, 0.10810811, 0])\
        expected_c = np.array([0, 0, 1, 0])\
        np.testing.assert_array_almost_equal(A, expected_A, decimal=10)\
        np.testing.assert_array_almost_equal(b, expected_b, decimal=10)\
        np.testing.assert_array_almost_equal(c, expected_c, decimal=10)\
\
if __name__ == "__main__":\
    unittest.main()}