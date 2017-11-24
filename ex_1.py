from librip.gens import field,gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

field_1 = field(goods, 'title')
print(', '.join(map(str,field_1)))

field_2 = field(goods, 'title','price')
print(', '.join(map(str,field_2)))

gen_1 = gen_random(1,3,5)
print(', '.join(map(str,gen_1)))