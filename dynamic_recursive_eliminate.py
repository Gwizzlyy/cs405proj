'''
Authors: Homer Al-Nowaif, Shahd Abdou, Sheikha Al-Qurtas
CSIS 405 Project: String Elimination 
Solution 2
Time Complexity: O(n^3)
'''
memory = {}

def can_empty(in_str):
    # Memorization to reduce the need for recursion.
    if not in_str:
        return True
    if in_str in memory:
        return memory[in_str]
    # Core Logic start
    i = 0
    can = False
    while i < len(in_str) and not can:
        j = i
        # Check for consecutive a's or b's
        while j + 1 < len(in_str) and in_str[j + 1] == in_str[i]:
            j += 1
        if j != i: # A block is spotted
            can = can_empty(in_str[:i] + in_str[j + 1:]) # concatenate and call the function on new string
        i = j + 1
    
    memory[in_str] = can # backtracking to stop recalculation of a seen combination.
    
    return can

def main():
    # Pasta your path/relative path
    with open('Project/input.txt', 'r') as file:
        lines = file.readlines()
    
    t = int(lines[0].strip())  # number of test cases
    test_cases = [line.strip() for line in lines[1:t+1]]  # Next `t` lines are the strings.

    for in_str in test_cases:
        memory.clear()
        if can_empty(in_str):
            print("1")
        else:
            print("0")

if __name__ == "__main__":
    main()