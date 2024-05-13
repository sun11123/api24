import xlrd


class read_excel():
    def excel_to_list(self,filename,sheetname):
        wb=xlrd.open_workbook(filename)
        sh=wb.sheet_by_name(sheetname)
        list=[]
        keys=sh.row_values(0)
        for i in range(1,sh.nrows):
            v=sh.row_values(i)
            list.append(dict(zip(keys,v)))
        return list

    def get_test_data(self,data_list,case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data

if __name__=='__main__':
    r=read_excel()
    l=r.excel_to_list("test_user_reg",'test_user_login')
    print(l)