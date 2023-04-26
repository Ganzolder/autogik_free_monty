from openpyxl import load_workbook

#  date, customer_name, customer_number, tire_brand, tire_model,
#  tire_size_width, tire_size_profile, tire_size_diameter, car_model, license_plate, check_number, manager
def get_base_parameters():
    wb_base_list = load_workbook(filename='base/base.xlsx')
    wb_base_list_sheet = wb_base_list['managers']
    # print(wb_base_list.sheetnames)
    managers = []
    tire_size_width = []
    tire_size_profile = []
    tire_size_diameter=[]

    for row in wb_base_list_sheet.iter_rows(min_row=2, min_col=1, max_col=1):
        for cell in row:
            managers.append(cell.value)

    wb_base_list_sheet = wb_base_list['sizes']

    for row in wb_base_list_sheet.iter_rows(min_row=2, min_col=1, max_col=1):
        for cell in row:
            if cell.value != None:
                tire_size_width.append(cell.value)
            else:
                break

    for row in wb_base_list_sheet.iter_rows(min_row=2, min_col=2, max_col=2):
        for cell in row:
            if cell.value != None:
                tire_size_profile.append(cell.value)
            else:
                break

    for row in wb_base_list_sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        for cell in row:
            if cell.value != None:
                tire_size_diameter.append(cell.value)
            else:
                break

    return managers, tire_size_width, tire_size_profile, tire_size_diameter


