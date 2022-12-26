def swap_case(s):
    letters = list(s)
    converted_list = []
    
    for x in letters:
        if(x.islower()):
            converted_list.append(x.upper())
        else:
            converted_list.append(x.lower())
  
    return ("".join(converted_list))
