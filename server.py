import hashlib
import time
import random
from server_const import *

def main():
    start_time = time.time()

    # for i in range(SERVING_SIZE):
    #     rand = str(i).zfill(10)
    #     hashlib.md5(str(rand).encode()).hexdigest()

    print("--- %s seconds ---" % (time.time() - start_time))



if __name__ == '__main__':
    main()