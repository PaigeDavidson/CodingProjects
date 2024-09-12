import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Comparator;

public class SchedulerSRTF extends SchedulerBase implements Scheduler{

    private Queue<Process> ready = new LinkedList<>(); // simple FIFO queue for this scheduling algorithm
    private Logger logger;

    public SchedulerSRTF(Logger logger){
        this.logger = logger; 
    }
    public void notifyNewProcess(Process p){
        this.ready.add(p);
    }
    public Process update(Process cpu){
        // Shortest Remaining Time First
        if (cpu != null) {
            if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
                this.contextSwitches++;
                logger.log(String.format("Process %s burst complete", cpu.getName()));
                if (!cpu.isExecutionComplete()) {
                    ready.add(cpu);
                } else {
                    logger.log(String.format("Process %s execution complete", cpu.getName()));
                }
                cpu = null;
            } else if (!ready.isEmpty() && ready.peek().getTotalTime() < cpu.getTotalTime()) {
                this.contextSwitches++;
                Process preemptedProcess = cpu;

                ready.add(preemptedProcess); // Add the preempted process back to the ready queue
                logger.log(String.format("Preemptively removed: %s", preemptedProcess.getName()));

                cpu = ready.poll(); // Get the next process from the ready queue and give it to the cpu
                logger.log(String.format("Scheduled: %s", cpu.getName()));
                this.contextSwitches++;
            }
        }

        // Sort the ready queue based on total time
        PriorityQueue<Process> updatedReadyQueue = new PriorityQueue<>(Comparator.comparingInt(Process::getTotalTime));
        updatedReadyQueue.addAll(ready);
        ready = updatedReadyQueue;

        // Give the new process to the CPU
        if (cpu == null && !ready.isEmpty()) {
            this.contextSwitches++;
            cpu = ready.poll();
            logger.log(String.format("Scheduled: %s", cpu.getName()));
        }

        return cpu;
    }
}
