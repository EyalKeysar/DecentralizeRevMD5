from server_const import *
from enum import Enum



class Task():
    def __init__(self, md5Hashed):
        self.md5Hashed = md5Hashed
        serving_array = [NOT_SERVED for i in range(int((RANGE_END - RANGE_START) / SERVING_SIZE))]
        print(len(serving_array))
        print(serving_array[0:90])

        # handle the last element
        if(len(serving_array) * SERVING_SIZE < RANGE_END - RANGE_START):
            serving_array.append(NOT_SERVED)

    def getMd5Hashed(self):
        return self.md5Hashed
    

    

if __name__ == '__main__':
    task = Task("123")
    