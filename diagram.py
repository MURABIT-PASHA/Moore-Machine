#
# def convert():
#
#
#     # ilk giriş state'ini bu değişkende tutalım
#     first_input = ''
#
#     # Geçiş tablosunun okunup, oluşturulması
#     with open(directory + "\\table.txt", "r") as f:
#         ingredients = f.readlines()
#
#         title = ingredients[0]
#         inputs = title.strip().split(sep='\t')[1:]
#
#         input_amount = len(inputs)
#
#         say = 0
#         for line in ingredients[1:]:
#             row = line.strip().split(sep='\t')
#             d = {inputs[p]: row[p + 1] for p in range(input_amount)}
#             transition_table[row[0]] = d
#             if say == 0:
#                 first_input = row[0]
#             say = say + 1
#
#     with open(directory + "\\output.txt") as f:
#         ingredients = f.readlines()
#
#         for line in ingredients[1:]:
#             row = line.strip().split(sep='\t')
#             output_table[row[0]] = row[1]
#             print(output_table)
#
#
#     entry = input_string.get()
#
#     states1 = []
#     outputs = []
#     states1.append(first_input)
#     outputs.append(output_table[first_input])
#
#     state = first_input
#
#     for g in entry:
#         state = transition_table[state][g]
#         output = output_table[state]
#         print('Girdi:', g, 'State:', state, 'Çıktı:', output)
#         states1.append(state)
#         outputs.append(output)
#
#     output_label.config(text=''.join(outputs))
#     states_label.config(text=''.join(states1))
