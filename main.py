# coding=utf-8
import win32com.client
import os

os.system('regsvr32 djjj.dll /s')
os.system('regsvr32 RegDll.dll /s')
dm = win32com.client.Dispatch('dm.dmsoft')


if dm.Ver() == '3.1233':
	print('注册成功  大漠版本为')
else:
	print ('djjj版本不对')
	exit()


#此大漠版本位3.1233
#接下来复制大漠接口说明文档中的示例就可以运行 