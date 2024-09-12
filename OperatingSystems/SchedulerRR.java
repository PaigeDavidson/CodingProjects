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
    // p1 is only added back to the ready queue once?
    public Process update(Process cpu){
        // if (cpu != null) {
        //     // preform context switch once time quantum has elapsed or execution has compleated
        //     // cpu.getElapsedBurst() >= timeQuantum || cpu.isExecutionComplete()
        //     if (cpu.getElapsedBurst() >= timeQuantum) {
        //         this.contextSwitches++;
        //         // if the process has completed or the burst time for the process is up, 
        //         if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
        //             // if the process is not finished executing add it back to the ready queue
        //             if (!cpu.isExecutionComplete()) {
        //                 ready.add(cpu);
        //             } else {
        //                 logger.log(String.format("Process %s execution complete", cpu.getName()));
        //             }
        //             cpu = null;
        //             // if the process has not compleated/reached the burst time then preemt the process
        //         } else if (!ready.isEmpty()) {
        //             this.contextSwitches++;
        //             Process preemptedProcess = cpu;
    
        //             ready.add(preemptedProcess); // Add the preempted process back to the ready queue
        //             logger.log(String.format("Time quantum complete for process %s", preemptedProcess.getName()));

        //             this.contextSwitches++;
        //             cpu = ready.poll();
        //             logger.log(String.format("Scheduled: %s", cpu.getName()));
                   
        //         }
        //     }
        // }
        // // Give the new process to the CPU
        // if (cpu == null && !ready.isEmpty()) {
        //     this.contextSwitches++;
        //     cpu = ready.poll();
        //     logger.log(String.format("Scheduled: %s", cpu.getName()));
        // }

        // return cpu;
        if (cpu != null) {
            // Check if the current process has exceeded the time quantum
            if (cpu.getElapsedBurst() >= timeQuantum || cpu.isExecutionComplete()) {
                // this.contextSwitches++;
                // Check if the current process has completed its burst or execution
                if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
                    // If not completed, add it back to the ready queue
                    if (!cpu.isExecutionComplete()) {
                        ready.add(cpu);
                    } else {
                        logger.log(String.format("Process %s execution complete", cpu.getName()));
                    }
                    cpu = null;
                } 
                else if (!ready.isEmpty()){
                    // Preempt the current process
                    Process preemptedProcess = cpu;
                    ready.add(preemptedProcess); // Add the preempted process back to the ready queue
                    logger.log(String.format("Time quantum complete for process %s", preemptedProcess.getName()));
                    cpu = null;
                }
            }
        }
        
        // Assign the CPU to the next process in the ready queue
        if (cpu == null && !ready.isEmpty()) {
            this.contextSwitches++;
            cpu = ready.poll();
            // cpu.update(); // Update the elapsed burst for the new process
            logger.log(String.format("Scheduled: %s", cpu.getName()));
        }
    
        return cpu;
        // if (cpu != null) {
        //     // Check if the current process has exceeded the time quantum
        //     if (cpu.getElapsedBurst() >= timeQuantum || cpu.isExecutionComplete()) {
        //         // If the process has completed its burst or execution, add it back to the ready queue
        //         if (!cpu.isExecutionComplete()) {
        //             ready.add(cpu);
        //         } else {
        //             logger.log(String.format("Process %s execution complete", cpu.getName()));
        //         }

        //         cpu = null;

        //     }
        // }
        // // Assign the CPU to the next process in the ready queue
        // if (cpu == null && !ready.isEmpty()) {
        //     this.contextSwitches++;
        //     cpu = ready.poll();
        //     logger.log(String.format("Scheduled: %s", cpu.getName()));
        // }

        // return cpu;
    }
}


