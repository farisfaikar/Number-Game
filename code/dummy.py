from _winreg import *

xyzKey = CreateKey(HKEY_CLASSES_ROOT, ".xyz")
SetValue(xyzKey, None, REG_SZ, "MyTest.xyz")
CloseKey(xyzKey)

myTestKey = CreateKey(HKEY_CLASSES_ROOT, "MyTest.xyz")
iconKey= CreateKey(myTestKey, "DefaultIcon")
CloseKey(myTestKey)

SetValue(iconKey, None, REG_SZ, "D:\\Python25\\python.exe")
CloseKey(iconKey)