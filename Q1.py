# Benchmarking it
import random
import time
import os
from main import main
import matplotlib.pyplot as plt

str_dict = {"a": 2, "b": 4, "c": 5, "d": 1, "e": 3}
string_lengths = [25, 50, 100, 200, 400, 600, 800, 1000, 1500, 2000]

def generate_inputs(str_dict, str_len):
    chars = list(str_dict.keys())
    result = str(len(chars)) + "\n"
    for c in chars:
        result += c + " " + str(str_dict[c]) + "\n"
    A = ""
    for i in range(str_len):
        A += random.choice(chars)
    B = ""
    for i in range(str_len):
        B += random.choice(chars)
    result += A + "\n" + B
    return result

def run_benchmark():
    times = []
    for id in range(len(string_lengths)):
        str_len = string_lengths[id]
        input_str = generate_inputs(str_dict, str_len)
        f = open("inputs/input_" + str(id) + ".txt", "w")
        f.write(input_str)
        f.close()
        start = time.time()
        max_value, subsequence = main(input_str)
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        f = open("outputs/output_" + str(id) + ".txt", "w")
        f.write(str(max_value) + "\n")
        f.write(subsequence + "\n")
        f.close()
        print("length " + str(str_len) + " --> " + str(elapsed) + " seconds")
    plt.figure()
    plt.plot(string_lengths, times)
    plt.xlabel("String len")
    plt.ylabel("Runtime in seconds")
    plt.savefig("outputs/runtime_over_str_len.png")
    plt.show()

os.makedirs("inputs", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
run_benchmark()