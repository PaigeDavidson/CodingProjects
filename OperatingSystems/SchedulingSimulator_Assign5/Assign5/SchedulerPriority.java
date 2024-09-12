import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class SchedulerPriority extends SchedulerBase implements Scheduler{

    private Queue<Process> ready = new PriorityQueue<>(Comparator.comparingInt(Process::getPriority));
    private Logger logger;

    public SchedulerPriority(Logger logger){
        this.logger = logger;
        
    }
    public void notifyNewProcess(Process p){
        this.ready.add(p);
    }
    public Process update(Process cpu){
        if (cpu != null && (cpu.isBurstComplete() || cpu.isExecutionComplete())) {
            this.contextSwitches++;
            logger.log(String.format("Process %s burst complete", cpu.getName()));
            if (!cpu.isExecutionComplete()) {
                ready.add(cpu);
            } else {
                logger.log(String.format("Process %s execution complete", cpu.getName()));
            }
            cpu = null;
        }

        if (cpu == null && !ready.isEmpty()) {
            this.contextSwitches++;
            cpu = ready.poll();
            logger.log(String.format("Scheduled: %s", cpu.getName()));
        }

        return cpu;
    }
}
