with open('recept.txt', 'r', encoding = 'utf8') as f:
  list_line = [line.strip() for line in f]                       # получаем список строк

def ingradient_dict(ingradient):                                   # формирует подсловарь словаря ингридиентов
    ingradient_keys = ['ingredient_name', 'quantity', 'measure']
    ingradient_values = [ingradient[0].strip(), ingradient[1].strip(), ingradient[2].strip()]
    return dict(zip(ingradient_keys, ingradient_values))

cooke_booke = {}
list_ingradient = []
for idx, el in enumerate(list_line):
    if idx == 0 and len(el) !=0:                                   # блок первого ключа словаря cooke_booke
        quantity = int(list_line[1])
        for i in range(quantity):
            ingradient = list_line[idx+2+i].split('|')
            list_ingradient += [(ingradient_dict(ingradient))]    # формируем список словарей ингридиентов
        cooke_booke.update({list_line[0]: list_ingradient})

    if len(el) == 0:                                              # блок всех последующих ключей словаря cooke_booke
        list_ingradient = []
        quantity = int(list_line[idx + 2])
        for i in range(quantity):
            ingradient = list_line[idx+3+i].split('|')
            list_ingradient += [(ingradient_dict(ingradient))]    # формируем список словарей ингридиентов
        cooke_booke.update({list_line[idx + 1]: list_ingradient})

def get_shop_list_by_dishes(dishes, person_count):        # формирует словарь ингридиентов по блюду с учетом кол-ва
    dict_by_dishes = {}
    for dish in dishes:
        for el in cooke_booke[dish]:
            el['quantity'] = int(el['quantity']) * person_count
            ingredient_ = el.pop('ingredient_name')
            dict_by_dishes.update({ingredient_: el})
    return dict_by_dishes

#for key, val in cooke_booke.items():                            # проверка вывода
#    print(f'{key}\n{val}')

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
print(get_shop_list_by_dishes(dishes, person_count))              # проверка вывода
