# The main goal of this function is to print the phone number menmonic
# for example if input = [2,3] 2 =abc 3 = def the combinations would ad ae af bd be bf cd ce cf
# the function takes digits as input 

def phone_number_mnemonics(digits):
    if len(digits) == 0:
        return []
    map_char = {
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"
    }
    result = []
    solve_combinations(digits,map_char,result)
    print(result)

def solve_combinations(digits,map_char,result,cur_str="",cur_lvl = 0):
    if cur_lvl == len(digits):
        result.append(cur_str)
        return

    for c in map_char[int(digits[cur_lvl])]:
        solve_combinations(digits,map_char,result,cur_str+c,cur_lvl+1)

phone_number_mnemonics("23")
    