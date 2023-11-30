with open('recept.txt', 'r', encoding = 'utf8') as f:
  list_line = [line.strip() for line in f]                       # получаем список строк

def ingradient_dict(ingradient):                                   # формирует подсловарь словаря ингридиентов
    ingradient_keys = ['ingredient_name', 'quantity', 'measure']
    ingradient_values = [ingradient[0].strip(), ingradient[1].strip(), ingradient[2].strip()]
    return dict(zip(ingradient_keys, ingradient_values))

cooke_booke = {}
list_ingradient = []
for idx, el in enumerate(list_line):
    if idx == 0:                                                 # блок первого ключа словаря cooke_booke
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

for key, val in cooke_booke.items():
    print(f'{key}\n{val}')
