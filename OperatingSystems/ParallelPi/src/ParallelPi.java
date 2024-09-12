import java.util.LinkedList;
import java.util.HashMap;
import java.util.ArrayList;

public class ParallelPi {
    final static int NUM_DIGITS = 1001;
    private static int reportCount = 0;

    public static synchronized void report() {
        reportCount++;
        if (reportCount % 10 == 0) {
            System.out.print(".");
            System.out.flush();
        }

        if (reportCount % 200 == 0) {
            System.out.println();
        }
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        TaskQueue taskQueue = new TaskQueue(ParallelPi.NUM_DIGITS);
        ResultTable resultTable = new ResultTable();


        try {
            ArrayList<Thread> myArray = new ArrayList<>();
            for (int cpu = 1; cpu <= Runtime.getRuntime().availableProcessors(); cpu++) {
                Thread t = new Thread(new ComputePiWorker(taskQueue, resultTable, ParallelPi::report));
                t.start();
                myArray.add(t);
            }

            for (Thread t : myArray) {
                try{
                    t.join();
                } catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
        finally{

        }
        
        // Print computed value of Pi
        StringBuilder piDigits = new StringBuilder();
        for (int i = 1; i < NUM_DIGITS; i++) {
            String digit = resultTable.getResult(i);
            piDigits.append(digit);
        }
        System.out.println();

        long endTime = System.currentTimeMillis();
        System.out.println("3." + piDigits);
        System.out.println("Pi computation took " + (endTime - startTime) + " ms");
    }
}
class TaskQueue {
    private LinkedList<String> taskQueue;

    public TaskQueue(int numDigits) {
        taskQueue = new LinkedList<>();
        for (int i = 1; i < numDigits; i++) {
            taskQueue.add(Integer.toString(i)); // Add a task for each digit to be computed
        }
        java.util.Collections.shuffle(taskQueue); // Shuffle the queue
    }

    public synchronized String dequeue() {
        return taskQueue.poll();
    }
}
class ResultTable {
    private HashMap<Integer, String> table;

    public ResultTable() {
        table = new HashMap<>();
    }

    public synchronized void putResult(int position, String digit) {
        table.put(position, digit);
    }

    public synchronized String getResult(int position) {
        return table.getOrDefault(position, "0");
    }
}

class ComputePiWorker implements Runnable {
    private TaskQueue taskQueue;
    private ResultTable results;
    private Runnable report;

    public ComputePiWorker(TaskQueue taskQueue, ResultTable results, Runnable report) {
        this.taskQueue = taskQueue;
        this.results = results;
        this.report = report;
    }

    @Override
    public void run() {
        Bpp bpp = new Bpp();
        String task;
        do {
            task = this.taskQueue.dequeue();
            if (task != null) {
                int digit = Integer.parseInt(task);
                String value = computeDigit(bpp.getDecimal(digit));
                results.putResult(digit, value);
                this.report.run();
            }
        } while (task != null);
    }

    private String computeDigit(long value) {
        if (value < 100000000) return "0";
        while (value >= 10) {
            value /= 10;
        }
        return Long.toString(value);
    }
}




