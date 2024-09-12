import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class TaskFIFO implements Runnable{

    private int[] sequence;
    private int maxMemoryFrames;
    private int[] pageFaults;
    
    public TaskFIFO(int[] sequence, int maxMemoryFrames, int maxPageReference, int[] pageFaults){
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.pageFaults = pageFaults;

    }

    @Override
    public void run(){
        // Use a queue to simulate the frames of memory
        Queue<Integer> memoryFrames = new ArrayDeque<>(maxMemoryFrames);
        Set<Integer> memorySet = new HashSet<>(maxMemoryFrames);

        int faults = 0;

        // Iterate through the page reference sequence
        for (int pageNumber : sequence) {
            // If the page is not in memory, it's a page fault
            if (!memorySet.contains(pageNumber)) {
                faults++;
                // If memory is full, remove the oldest page
                if (memoryFrames.size() == maxMemoryFrames) {
                    int removedPage = memoryFrames.poll();
                    memorySet.remove(removedPage);
                }
                // Add the new page to memory
                memoryFrames.offer(pageNumber);
                memorySet.add(pageNumber);
            }
        }

        // Store the number of page faults
        pageFaults[maxMemoryFrames] = faults;
    }
    
}
