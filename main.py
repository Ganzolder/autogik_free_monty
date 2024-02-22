import get_base_parameters
import interface
from budget_control import budget_control
from fill_warranty_list import fill_warranty_list
from PDF_creator import create_pdf
import os


if __name__ == '__main__':

    stop = 0
    while stop != 'Отмена':
        parameters_for_budget = interface.interface()[0]

        tire_brand = parameters_for_budget['tire_brand']
        tire_model = parameters_for_budget['tire_model']
        tire_size_diameter = parameters_for_budget['tire_size_diameter']

        base_parameters = get_base_parameters.get_base_parameters()
        compensation_dict = base_parameters[7].copy()
        brands_budgets = base_parameters[8].copy()

        tire_size = f'{parameters_for_budget["tire_size_width"]}/{parameters_for_budget["tire_size_profile"]} {parameters_for_budget["tire_size_diameter"]}'

        customer_name, customer_number, tire_brand, tire_model, tire_season, check_sum, NFD, check_number, manager, unique_code, check_sum =\
            parameters_for_budget["customer_name"], parameters_for_budget["customer_number"], parameters_for_budget["tire_brand"],\
            parameters_for_budget["tire_model"], parameters_for_budget['tire_season'], parameters_for_budget["check_sum"], parameters_for_budget["NFD"],\
            parameters_for_budget["check_number"], parameters_for_budget["manager"], parameters_for_budget["unique_code"], parameters_for_budget["check_sum"]

        fill_warranty_list(customer_name, customer_number, tire_brand, tire_model, tire_size, tire_season, check_sum, NFD, check_number, manager, unique_code)

        budget_control(tire_brand, tire_size_diameter, brands_budgets, compensation_dict)

        os.makedirs(f"cupons/{tire_brand}", exist_ok=True)
        file_path = f"cupons/{tire_brand}/{unique_code}"+".pdf"

        os.makedirs(f"c:/cupons/", exist_ok=True)
        file_path_for_manager = f"c:/cupons/{unique_code}" + ".pdf"

        create_pdf(file_path, customer_name, tire_size, tire_brand, tire_model, customer_number, NFD, check_number)
        create_pdf(file_path_for_manager, customer_name, tire_size, tire_brand, tire_model, customer_number, NFD, check_number)

