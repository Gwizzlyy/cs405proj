'''
Authors: Homer Al-Nowaif, Shahd Abdou, Sheikha Al-Qurtas
CSIS 405 Project: String Elimination 
Solution 1
Time Complexity: O(2^n)
'''
def brute_force(in_str):
    if not in_str:
        return True
    i = 0
    while i < len(in_str):
        j = i
        # Find the end of the consecutive block
        while j + 1 < len(in_str) and in_str[j + 1] == in_str[i]:
            j += 1 # increase index when a match is found
        if j > i:  # End of block
            new_str = in_str[:i] + in_str[j + 1:]  # Remove the block
            if brute_force(new_str):  # Call bruteforce on the new sliced string
                return 1 # reducable
        i = j + 1  # Move to the next character
    return 0  # No blocks were removed

def main():
    with open("Project\input.txt", "r") as file: # Please paste your relative path/path in the quotes :) ensure its // for normal paths
        lines = file.readlines()
    
    t = int(lines[0].strip())
    results = []
    for i in range(1, t + 1):
        in_str = lines[i].strip()
        results.append(brute_force(in_str))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
