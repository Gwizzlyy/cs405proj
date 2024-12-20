import time
import random
def can_empty_brute_force(in_str):
    if not in_str:
        return True
    for i in range(len(in_str)):
        for j in range(i + 1, len(in_str)):
            if in_str[i] == in_str[j]:
                new_str = in_str[:i] + in_str[i+1:j] + in_str[j+1:]
                start_time = time.perf_counter()  # Use perf_counter for higher precision
                if can_empty_brute_force(new_str):
                    print(f"Time for {new_str}: {time.perf_counter() - start_time:.6f} seconds")
                    return True
    return False

def generate_test_case(length):
    return ''.join(random.choices('ab', k=length))  # Only 'a' and 'b' characters

def test_algorithm():
    input_sizes = [5, 10, 15, 20, 25, 30]
    results = []

    for size in input_sizes:
        test_string = generate_test_case(size)
        
        # Measure the start time using perf_counter for better precision
        start_time = time.perf_counter()
        
        can_empty_brute_force(test_string)
        
        # Measure the end time
        end_time = time.perf_counter()
        
        # Calculate time taken
        execution_time = end_time - start_time
        
        results.append((size, execution_time))
        print(f"Input size: {size}, Time: {execution_time:.6f} seconds")
    
    return results

results = test_algorithm()

try:
    import matplotlib.pyplot as plt
    sizes, times = zip(*results)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Empirical Testing of Brute Force Algorithm with 'a' and 'b' Strings")
    plt.show()
except ImportError:
    print("matplotlib is not installed. Skipping the plot.")
