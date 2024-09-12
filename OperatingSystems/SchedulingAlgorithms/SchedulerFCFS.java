import java.util.LinkedList;
import java.util.Queue;

public class SchedulerFCFS extends SchedulerBase implements Scheduler{ 

    private Queue<Process> ready = new LinkedList<>(); // simple FIFO queue for this scheduling algorithm
    private Logger logger;

    public SchedulerFCFS(Logger logger){
        this.logger = logger;
    }
    
    public void notifyNewProcess(Process p){
        // Used to notify the scheduler a new process has just entered the ready state.
        this.ready.add(p);

    }
    public Process update(Process cpu){
        // Update the scheduling algorithm for a single CPU.
        // @return Reference to the process that is executing on the CPU; 
        // result might be null if no process available for scheduling.
        if (cpu != null) {
            // Check to see if this process has completed its burst time, if so, return it to the ready state
            if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
                this.contextSwitches++;
                this.logger.log(String.format("Process %s burst complete", cpu.getName()));
                // Only return to the ready state if there is remaining execution time
                if (!cpu.isExecutionComplete()) {
                    ready.add(cpu);
                }
                else {
                    this.logger.log(String.format("Process %s execution complete", cpu.getName()));
                }
                cpu = null;
            }
        }
        // gives the new process to the cpu
        if (cpu == null && ready.peek() != null) {
            this.contextSwitches++;
            Process p = ready.remove();
            cpu = p;
            this.logger.log(String.format("Scheduled: %s", cpu.getName()));
        }
        // If no process available or CPU is already executing a process, return current process
        return cpu;
    }
    
}
