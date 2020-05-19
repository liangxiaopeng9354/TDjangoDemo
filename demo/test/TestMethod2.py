
import  unittest
from demo2 import RunMain
import HTMLTestRunner
import fileinput

class TestMethod(unittest.TestCase):


    def setUp(self):

        self.run = RunMain()


        print('这个是开始执行的方法')


    def tearDown(self):
        print('这个是执行之后的方法')

    def test_01(self):
        url2 = 'http://192.168.10.166:9006/rest/sxreader/getAllTeacherTaskInfos?activity=0&condition=&indexPage=1&pageSize=12&status=unfinished&userId=60da42581d4b11eaa0046c92bf28f871'
        res_data = dict(
            userid=111,
            extno=""
        )
        res = self.run.run_main(url2,'GET',res_data)
        self.assertEqual(res['code'],200, msg = '测试通过')
        print(res)


    def test_02(self):
        url = 'http://192.168.10.166:9006/login'
        data = {'username': '232323', 'password': '232323'}
        res2 = self.run.run_main(url,'POST',data)
        self.assertEqual(res2['userName'],'232323',msg='测试通过')
        print(res2)

        print('这个是测试用例2')
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    file_html = 'F:\work\htmlreport.html'
    fp = open(file_html,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is my first report').run(suite)
    fp.close()

    #unittest.TextTestRunner().run(suite)

