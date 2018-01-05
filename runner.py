import sys, hist, time, multiprocessing

def CreateOhmu(line):
    
    # Create Ohmu object
    O = hist.Ohmu()

    # Gets time to start
    now = time.time()
    now = int(now)

    frq = "histoday"
    lastTime = O.download(line)

    print(lastTime)
    print("%s Complete!" % line)

def process(line):
    CreateOhmu(line)
    return

def process_wrapper(lineByte):
    with open("coinList") as f:
        f.seek(lineByte)
        line = f.readline()
        process(line)
        return

def main():
    # 0. init objects
    t0=time.time()
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(cores)
    jobs = []

    # 2. Open address file
    #create jobs
    with open("coinList") as f:
        nextLineByte = f.tell()
        for line in f:
            jobs.append( pool.apply_async(process(line)))
            nextLineByte = f.tell()

    # 3. wait for all jobs to finish
    for job in jobs:
        job.get()

    #clean up
    pool.close()
    t1=time.time()
    print("Time Elapsed: %s" % str(t1-t0))

    return

if __name__ == "__main__":
    main()