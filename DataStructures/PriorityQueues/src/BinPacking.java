import java.util.Arrays;
import java.util.Random;
public class BinPacking {
    static int BINSIZE=100;
    Integer [] requests;
    BinPacking(int size){
        Random rand = new Random(size);
        //Seed will cause the same sequence of numbers to be generated each test
        requests = new Integer[size];
        for (int i=0; i < size; i++){
            requests[i] =rand.nextInt(BINSIZE)+1;
        }
        if (size <=500 ) System.out.println("Size " + size + " "
                +Arrays.toString(requests));
    }
    public int getMinBins(){
        int numBins = 0;

        for (Integer request : requests) {
            numBins += request;
        }
        return (int) Math.ceil((double) numBins / 100);
    }
    public int scheduleWorstFit(boolean sort, String message){
        // if you are sorting first, create a new heap and sort the requests into the heap
        if(sort){
            HeapSort<Integer> reverseHeap = new HeapSort<>();
            reverseHeap.sort(requests);
        }
        //otherwise insert the disks into the left heap

        //create new heap
        MaxLeftHeap<Disk> leftHeap = new MaxLeftHeap<>();
        //create the first disk
        Disk disk = new Disk(1, BINSIZE);
        //insert disk into heap
        leftHeap.insert(disk);

        //for each file in the requests
        int id = 1;
        for(int file : requests){
            //get this first disk in the heap
            Disk firstDisk = leftHeap.findMax();
            // if the first disk isn't null and there is space, insert the file
            if(firstDisk != null && firstDisk.remainingSpace >= file){
                firstDisk.add(file);
                leftHeap.deleteMax();
                leftHeap.insert(firstDisk);
            //otherwise create a new disk and add it to that disk
            }else{
                Disk newDisk = new Disk(++id, BINSIZE);
                newDisk.add(file);
                leftHeap.insert(newDisk);
            }
        }
        System.out.println(message + id + " (requestCt=" + requests.length +
                ") Minimum number of bins " + getMinBins());

        if (requests.length <= 20){
            while(!leftHeap.isEmpty()){
                System.out.println(leftHeap.deleteMax());
            }
        }
        return id;

    }



    public static void main (String[] args) {
        int [] fileSizes = {10, 20, 100, 500,10000,100000};
        for (int size :fileSizes){
            BinPacking b = new BinPacking(size);
            int online = b.scheduleWorstFit(false, "OnLine worst Fit Bin Packing Yields ");
            int offline = b.scheduleWorstFit(true, "Decreasing Worst Fit Bin Packing Yields ");

            int difference = online - offline;
            int percent = (int)(((double)offline / (double)online) * 100);

            if(online == offline){
                System.out.println("BOTH are the same");
            }else if(offline < online){
                System.out.println("Decreasing Worst fit is better " + difference + " " + percent + "%");
            }else{
                System.out.println("Decreasing Worst fit is worse " + difference + " " + percent + "%");
            }
        }


    }}

