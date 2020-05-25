#
#
chinese_zodic = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#
zodic_name = (u'摩羯座',u'宝瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'室女座',u'天秤座',u'天蝎座',u'人马座')

zodic_mouth = ((1,20),(2,19),(3,23),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
#

ch_num = {}
zc_num = {}
for i in chinese_zodic:
    ch_num[i] = 0

for i in zodic_name:
    zc_num[i] = 0






while True:

    year = int(input("请输入年份："))
    int_month = int(input('请输入一个月份：'))
    int_day = int(input('请输入一个日期：'))

    zodic_day = filter(lambda x: x <=(int_month,int_day),zodic_mouth)
    zodic_len = len(list(zodic_day)) % 12

    n = 0

    while zodic_mouth[n] < (int_month,int_day):
        if int_month == 12 and int_day > 23:
            break
        n = n +1


    print(zodic_name[zodic_len])

    ch_num[chinese_zodic[year % 12]] += 1
    zc_num[zodic_name[zodic_len]] +=1


    for each_key in ch_num.keys():
        print("each_key这个是：",each_key)
        print("生肖是 %s 的有 %d 个"%(each_key,ch_num[each_key]))

    for each_key in zc_num.keys():
        print("星座是 %s 的有 %d 个"%(each_key,zc_num[each_key]))
























# n = 0
#
# while zodic_mouth[n] < (int_month,int_day):
#     if int_month == 12 and int_day > 23:
#         break
#     n = n +1
# #print(zodic_name[n])

import time
#
# num = 5
# while True:
#
#     num = num +1
#     if num == 10:
#         continue
#     print(num)
#     time.sleep(1)



# for zd_num in range(len(zodic_mouth)):
#     if zodic_mouth[zd_num] >= (int_month,int_day):
#         print(zodic_name[zd_num])
#         break
#
#     elif int_month==12 and int_day > 24 and int_day<32:
#         print(zodic_name[0])
#         break
#     elif int_month>12:
#         print('请输入正确的月份和天')
#         break



