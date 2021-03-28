# Note: make sure the last line isn't empty!

# Note: make sure the last line isn't empty!

# Note: make sure the last line isn't empty!

with open('fake_first_names.txt', 'r+', encoding='utf-8') as first_names_r:
    first_names_list = first_names_r.readlines()
    first_names_list.sort()
    first_names_r.write("\n")

with open('fake_first_names.txt', 'w+', encoding='utf-8') as first_names:
    
    for x in first_names_list:
        first_names.write(x)

with open('fake_last_names.txt', 'r+', encoding='utf-8') as last_names_r:
    last_names_list = last_names_r.readlines()
    last_names_list.sort()
    last_names_r.write("\n")

with open('fake_last_names.txt', 'w+', encoding='utf-8') as last_names:
    
    for x in last_names_list:
        last_names.write(x)

with open('dumb_reasons.txt', 'r+', encoding='utf-8') as reasons_r:
    reasons_list = reasons_r.readlines()
