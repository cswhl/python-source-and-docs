from web_server import *
import unittest


class test_CliParam(unittest.TestCase):
    def test_param_num(self):
        param = 'web_server.py 9999  mini_frame:application'.split()
        self.assertEqual(get_param_num(param), True)

    def test_port(self):
        param = 'web_server.py 9999 mini_frame:application'.split()
        self.assertEqual(get_port(param).isdigit(), True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_CliParam('test_param_num'))
    suite.addTest(test_CliParam('test_port'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())  # 执行测试套件
