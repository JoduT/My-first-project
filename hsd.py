# def strcounter(s):
#     for el in set(s):
#         counter = 0
#         for sub_el in s:
#             if sub_el == el:
#                 counter += 1
#         print(el, counter)
#
# strcounter('abbcd')

def strcounter(s):
    el_counter = {}
    for el in s:
        el_counter[el] = el_counter.get(el, 0) + 1
    for el, count in el_counter.items():
        print(el, count)

strcounter('abbcd')