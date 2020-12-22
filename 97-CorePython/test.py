import multiprocessing

def foo(i):
    print ('called function in process: %s' %i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(foo, (i,))
        Process_jobs.append(p)
        p.start()
        p.join()
