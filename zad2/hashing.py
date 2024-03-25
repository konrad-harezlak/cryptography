import hashlib
import timeit
import matplotlib.pyplot as plt

def hash_string(algorithm, data):
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Algorithm '{algorithm}' is not available in hashlib.")
    hasher = hashlib.new(algorithm)
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest(), timeit.default_timer()

def hash_file(algorithm, file_path):
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Algorithm '{algorithm}' is not available in hashlib.")
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest(), timeit.default_timer()

def plot_hashing_speeds(message_sizes, algorithms):
    time_results = {algo: [] for algo in algorithms}
    for size in message_sizes:
        data = 'a' * size
        for algo in algorithms:
            _, time_taken = hash_string(algo, data)
            time_results[algo].append(time_taken)

    for algo, times in time_results.items():
        plt.plot(message_sizes, times, label=algo)

    plt.xlabel('Message Size')
    plt.ylabel('Time (s)')
    plt.title('Hashing Speeds for Different Message Sizes')
    plt.legend()
    plt.show()