from openpyxl import load_workbook
from datetime import datetime
from interface import interface

# {'date': '02/05/2023', 'customer_name': 'Волобуев Алексей', 'customer_number': '89539106192',
# 'tire_size_width': 215, 'tire_size_profile': 55, 'tire_size_diameter': 'R16',
# 'tire_brand': 'Tunga', 'tire_model': 'Zodiak 2', 'car_model': 'nissan cube', 'license_plate': 'k602tm',
# 'check_number': '123123', 'manager': 'Шараев'}

user_data = interface()

tire_size = f'{user_data["tire_size_width"]}/{user_data["tire_size_profile"]} {user_data["tire_size_diameter"]}'

date, customer_name, customer_number, tire_brand, tire_model, car_model, license_plate, check_number, manager = user_data["date"],\
    user_data["customer_name"], user_data["customer_number"], user_data["tire_brand"],\
    user_data["tire_model"], user_data["car_model"], user_data["license_plate"],\
    user_data["check_number"], user_data["manager"]


def fill_warranty_list(date, customer_name, customer_number, tire_brand, tire_model, tire_size, car_model, license_plate, check_number, manager):
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

fill_warranty_list(date, customer_name, customer_number, tire_brand, tire_model, tire_size, car_model, license_plate, check_number, manager)

