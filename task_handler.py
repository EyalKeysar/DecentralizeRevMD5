
RANGE = (0, 99999_99999)
SERVSIZE = 1_000_000
NOT_DONE = 0
IN_PROGRESS = 1
DONE = 2



class TaskHandler():
    def __init__(self):
        self.tasklist = [NOT_DONE for i in range(int((RANGE[1] - RANGE[0])/SERVSIZE))]
        self.clients_to_task = {}
        
    def add_task_client(self, client):
        for i in range(len(self.tasklist)):
            if(self.tasklist[i] == NOT_DONE):
                print(i, " not done")
                self.tasklist[i] = IN_PROGRESS
                if(client not in self.clients_to_task):
                    self.clients_to_task[client] = []
                self.clients_to_task[client].append(i)
                return RANGE[0] + i*SERVSIZE, RANGE[0] + (i+1)*SERVSIZE
            else:
                print(i, " already done")
        
        for i in self.tasklist:
            if(i == IN_PROGRESS):
                if(client not in self.clients_to_task):
                    self.clients_to_task[client] = []
                self.clients_to_task[client].append(i)
                return RANGE[0] + i*SERVSIZE, RANGE[0] + (i+1)*SERVSIZE
    
    def task_checked(self, client, start, end):
        self.tasklist[int((start - RANGE[0])/SERVSIZE)] = DONE
        self.clients_to_task[client].remove(int((start - RANGE[0])/SERVSIZE))
        print(int((start - RANGE[0])/SERVSIZE), " is done")
        return
    
    
        
    
            
if __name__ == '__main__':
    th = TaskHandler()
    print(th.add_task_client('a'))