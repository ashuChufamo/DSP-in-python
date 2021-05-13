from threading import Thread, Lock
from queue import Queue

total_counter= 0

total_queue = Queue()


def count_word(filepath, search_word, l: Lock):
    counter = 0
    with open(filepath) as f:
        for line in f.readlines():
            for word in line.split():
                if word.lower() == search_word:
                    counter += 1
    l.acquire()
    global total_counter
    # total_counter+= counter
    l.release()
    
    global total_queue
    total_queue.put(counter)


if __name__ =="__main__":
    search_word = input('Enter a search word: ').split()[0].lower()
    file_paths= [
        '/home/ashu/Desktop/lab-1-2/lab/text_assets/a.txt',
        '/home/ashu/Desktop/lab-1-2/lab/text_assets/b.txt',
        '/home/ashu/Desktop/lab-1-2/lab/text_assets/c.txt',
    ]
    threds= []
    lock = Lock()
    for file_path in file_paths:
        thread= Thread(target=count_word, args= [file_path, search_word,lock])
        thread.start()
        threds.append(thread)
        
    for thread in threds:
        thread.join()
    total_queue.put("QUIT")
        
    # print('Total occurences: ', total_counter)
    
def get_count(q: Queue):
    while True:
        next_item = q.get()
        if (next_item == 'QUIT'):
            break
        global total_counter
        total_counter +=  next_item
        
thread = Thread(target=get_count, args=[total_queue])
thread.start()
thread.join()
print("Total count ,", total_counter)