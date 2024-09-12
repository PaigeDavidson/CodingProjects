import java.util.LinkedList;
import java.util.Queue;

public class SchedulerRR extends SchedulerBase implements Scheduler{

    private Queue<Process> ready = new LinkedList<>();
    private int timeQuantum;
    private Logger logger;
    
    public SchedulerRR(Logger logger, int timeQuantum){
        this.logger = logger;
        this.timeQuantum = timeQuantum;
    }
    public void notifyNewProcess(Process p){
        ready.add(p);
    }

    public Process update(Process cpu){
        if (cpu != null && !cpu.isExecutionComplete()) {
            if (cpu.getElapsedBurst() % timeQuantum == 0) {
                // Preempt the current process because the time quantum has elapsed
                this.contextSwitches++;
                logger.log(String.format("Time quantum complete for process %s", cpu.getName()));
                ready.add(cpu); // Add the preempted process back to the ready queue
                cpu = null; // Remove the process from the CPU to allow the next process to be scheduled
            }
        }
    
        // If the process has finished, log it and remove it from the CPU
        if (cpu != null && cpu.isExecutionComplete()) {
            logger.log(String.format("Process %s execution complete", cpu.getName()));
            this.contextSwitches++;
            cpu = null;
        }

        // Schedule a new process if the CPU is idle
        if (cpu == null && !ready.isEmpty()) {
            this.contextSwitches++;
            cpu = ready.poll(); // Get the next process from the ready queue
            logger.log(String.format("Scheduled: %s", cpu.getName()));
        }
    
        return cpu; // Return the process that should be on the CPU
    }
}


