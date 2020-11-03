# coding=utf-8
import xlrd

class ExcelReadUtil(object):
    """excel文件读取类"""


    def getSheetValue( self,filename,index ):
        """获取sheet内容"""
        book = xlrd.open_workbook(filename) #打开Excel文件读取数据
        sheet =book.sheets()[index-1] #指定工作表
        return sheet


    def getRowsClosNum( self,sheet):
        """获取表格的总行数和总列数"""
        rows = sheet.nrows
        columns = sheet.ncols
        return rows, columns

    def getCellValue( self,sheet,row,column):
        """获取某个单元格的值"""
        cell = sheet.cell(row+1,column+1).ctype
        return cell

    def getColValues( self,sheet,column ):
        """获取某列的所有值"""
        return sheet.col_values(column-1)

    def getRowValues( self,sheet,row ):
        """获取某行的所有值"""

        return sheet.row_values(row-1)
