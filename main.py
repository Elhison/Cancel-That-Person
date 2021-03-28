import random
import sorter

random_first_name = random.choice(sorter.first_names_list)
random_last_name = random.choice(sorter.last_names_list)
random_reason = random.choice(sorter.reasons_list)

first_name = random_first_name.replace('\n', ' ')

full_name = first_name + random_last_name

print("Target:", full_name, "\nReason: ", random_reason)
