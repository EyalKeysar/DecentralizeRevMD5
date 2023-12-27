from ServerAPI.ServerAPI import ServerAPI
from hashlib import md5
from multiprocessing import Process, Queue

class Client():
    def __init__(self):
        self.main()
    def main(self):
        num_of_cores = 4
        running_processes = []

        self.found_index = -1
        self.not_found_buff = []
        
        self.server_api = ServerAPI()
        
        self.server_api.connect()
        
        while True:
            if(len(running_processes) >= num_of_cores):
                for p in running_processes:
                    p.join()
                    running_processes.remove(p)
                if(self.found_index != -1):
                    self.server_api.found(self.found_index)
                    break
                for i in self.not_found_buff:
                    self.server_api.not_found(i[0], i[1])
                    self.not_found_buff.remove(i)
            else:
                print("num of running processes: ", len(running_processes))

                task = self.server_api.get_task()
                print("Got new task: ", task)
                if task is False:
                    print("Task False")
                    break
                
                self.do_task_subproc(task, running_processes)
        
        self.server_api.disconnect()
        print("Done")
        
        
    def do_task_subproc(self, task, running_processes):
        '''
            create a subprocess and execute the do_task function
        '''
        print("Starting new process")
        p = Process(target=self.do_task, args=(task,))
        running_processes.append(p)
        p.start()
        return
        
    def do_task(self, task):
        for i in range(int(task[0]), int(task[1])):
            if(md5(str(str(i).zfill(10)).encode()).hexdigest() == task[2]):
                self.server_api.found(i)
                return
        self.not_found_buff.append((int(task[0]), int(task[1])))
        return
    


if __name__ == "__main__":
    c = Client()
