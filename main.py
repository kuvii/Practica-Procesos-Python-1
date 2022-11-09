import os
from time import sleep

def padre():
        print("Pid padre: ", os.getpid())
        for i in range(processRepeat):
            sonPid = os.fork()
            if sonPid == 0:
                hijo()
          
    
def hijo():
    print("  > Son pid: ", os.getpid())
    sleep(5)
    print("Process ", os.getpid(), " ended")
    os._exit(0)
    
if __name__ == '__main__' :
    processRepeat = int(input("Cuantos procesos quieres abrir: "))
    padre()