import csv
import re


def write_to_csv(file, data):
    with open(file, 'w') as f_obj1:
        f_obj_writer = csv.writer(f_obj1)
        for row in data:
            f_obj_writer.writerow(row)


def get_data(list_1):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in list_1:
        with open(i, encoding='cp1251') as file_1:
            file = file_1.read()
        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(file)[0].split()[2])
        os_prod_reg = re.compile(r'Название ОС:\s*\S*')
        os_name_list.append(os_prod_reg.findall(file)[0].split()[2])
        os_prod_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_prod_reg.findall(file)[0].split()[2])
        os_prod_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_prod_reg.findall(file)[0].split()[2])

    for i in range(len(list_1)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


result = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
write_to_csv('data_report_new.csv', result)

with open('data_report_new.csv') as f_obj2:
    print(f_obj2.read())
