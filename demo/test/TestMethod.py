
import  unittest
from demo import RunMain

class TestMethod(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls) -> None:
        print('类执行之后的方法')

    def setUp(self):
        url2 = 'http://192.168.10.166:9006/rest/sxreader/getAllTeacherTaskInfos?activity=0&condition=&indexPage=1&pageSize=12&status=unfinished&userId=60da42581d4b11eaa0046c92bf28f871'
        res_data = dict(
            userid=111,
            extno=""
        )
        run = RunMain(url2,'GET',res_data)
        print('这个是开始执行的方法')


    def tearDown(self):
        print('这个是执行之后的方法')

    def test_01(self):
        print('这个是测试用例')
    def test_02(self):
        print('这个是测试用例2')
if __name__ == '__main__':
    unittest.main()




