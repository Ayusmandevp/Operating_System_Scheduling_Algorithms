def sjf(procs):
    time,finished=0,[]

    while procs:
        available=[p for p in procs if p['arrival']<=time]

        if not available:
            time=min(p['arrival'] for p in procs)
            continue
        p=min(available,key= lambda x:x['burst'])
        procs.remove(p)

        time+=p['burst']
        p['completion']=time
        p['turnaound']=p['completion']-p['arrival']
        p['waiting']=p['turnaound']-p['burst']

        finished.append(p)

    return finished

procs = [{'id': 1, 'arrival': 0, 'burst': 5}, {'id': 2, 'arrival': 2, 'burst': 3}]
print("FCFS:", sjf(procs))
