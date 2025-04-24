from multiprocessing import Process

import time
def squte_number():
      for i in range(5):
            time.sleep(1)
            print(f"Square of {i} is {i * i}")
           
def cube_numbers():
      for i in range(5):
            time.sleep(1.5)
            print(f"Cube : {i*i*i}")
if __name__ == "__main__":
                  process1 = Process(target=squte_number)
                  process2 = Process(target=cube_numbers)
                  t=time.time()

                  process1.start()
                  process2.start()

                  process1.join()
                  process2.join()
                  finished_time=time.time()-t

                  print("Both processes are complete.")