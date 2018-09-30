import linecache
import random

TEST_FILE = "chord_master_list.txt"

def get_line_index_from_file(f, i):
    return linecache.getline(f, i + 1)

def random_int(n, LB, UB):
    if n == 0:
        return None
    elif n == 1:
        return random.randint(LB, UB)
    else:
        l = [i for i in range(n)]
        k = random.sample(l)
        return k

if __name__ == "__main__":
    #print(linecache.getline(TEST_FILE, 3))
    #print(get_line_index_from_file(TEST_FILE, 2))

    random_int(30, 1, 49)