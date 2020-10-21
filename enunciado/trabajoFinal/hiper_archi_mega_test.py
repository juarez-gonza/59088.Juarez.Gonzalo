import unittest
import os
suite = unittest.TestSuite()
loader = unittest.TestLoader()
runner = unittest.TextTestRunner()
tests = loader.discover(os.path.dirname(os.path.abspath(__file__)), "test*.py")
suite.addTests(tests)
runner.run(suite)
