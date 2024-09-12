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
        // if (cpu != null) {
        //     // Check if the current process has exceeded the time quantum
        //     if (cpu.getElapsedBurst() >= timeQuantum || cpu.isExecutionComplete()) {
        //         // this.contextSwitches++;
        //         // Check if the current process has completed its burst or execution
        //         if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
        //             // If not completed, add it back to the ready queue
        //             if (!cpu.isExecutionComplete()) {
        //                 ready.add(cpu);
        //             } else {
        //                 logger.log(String.format("Process %s execution complete", cpu.getName()));
        //             }
        //             cpu = null;
        //         } 
        //         else if (!ready.isEmpty()){
        //             // Preempt the current process
        //             Process preemptedProcess = cpu;
        //             ready.add(preemptedProcess); // Add the preempted process back to the ready queue
        //             logger.log(String.format("Time quantum complete for process %s", preemptedProcess.getName()));
        //             cpu = null;
        //         }
        //     }
        // }
        
        // // Assign the CPU to the next process in the ready queue
        // if (cpu == null && !ready.isEmpty()) {
        //     this.contextSwitches++;
        //     cpu = ready.poll();
        //     // cpu.update(); // Update the elapsed burst for the new process
        //     logger.log(String.format("Scheduled: %s", cpu.getName()));
        // }
    
        // return cpu;
        if (cpu != null && !cpu.isExecutionComplete()) {
            //AMMON'S NOTES (PLEASE REMOVE AFTER)
            //Changed this if statement becuase they way they have to reset the get elasped
            //burst is broken so it's easier to compare the time quantum and burst using the modulo
            //END NOTE
            if (cpu.getElapsedBurst() % timeQuantum == 0) {
                // Preempt the current process because the time quantum has elapsed
                //AMMON'S NOTES (PLEASE REMOVE AFTER)
                //removed the cpu update from here because I don't think it was doing anything
                //END NOTE
                this.contextSwitches++;
                logger.log(String.format("Time quantum complete for process %s", cpu.getName()));
                ready.add(cpu); // Add the preempted process back to the ready queue
                cpu = null; // Remove the process from the CPU to allow the next process to be scheduled
            }
        }

        //AMMON'S NOTES
        //This was origionally at the end of this function but because that caused the function to return null
        //it was ending the simulation ealry by swapping this if statment and the one that scedules a process
        //if the cpu is idle it ensures that this function never returns a null value!
        //END NOTES
        // If the process has finished, log it and remove it from the CPU
        if (cpu != null && cpu.isExecutionComplete()) {
            logger.log(String.format("Process %s execution complete", cpu.getName()));
            //AMMON'S NOTES
            //adding one to the context switches because that increases every time you take a value off from being
            //executed.
            //END NOTES
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


