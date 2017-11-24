import random


def field(my_list,*args):
    if len(args) == 1:
            for el in my_list:
                for k, val in el.items():
                    if k == args[0]:
                        yield val
    else:
        for el in my_list:
            my_dict = {k: v for k, v in el.items() for arg in args if k == arg}
            yield my_dict


def gen_random(start,fin, count):
    for i in range(0,count):
        yield random.randint(start,fin)
