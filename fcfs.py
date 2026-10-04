def fcfs(proc):
    proc.sort(key=lambda x:x['arrival'])
    current_time=0
    for p in proc:
        if current_time<p['arrival']:
            current_time=p['arrival']
        p['completion']=current_time + p['burst']
        p['turnaround'] = p['completion'] - p['arrival']
        p['waiting'] = p['turnaround'] - p['burst']
        current_time = p['completion']
    return proc





procs = [{'id': 1, 'arrival': 0, 'burst': 5}, {'id': 2, 'arrival': 2, 'burst': 3}]
print("FCFS:", fcfs(procs))
