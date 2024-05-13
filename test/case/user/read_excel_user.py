import xlrd
wb=xlrd.open_workbook("../../test_user_data.xlsx")
sheet1=wb.sheet_by_name("text_user_reg")
print(sheet1.nrows)
print(sheet1.ncols)
print(sheet1.cell(0,0).value)
for i in range(sheet1.nrows):
    print(sheet1.row_values(i))