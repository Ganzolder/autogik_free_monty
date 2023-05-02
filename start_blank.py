import get_base_parameters
import interface
from budget_control import budget_control
from fill_warranty_list import fill_warranty_list

parameters_for_budget = interface.interface()

tire_brand = parameters_for_budget['tire_brand']
tire_model = parameters_for_budget['tire_model']
tire_size_diameter = parameters_for_budget['tire_size_diameter']

base_parameters = get_base_parameters.get_base_parameters()
compensation_dict = base_parameters[6].copy()
brands_budgets = base_parameters[7].copy()

tire_size = f'{parameters_for_budget["tire_size_width"]}/{parameters_for_budget["tire_size_profile"]} {parameters_for_budget["tire_size_diameter"]}'

date, customer_name, customer_number, tire_brand, tire_model, car_model, license_plate, check_number, manager, unique_code = parameters_for_budget["date"],\
    parameters_for_budget["customer_name"], parameters_for_budget["customer_number"], parameters_for_budget["tire_brand"],\
    parameters_for_budget["tire_model"], parameters_for_budget["car_model"], parameters_for_budget["license_plate"],\
    parameters_for_budget["check_number"], parameters_for_budget["manager"], parameters_for_budget["unique_code"]

fill_warranty_list(date, customer_name, customer_number, tire_brand, tire_model, tire_size, car_model, license_plate, check_number, manager, unique_code)

budget_control(tire_brand, tire_size_diameter, brands_budgets, compensation_dict)

