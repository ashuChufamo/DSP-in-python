from threading import Thread, Lock

total_counter= 0
def count_word(filepath, search_word, l: Lock):
    with open(filepath) as f:
        for line in f.readlines():
            for word in line.split():
                if word == search_word:
                    counter += 1
    l.acquire()
    total_counter+= counter
    l.release()


if __name__ =="__main__":
    search_word = input('Enter a search word: ').split()[0].lower()
    file_paths= [
        '../text_assets/a.txt'
    ]
    threds= []
    lock = Lock()
    for file_path in file_paths:
        thread= Thread(target=count_word, args= [file_path, search_word,lock])
        thread.start()
        threds.append(thread)
        
    for thread in threads:
        thread.join()
        
    print('Total occurences: ', total_counter)