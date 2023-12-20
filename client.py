from ServerAPI.ServerAPI import ServerAPI
from hashlib import md5
from multiprocessing import Process, Queue


def main():
    num_of_cores = 4
    running_processes = []
    
    server_api = ServerAPI()
    
    server_api.connect()
    
    while True:
        task = server_api.get_task()
        print("Got new task: ", task)
        if task is False:
            break
        if(len(running_processes) >= num_of_cores):
            for p in running_processes:
                p.join()
        do_task_subproc(task, server_api, running_processes)
    
    server_api.disconnect()
    print("Done")
    
    
def do_task_subproc(task, server_api, running_processes):
    '''
        create a subprocess and execute the do_task function
    '''
    p = Process(target=do_task, args=(task, server_api))
    running_processes.append(p)
    p.start()
    return
    
def do_task(task, server_api):
    for i in range(task[0], task[1]):
        if(md5(str(i.zfill(10)).encode()).hexdigest() == task[2]):
            server_api.found(i)
            return
    server_api.not_found()
    

# Q: how to hash with md5?
# A: hashlib.md5(str(rand).encode()).hexdigest()


if __name__ == "__main__":
    main()