import java.util.LinkedList;
import java.util.Queue;
import java.util.Collections;
import java.util.Comparator;

public class SchedulerSJF extends SchedulerBase implements Scheduler{

    private Queue<Process> ready = new LinkedList<>(); // simple FIFO queue for this scheduling algorithm
    private Logger logger;

    public SchedulerSJF(Logger logger){
        this.logger = logger;
    }

    public void notifyNewProcess(Process p){
        this.ready.add(p);
    }
    public Process update(Process cpu){
        // Shortest Job First scheduling
        if (cpu != null) {
            if (cpu.isBurstComplete() || cpu.isExecutionComplete()) {
                this.contextSwitches++;
                this.logger.log(String.format("Process %s burst complete", cpu.getName()));
                if (!cpu.isExecutionComplete()) {
                    ready.add(cpu);
                } else {
                    this.logger.log(String.format("Process %s execution complete", cpu.getName()));
                }
                cpu = null;
            }
        }

        // Sort the ready queue based on total time
        Collections.sort((LinkedList<Process>) ready, new Comparator<Process>() {
            @Override
            public int compare(Process p1, Process p2) {
                return Integer.compare(p1.getTotalTime(), p2.getTotalTime());
            }
        });

        // Give the new process to the CPU
        if (cpu == null && !ready.isEmpty()) {
            this.contextSwitches++;
            cpu = ready.poll();
            this.logger.log(String.format("Scheduled: %s", cpu.getName()));
        }

        return cpu;
    }
}
