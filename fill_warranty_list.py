from openpyxl import load_workbook
from datetime import datetime

date, customer_name, customer_number, tire_brand, tire_model, tire_size, car_model, license_plate, check_number, manager = \
    '01/03/1986', 'Ленин ВИ', '89539106192', 'Pirelli', 'P1 Verde', '195/65 R15', 'Nissan Сube', 'К602ТМ42', '65496864565', 'Волобуев'

def fill_warranty_list(date, customer_name, customer_number, tire_brand, tire_model,
                       tire_size, car_model, license_plate, check_number, manager):
    # открываем список бшм и делаем запись в последнюю пустую строку

    time_stamp = datetime.now()
    form_data = [date, customer_name, customer_number, tire_brand, tire_model,
                 tire_size, car_model, license_plate, check_number, manager, time_stamp]

    wb_warranty_list = load_workbook(filename='base/warranty_list.xlsx')
    wb_warranty_list_sheet = wb_warranty_list.worksheets[0]

    for row in wb_warranty_list_sheet.iter_rows(min_row=1, min_col=1, max_col=11):
        step = 0
        for cell in row:
            if cell.offset(row=1).value == None:
                cell.offset(row=1).value = form_data[step]
            step += 1

    wb_warranty_list.save(filename='base/warranty_list.xlsx')


fill_warranty_list(date, customer_name, customer_number, tire_brand, tire_model,
                   tire_size, car_model, license_plate, check_number, manager)
