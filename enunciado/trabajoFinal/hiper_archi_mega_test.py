import unittest
import os
suite = unittest.TestSuite()
loader = unittest.TestLoader()
runner = unittest.TextTestRunner()
tests = loader.discover(os.path.abspath("."), "test*.py")
suite.addTests(tests)
runner.run(suite)
