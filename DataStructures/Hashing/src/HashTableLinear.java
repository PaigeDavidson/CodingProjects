public class HashTableLinear extends HashTable{
    public HashTableLinear(){
        this(DEFAULT_TABLE_SIZE, 50);
        load = 50;
        doClear();
        debug=false;

    }
    public HashTableLinear(int size, int load){
        allocateArray(size);
        this.load = load;
        doClear();
        debug=false;
    }
    protected int findPos(String x) {
        int currentPos = myhash(x);
        int thisProbe=1;
        probeCt++;
        // while the current position already has something in it and the array element does not equal x...
        while (array[currentPos] != null &&
                !array[currentPos].element.equals(x)) {
            // go to the next position on the list and check that one
            currentPos += 1;
            // increase the probe count
            probeCt++;
            thisProbe++;
            if (currentPos >= array.length)
                currentPos -= array.length;
        }
        //update probe count
        if (thisProbe > maxProbeCt){
            maxProbeCt=thisProbe;
        }
        return currentPos;
    }
}
