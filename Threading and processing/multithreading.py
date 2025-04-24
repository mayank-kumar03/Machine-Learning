import threading
import time
def print_num():
      for i in range(5):
            time.sleep(2)
            print(f"Number:{i}")
def print_letter():
      for letter in "abcde":
            time.sleep(2)
            print(f"Letter: {letter}")
t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)

t=time.time()
# print_num()
# print_letter()
t1.start()
t2.start()
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)
