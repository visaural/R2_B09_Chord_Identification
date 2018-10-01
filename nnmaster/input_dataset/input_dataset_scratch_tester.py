import linecache
import random

TEST_FILE = "chord_master_list.txt"

def get_line_index_from_file(f, i):
    return linecache.getline(f, i)

def random_ints_in_range(num_samples, LB, UB):
    if num_samples == 0:
        return None
    elif num_samples == 1:
        return random.randint(LB, UB)
    else:
        l = [i for i in range(LB, UB + 1)]
        k = random.sample(l, num_samples)

    return k

if __name__ == "__main__":
    #print(linecache.getline(TEST_FILE, 3))
    #print(get_line_index_from_file(TEST_FILE, 2))

    #print(random_ints_in_range(30, 1, 444))
    print(get_line_index_from_file("input_dataset.txt", 5))