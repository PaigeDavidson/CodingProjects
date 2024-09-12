import java.util.LinkedHashMap;
import java.util.Map;

public class TaskLRU implements Runnable{
    private static final int MAX_PAGE_REFERENCE = 250;

    private int[] sequence;
    private int maxMemoryFrames;
    private int[] pageFaults;

    public TaskLRU(int[] sequence, int maxMemoryFrames, int maxPageReference, int[] pageFaults){
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.pageFaults = pageFaults;
    }

    @Override
    public void run(){
        // Use a LinkedHashMap to simulate the frames of memory with access order
        Map<Integer, Integer> memoryFrames = new LinkedHashMap<>(maxMemoryFrames, 0.75f, true);
        int faults = 0;

        // Iterate through the page reference sequence
        for (int pageNumber : sequence) {
            // If the page is not in memory, it's a page fault
            if (!memoryFrames.containsKey(pageNumber)) {
                faults++;
                // If memory is full, remove the least recently used page
                if (memoryFrames.size() == maxMemoryFrames) {
                    memoryFrames.remove(memoryFrames.entrySet().iterator().next().getKey());
                }
            }
            // Add the page to memory or update its access order
            memoryFrames.put(pageNumber, 0);
        }

        // Store the number of page faults
        pageFaults[maxMemoryFrames] = faults;

    }

    public static void testLRU() {
        int[] sequence1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] sequence2 = {1, 2, 1, 3, 2, 1, 2, 3, 4};
        int[] testSequence = {5, 1, 4, 3, 0, 2, 1, 3, 0, 5, 4, 0, 1, 0, 5, 2, 1, 2, 3, 1, 0, 5, 3};
        int[] pageFaults = new int[4];  // 4 because maxMemoryFrames is 3
    
        // Replacement should be: 1, 2, 3, 4, 5, 6, 7, 8
        // Page Faults should be 9
        (new TaskLRU(sequence1, 1, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[1]);
    
        // Replacement should be: 2, 1, 3, 1, 2
        // Page Faults should be 7
        (new TaskLRU(sequence2, 2, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[2]);
    
        // Replacement should be: 1
        // Page Faults should be 4
        (new TaskLRU(sequence2, 3, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[3]);

        (new TaskLRU(testSequence, 3, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page faults: %d\n", pageFaults[3]);


    }
    public static void main(String[] args) {
        testLRU();
    }
    
}
