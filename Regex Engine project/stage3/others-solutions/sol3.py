def str_in_str(str_one, str_two):
    possible_lst = [list(str_two)[i:len(str_one) + i] for i, _ in enumerate(str_two)]
    
    final_lst = [''.join(i) for i in possible_lst if len(i) == len(str_one)]
    
    return bool([i for i in final_lst if i == str_one])
        
regex, input_str = input().split('|')

print(True if (regex == input_str or not regex or str_in_str('.', regex) and \
               str_in_str(''.join(regex.split('.')), input_str)) or \
               str_in_str(regex if regex != '.' else '', input_str) else False)