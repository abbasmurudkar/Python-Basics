import threading

class thread(threading.Thread):
    def _init_(self, thread_name , thread_id):
        threading.Thread._init_(self)
        self.thread_name = thread.name
        self.thread_id = thread.id

    def run(self):
        print(str(self.thread_name) +" "+str(self.thread_id));

thread1 = thread("GFG",1000)
thread2 = thread("GREEKSFORGEEKS",2000)

thread1.start()
thread2.start()

print("EXIT")
