list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9], [10, 11, 12]]


def unpack():
    try:
        list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9], [10, 11, 12]]
        new_list = [int(num) for row in list_ for num in row]
    except Exception as e:
        new_list = [int(num) for row in list_ for num in row if type(num) == (int)]
    finally:
        print(new_list)

unpack()






















# new_list = []
# for i, x in enumerate(list_):
#     if type(x) == type([]):
#         for k in list_[i]:
#             if type(x) == type([]):
#                 for j in list_[i]:
#                     try:    
#                         if type(j) != type([]):
#                             raise Exception("Error")
#                     except Exception:
#                         if j not in new_list and type(j) == type(2):
#                             new_list.append(j)

# print(new_list)