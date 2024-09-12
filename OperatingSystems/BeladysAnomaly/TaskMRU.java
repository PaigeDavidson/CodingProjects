import java.util.LinkedHashMap;
import java.util.Map;

public class TaskMRU implements Runnable{
    private static final int MAX_PAGE_REFERENCE = 250;

    private int[] sequence;
    private int maxMemoryFrames;
    private int[] pageFaults;
    
    public TaskMRU(int[] sequence, int maxMemoryFrames, int maxPageReference, int[] pageFaults){
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.pageFaults = pageFaults;
    }
    public void run(){
        // Use a LinkedHashMap to simulate the frames of memory with access order
        Map<Integer, Integer> memoryFrames = new LinkedHashMap<>(maxMemoryFrames, 0.75f, true);
        int faults = 0;

        // Iterate through the page reference sequence
        for (int pageNumber : sequence) {
            // If the page is not in memory, it's a page fault
            if (!memoryFrames.containsKey(pageNumber)) {
                faults++;
                // If memory is full, remove the most recently used page
                if (memoryFrames.size() == maxMemoryFrames) {

                    Map.Entry<Integer, Integer> lastEntry = null;
                    for(Map.Entry<Integer, Integer> entry : memoryFrames.entrySet()){
                        lastEntry = entry;
                    }
                    if(lastEntry != null){
                        memoryFrames.remove(lastEntry.getKey());
                    }
                }
            }
            // Add the page to memory or update its access order
            memoryFrames.put(pageNumber, 0);
        }

        // Store the number of page faults
        pageFaults[maxMemoryFrames] = faults;

    }
    public static void testMRU() {
        int[] sequence1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] sequence2 = {1, 2, 1, 3, 2, 1, 2, 3, 4};
        int[] pageFaults = new int[4];  // 4 because maxMemoryFrames is 3
    
        // Replacement should be: 1, 2, 3, 4, 5, 6, 7, 8
        // Page Faults should be 9
        (new TaskMRU(sequence1, 1, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[1]);
    
        // Replacement should be: 1, 2, 1, 3
        // Page Faults should be 6
        (new TaskMRU(sequence2, 2, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[2]);
    
        // Replacement should be: 3
        // Page Faults should be 4
        (new TaskMRU(sequence2, 3, MAX_PAGE_REFERENCE, pageFaults)).run();
        System.out.printf("Page Faults: %d\n", pageFaults[3]);
    }
    public static void main(String[] args) {
        testMRU();
    }
    
    
}
