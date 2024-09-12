public class HashTableDouble extends HashTable{
    public HashTableDouble(){
        this(DEFAULT_TABLE_SIZE, 50);
        load = 50;
        doClear();
        debug=false;

    }
    public HashTableDouble(int size, int load){
        allocateArray(size);
        this.load = load;
        doClear();
        debug=false;
    }
    protected int findPos(String x) {
        int currentPos = myhash(x);
        int thisProbe=1;
        int secondHash = myHash2(x);
        probeCt++;
        // if the current position already has something in it and the array element does not equal x...
        while (array[currentPos] != null &&
                !array[currentPos].element.equals(x)) {
            // go to the next position on the list and check that one
            currentPos += secondHash;
            // increase the probe count
            probeCt++;
            thisProbe++;
            if (currentPos >= array.length)
                currentPos -= array.length;
        }
        if (thisProbe > maxProbeCt){
            maxProbeCt=thisProbe;
        }
        return currentPos;
    }
    protected int myHash2(String x) {
        int hashVal2 = 101 - (x.hashCode() % 101);

        return hashVal2;
    }
}
