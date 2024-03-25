import hashlib
import argparse
import os
from hashing import hash_string, hash_file, plot_hashing_speeds

def main():
    parser = argparse.ArgumentParser(description='Hashing data and benchmarking hashing speeds')
    parser.add_argument('data', type=str, help='Data to hash')
    parser.add_argument('--file', type=str, help='Path to file for hashing')
    args = parser.parse_args()

    input_data = args.data
    file_path = os.path.join(os.path.dirname(__file__), "ubuntu.iso")


    # Step 1: Hashing input data from console
    for algo in hashlib.algorithms_available:
        if algo.startswith('shake_'):
            continue
        hashed_value, time_taken = hash_string(algo, input_data)
        print(f"{algo}: {hashed_value} (Time taken: {time_taken:.6f} seconds)")

    # Step 2: Hashing a large file and checking the correctness of hashing for sha256 hash
    if file_path:
        sha256_hash = '3b6c5275366d02160554fa5703add462da3b8ce9be1749f8806e8dbbffaa2b5a'
        hashed_value, _ = hash_file('sha256', file_path)
        print(f"SHA256: {hashed_value}")
        if hashed_value == sha256_hash:
            print("Hash matches for SHA256")

    # Step 3: Hashing a binary file from disk
    if file_path:
        for algo in hashlib.algorithms_available:
            if algo.startswith('shake_'):
                continue
            hashed_value, _ = hash_file(algo, file_path)
            print(f"{algo}: {hashed_value}")

    # Step 4: Benchmarking hashing speeds for different message sizes
    if not file_path:
        message_sizes = [10**i for i in range(1, 7)]
        algorithms_to_test = ['md5', 'sha1', 'sha256', 'sha512']
        plot_hashing_speeds(message_sizes, algorithms_to_test)

if __name__ == "__main__":
    main()
