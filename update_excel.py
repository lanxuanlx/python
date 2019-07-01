import xlwt
import xlrd
from xlutils.copy import copy

w = copy('test.xls')
w.get_sheet(0).write(0,0,"foo")
w.save('test1.xls')