
'''
    snake_case_to_camel_case()
     convert input string of snake case to camel case

    input
       str_snake_case

    output
        strCamelCase

'''
def snake_case_to_camel_case(str_snake_case):

    list_camel = []
    s = str_snake_case 
    list_snake = s.split("_")
    size = len(list_snake)
    for i, sub_str in enumerate( list_snake ):
        if len(sub_str) != 1:
            sub_str_lower = sub_str.lower()
            if i != 0: ## capitalize non-first string
                sub_str_Cap = sub_str_lower.capitalize()
                list_camel.append(sub_str_Cap)        
            else: ## first string, lower case
                list_camel.append(sub_str_lower)        
        else: ## no change for single letter string
            if i == 0: ## first string
                single_char = sub_str + "_"
            elif i == size-1: ## last string
                single_char = "_"+sub_str
            else:
                single_char = "_"+sub_str+"_"

            list_camel.append(single_char)        
            
    strCamelCase = "".join(list_camel)
    strCamelCase = strCamelCase.replace("__", "_", 10)

    return strCamelCase


## test 


snake = "this_is_a_word"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")


snake = "this_is_a_WORD"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "This_is_0_word"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "This_is_a_WORD"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "This_is_A_0WORD"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "avSTACK_design_voltage_W"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "avSTACK_design_voltage_W0"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "avSTACK_design_voltage_X_y_Z"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

snake = "X_abc_def_Z"
print(f"snake = {snake}; camel = {snake_case_to_camel_case(snake)}")

print("wait")