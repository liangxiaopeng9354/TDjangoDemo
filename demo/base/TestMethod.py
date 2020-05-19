
import  unittest
from demo import RunMain
import json

class TestMethod(unittest.TestCase):


    def setUp(self):
        self.run=RunMain()

        print('这个是开始执行的方法')
    def tearDown(self):
        print('这个是执行之后的方法')

    def test_01(self):
        url = 'https://sxreader.com:9006/login'
        data={'username':'232323','password':'232323'}
        res=self.run.run_main(url,'POST',data)
        self.assertEqual(res['userName'],'232323','测试失败')
        print(res)
        print(type(res))
        #self.assertEqual()
'''
    def test_02(self):
        url2 = 'https://sxreader.com:9006/rest/sxreader/getAllTeacherTaskInfos?activity=0&condition=&indexPage=1&pageSize=12&status=unfinished&userId=60da42581d4b11eaa0046c92bf28f871'
        res_data = dict(
            userid=111,
            extno=""
        )
        res=self.run.run_main(url2,'GET',res_data)
        print(res)
'''
if __name__ == '__main__':
    unittest.main()




