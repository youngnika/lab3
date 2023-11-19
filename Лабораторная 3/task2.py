# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    group1_list = group1.split(delimiter)
    group2_list = group2.split(delimiter)

    set_group1 = set(group1_list)
    set_group2 = set(group2_list)

    common_participants = set_group1.intersection(set_group2)
    common_participants_list = sorted(list(common_participants))

    return common_participants_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group, delimiter="|"))
