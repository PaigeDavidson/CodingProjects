import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

public class Assign5 {

    private static final int NUM_SIMULATIONS = 1000;
    private static final int PAGE_SEQUENCE_LENGTH = 1000;
    private static final int MAX_PAGE_REFERENCE = 250;
    private static final int NUM_MEMORY_FRAMES = 100;

    public static void main(String[] args) {
        try {
            long startTime = System.currentTimeMillis();

            int processors = Runtime.getRuntime().availableProcessors();

            // Counts for minimum page faults
            int fifoMinCount = 0;
            int lruMinCount = 0;
            int mruMinCount = 0;

            // Variables for Belady's Anomaly
            int anomolyNumFifo = 0;
            int anomolyNumLru = 0;
            int anomolyNumMru = 0;

            int maxDiffFifo = 0;
            int maxDiffLru = 0;
            int maxDiffMru = 0;

            List<String> fifoList = new ArrayList<>();
            List<String> lruList = new ArrayList<>();
            List<String> mruList = new ArrayList<>();

            // Arrays to store page faults
            int[] fifoPageFaults = new int[NUM_MEMORY_FRAMES + 1];
            int[] lruPageFaults = new int[NUM_MEMORY_FRAMES + 1];
            int[] mruPageFaults = new int[NUM_MEMORY_FRAMES + 1];

            

            for (int i = 0; i < NUM_SIMULATIONS; i++) {
                // Generate page reference sequence
                int[] pageReferenceSequence = generatePageReferenceSequence();

                ExecutorService executor = Executors.newFixedThreadPool(processors);

                // Run simulations for different memory frames
                for (int frames = 1; frames <= NUM_MEMORY_FRAMES; frames++) {
                    TaskFIFO fifoTask = new TaskFIFO(pageReferenceSequence, frames, MAX_PAGE_REFERENCE, fifoPageFaults);
                    TaskLRU lruTask = new TaskLRU(pageReferenceSequence, frames, MAX_PAGE_REFERENCE, lruPageFaults);
                    TaskMRU mruTask = new TaskMRU(pageReferenceSequence, frames, MAX_PAGE_REFERENCE, mruPageFaults);

                    executor.execute(fifoTask);
                    executor.execute(lruTask);
                    executor.execute(mruTask);

                }

                executor.shutdown();
                executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);

                // Calculate occurance of minimum page faults
                for (int frames = 1; frames < NUM_MEMORY_FRAMES; frames++) {
                    int fifoPageFault = fifoPageFaults[frames];
                    int lruPageFault = lruPageFaults[frames];
                    int mruPageFault = mruPageFaults[frames];

                    if(fifoPageFault <= lruPageFault && fifoPageFault <= mruPageFault){
                        fifoMinCount++;
                    }
                    if(lruPageFault <= fifoPageFault && lruPageFault <= mruPageFault){
                        lruMinCount++;
                    }
                    if(mruPageFault <= lruPageFault && mruPageFault <= fifoPageFault){
                        mruMinCount++;
                    }
                }
                
                // Calculate Belady's Anomaly
                for (int frames = 1; frames < NUM_MEMORY_FRAMES; frames++) {
                    int Fdiff = fifoPageFaults[frames + 1] - fifoPageFaults[frames];
                    int Ldiff = lruPageFaults[frames + 1] - lruPageFaults[frames];
                    int Mdiff = mruPageFaults[frames + 1] - mruPageFaults[frames];

                    // fifo
                    if (Fdiff > maxDiffFifo) {
                        maxDiffFifo = Fdiff;
                    }
                    if (Fdiff > 0) {
                        anomolyNumFifo++;
                        fifoList.add("\tDetected - Previous " + fifoPageFaults[frames] + " : Current " + fifoPageFaults[frames + 1] + " (" + Fdiff + ")");
                    }
                    // lru
                    if (Ldiff > maxDiffFifo) {
                        maxDiffLru = Fdiff;
                    }
                    if (Ldiff > 0) {
                        anomolyNumLru++;
                        lruList.add("\tDetected - Previous " + lruPageFaults[frames] + " : Current " + lruPageFaults[frames + 1] + " (" + Ldiff + ")");
                    }
                    // mru
                    if (Mdiff > maxDiffFifo) {
                        maxDiffMru = Fdiff;
                    }
                    if (Mdiff > 0) {
                        anomolyNumMru++;
                        mruList.add("\tDetected - Previous " + mruPageFaults[frames] + " : Current " + mruPageFaults[frames + 1] + " (" + Mdiff + ")");
                    }
                }

                // Reset executor for next simulation
                executor = Executors.newFixedThreadPool(processors);
            }

            long endTime = System.currentTimeMillis();

            // Output results
            long time = endTime - startTime;
            System.out.println();
            System.out.println("Simulation took " + time + " ms");
            System.out.println();
            System.out.println("FIFO min PF : " + fifoMinCount);
            System.out.println("LRU min PF  : " + lruMinCount);
            System.out.println("MRU min PF  : " + mruMinCount);
            System.out.println();

            // Belady's Anomaly Report
            System.out.println("Belady's Anomaly Report for FIFO");
            for (String str : fifoList) {
                System.out.println(str);
            }
            System.out.println("\tAnomaly detected " + anomolyNumFifo + " times with a max difference of " + maxDiffFifo);

            System.out.println("Belady's Anomaly Report for LRU");
            for (String str : lruList) {
                System.out.println(str);
            }
            System.out.println("\tAnomaly detected " + anomolyNumLru + " times with a max difference of " + maxDiffLru);

            System.out.println("Belady's Anomaly Report for MRU");
            for (String str : mruList) {
                System.out.println(str);
            }
            System.out.println("\tAnomaly detected " + anomolyNumMru + " times with a max difference of " + maxDiffMru);

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static int[] generatePageReferenceSequence() {
        Random rand = new Random();
        int[] pageReferences = new int[PAGE_SEQUENCE_LENGTH];
        for (int i = 0; i < PAGE_SEQUENCE_LENGTH; i++) {
            pageReferences[i] = rand.nextInt(MAX_PAGE_REFERENCE) + 1;
        }
        return pageReferences;
    }
}
