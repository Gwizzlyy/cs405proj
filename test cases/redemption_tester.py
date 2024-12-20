import random
import time

valid = {}

def can_empty(in_str):
    if not in_str:
        return True
    if in_str in valid:
        return valid[in_str]
    
    # Core Logic to reduce string
    i = 0
    can = False
    while i < len(in_str) and not can:
        j = i
        while j + 1 < len(in_str) and in_str[j + 1] == in_str[i]:
            j += 1
        if j != i:
            can = can_empty(in_str[:i] + in_str[j + 1:])
        i = j + 1
    
    valid[in_str] = can
    return can

def generate_test_case(length):
    """Generate a test case with only 'a' and 'b' characters."""
    return ''.join(random.choices('ab', k=length))

def empirical_testing():
    # List of input sizes to test on
    input_sizes = [5, 10, 15, 20, 30,40,50,60,70,80,90,100]
    results = []

    for size in input_sizes:
        # Generate a random string of the given size
        test_string = generate_test_case(size)
        
        # Start measuring execution time
        start_time = time.perf_counter()
        
        # Call the can_empty function
        can_empty(test_string)
        
        # End time measurement
        end_time = time.perf_counter()
        
        # Calculate the time taken
        execution_time = end_time - start_time
        
        # Store the result
        results.append((size, execution_time))
        print(f"Input size: {size}, Time: {execution_time:.6f} seconds")
    
    return results



results = empirical_testing()
try:
    import matplotlib.pyplot as plt
    sizes, times = zip(*results)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Empirical Testing of Recursive Backtracking/DP with 'a' and 'b' Strings")
    plt.show()
except ImportError:
    print("matplotlib is not installed. Skipping the plot.")