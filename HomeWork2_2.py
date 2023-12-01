def list_line_open(name_file):                                    # функция чтения , возвращает список строк
    with open(name_file, 'r', encoding = 'utf8') as f:
        list_ = [line for line in f]
        return list_

def list_line_write(sort_list_name):                                 # функция записи
    with open('return123.txt', 'a', encoding = 'utf8') as f:
        for name in sort_list_name:
            f.write(f'{name[0]}\n{name[1]}\n')                       # дописываем служебную информацию
            list_line = list_line_open(name[0])                      # запрос списка в функцию
            [f.write(line) for line in list_line]                    # пишем обьект
            f.write('\n')

list_name = ['1.txt', '2.txt', '3.txt']     # заводим вводные

dict_name = {name: len(list_line_open(name)) for name in list_name}   # формируем словарь {name: кол-во строк}
sort_list_name = sorted(dict_name.items(), key=lambda x: x[1])           # сортируем по значению

list_line_write(sort_list_name)          #  запись

# можно весь код определить как функцию и подавать на вход только список с наименованием файлов,
# но в задаче этого не требовалось


