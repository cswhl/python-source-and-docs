import web_server as ws
import unittest
import types

class test_HttpHandler(unittest.TestCase):
    pass

class test_CliParam(unittest.TestCase):
    param0 = 'web_server.py mini_frame:application'.split()
    param1 = 'web_server.py 9999  mini_frame:application'.split()
    param2 = 'web_server.py sc9 mini_frame:application'.split()
    param3 = 'web_server.py 9999 :application'.split()
    param4 = 'web_server.py 9999 mini_frame:application'.split()

    def test_is_validate_param_num(self):
        test_ins1 = ws.CliParam(self.param0)
        self.assertEqual(bool(test_ins1._is_validate_param_num()), False)
        test_ins2 = ws.CliParam(self.param1)
        self.assertEqual(test_ins2._is_validate_param_num(), True)

    def test_port(self):
        test_ins1 = ws.CliParam(self.param2)
        self.assertEqual(test_ins1._get_port(), None)
        test_ins2 = ws.CliParam(self.param1)
        self.assertEqual(test_ins2._get_port(), '9999')

    def test_frame_app(self):
        test_ins1 = ws.CliParam(self.param3)
        self.assertEqual(test_ins1._get_app_of_frame(), None)
        test_ins2 = ws.CliParam(self.param4)
        self.assertIsInstance(test_ins2._get_app_of_frame(), types.FunctionType)

class test_get_conf(unitest.TestCase):
    pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_CliParam('test_is_validate_param_num'))
    suite.addTest(test_CliParam('test_port'))
    suite.addTest(test_CliParam('test_frame_app'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())  # 执行测试套件
