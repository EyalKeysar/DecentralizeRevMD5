
RANGE = (0, 99999_99999)
SERVSIZE = 1_000_000
NOT_DONE = 0
IN_PROGRESS = 1
DONE = 2

class TaskHandler():
    def __init__(self):
        self.tasklist = [NOT_DONE for i in range((RANGE[1] - RANGE[0])/SERVSIZE)]
        
    def add_client(self, client):
        for i in self.tasklist:
            if(i == NOT_DONE):
                i = IN_PROGRESS
                return self.tasklist.index(i) * SERVSIZE
        
    
    def task_checked(self, client):
    
    
            
            