# import os.path
# a = os.path.abspath(".")
# b = os.path.dirname(os.path.abspath(".")) + '\\test_data\\test.xlsx'
# print(a)
#
# print(b)

dict1 = {'errCode': '', 'data': None, 'code': 0, 'requestId': '6d2caa0abefaa4e5', 'msg': 'success'}
dict2 = {"w": '',"q": ''}
dict3 = dict(dict1,**dict2)
print(dict3)
