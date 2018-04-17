'''
CS5250 Assignment 4, Scheduling policies simulator
Sample skeleton program
Author: Minh Ho
Input file:
    input.txt
Output files:
    FCFS.txt
    RR.txt
    SRTF.txt
    SJF.txt

Apr 10th Revision 1:
    Update FCFS implementation, fixed the bug when there are idle time slices between processes
    Thanks Huang Lung-Chen for pointing out
Revision 2:
    Change requirement for future_prediction SRTF => future_prediction shortest job first(SJF), the simpler non-preemptive version.
    Let initial guess = 5 time units.
    Thanks Lee Wei Ping for trying and pointing out the difficulty & ambiguity with future_prediction SRTF.
'''
import sys
from Queue import Queue

input_file = 'input.txt'

DEBUG = True

class Process:
    last_scheduled_time = 0
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
    #for printing purpose
    def __repr__(self):
        return ('[id %d : arrive_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))

def FCFS_scheduling(process_list):
    #store the (switching time, proccess_id) pair
    schedule = []
    current_time = 0
    waiting_time = 0
    for process in process_list:
        if(current_time < process.arrive_time):
            current_time = process.arrive_time
        schedule.append((current_time,process.id))
        waiting_time = waiting_time + (current_time - process.arrive_time)
        current_time = current_time + process.burst_time
    average_waiting_time = waiting_time/float(len(process_list))
    return schedule, average_waiting_time

#Input: process_list, time_quantum (Positive Integer)
#Output_1 : Schedule list contains pairs of (time_stamp, proccess_id) indicating the time switching to that proccess_id
#Output_2 : Average Waiting Time
def RR_scheduling(process_list, time_quantum ):
    '''
    RR Scheduling:
        - When a process arrives, it's enqueued into a ready queue
        - If no process currently executing, start executing head of queue
        - Three scenarios
            - Process ends before time quantum Q expires
            - Time quantum Q expires:
                - Process is done : nothing to do
                - Process not done: needs to go back into ready queue
    '''
    if not process_list:
        return (["no processes given"], 0.0)

    schedule = []
    current_time = 0
    waiting_time = 0
    ready_queue = []

    def add_arrived_processes_to_ready_queue(old_ready_queue, process_list):
        arrived_processes = filter(lambda p: p.arrive_time <= current_time, process_list)
        remaining_processes = filter(lambda p: p.arrive_time > current_time, process_list)
        # Our new ready queue includes the processes that just arrived - and we return the remaining processes
        old_ready_queue.extend(arrived_processes)
        return remaining_processes

    # Add arrived processes before we start (should just be the first process)
    process_list = add_arrived_processes_to_ready_queue(ready_queue, process_list)


    # Run this algorithm as long as the ready queue has processes inside
    while ready_queue:

        # Take a process out of the current waiting process queue and note the context switch
        running_process = ready_queue.pop(0)
        schedule.append((current_time, running_process.id))

        if running_process.burst_time <= time_quantum:
            # If the process runs within the time quantum, it is done and we just take as much time as the burst time of that process
            current_time += running_process.burst_time
            running_process.burst_time = 0
            process_list = add_arrived_processes_to_ready_queue(ready_queue, process_list)
        else:
            # The process exceeds TQ - need to pre-empt and put to back of queue
            running_process.burst_time -= time_quantum
            current_time += time_quantum
            # before we add the running process back to the list, add any new processes
            process_list = add_arrived_processes_to_ready_queue(ready_queue, process_list)
            ready_queue.append(running_process)
        
    
    return (schedule, 0.0)

def SRTF_scheduling(process_list):
    return (["to be completed, scheduling process_list on SRTF, using process.burst_time to calculate the remaining time of the current process "], 0.0)

def SJF_scheduling(process_list, alpha):
    return (["to be completed, scheduling SJF without using information from process.burst_time"],0.0)


def read_input():
    result = []
    with open(input_file) as f:
        for line in f:
            array = line.split()
            if (len(array)!= 3):
                print ("wrong input format")
                exit()
            result.append(Process(int(array[0]),int(array[1]),int(array[2])))
    return result
def write_output(file_name, schedule, avg_waiting_time):
    with open(file_name,'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f \n'%(avg_waiting_time))


def main(argv):
    process_list = read_input()
    print ("printing input ----")
    for process in process_list:
        print (process)
    print ("simulating FCFS ----")
    FCFS_schedule, FCFS_avg_waiting_time =  FCFS_scheduling(process_list)
    write_output('FCFS.txt', FCFS_schedule, FCFS_avg_waiting_time )
    print ("simulating RR ----")
    RR_schedule, RR_avg_waiting_time =  RR_scheduling(process_list,time_quantum = 4) #default TQ = 2
    write_output('RR.txt', RR_schedule, RR_avg_waiting_time )
    print ("simulating SRTF ----")
    SRTF_schedule, SRTF_avg_waiting_time =  SRTF_scheduling(process_list)
    write_output('SRTF.txt', SRTF_schedule, SRTF_avg_waiting_time )
    print ("simulating SJF ----")
    SJF_schedule, SJF_avg_waiting_time =  SJF_scheduling(process_list, alpha = 0.5)
    write_output('SJF.txt', SJF_schedule, SJF_avg_waiting_time )

if __name__ == '__main__':
    main(sys.argv[1:])
