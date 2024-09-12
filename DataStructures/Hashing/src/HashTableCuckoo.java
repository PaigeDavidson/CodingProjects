import java.io.BufferedReader;
//import java.io.IOException;
//import java.text.DecimalFormat;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Arrays;
public class HashTableCuckoo implements HashTableInterface{
    protected static final int DEFAULT_TABLE_SIZE = 101;

    String[] array1;
    String[] array2;

    protected int occupiedCt;         // The number of occupied cells: active or deleted
    protected int currentActiveEntries;                  // Current size
    protected int probeCt;
    protected int maxProbeCt;
    protected int insertCt;
    protected int rehashCt;
    protected int load;
    protected boolean debug;

    public HashTableCuckoo(){
        //two arrays not one, and you don't need the hash entry
        //the table will just be a table of strings
        //inserts is the main difference
        // you want a hash function that gives you a good spread
        this(DEFAULT_TABLE_SIZE, 50);
        load = 50;
        doClear();
        debug=false;

    }
    public HashTableCuckoo(int size, int load){
        allocateArray(size);
        this.load = load;
        doClear();
        debug=false;
    }
    public int hash1(String key) {
        int hashVal = 0;
        for (char c: key.toCharArray()) {
            hashVal = (hashVal <<5)^c^hashVal;
        }
        hashVal = hashVal %array1.length;
        if (hashVal < 0) hashVal+=array1.length;
        return hashVal;
    }
    public int hash2(String key) {
        int hashVal = key.hashCode();

        hashVal %= array2.length;
        if (hashVal < 0)
            hashVal += array2.length;

        return hashVal;
    }
    protected void allocateArray(int arraySize) {
        array1 = new String[nextPrime(arraySize)];
        array2 = new String[nextPrime(arraySize)];
        doClear();
    }
    protected void doClear() {
        occupiedCt = 0;
        Arrays.fill(array1, null);
        Arrays.fill(array2, null);
    }
    protected static int nextPrime(int n) {
        if (n % 2 == 0)
            n++;

        for(; !isPrime(n); n += 2) {
            ;
        }

        return n;
    }


    /**
     * Internal method to test if a number is prime.
     * Not an efficient algorithm.
     *
     * @param n the number to test.
     * @return the result of the test.
     */
    protected static boolean isPrime(int n) {
        if (n == 2 || n == 3)
            return true;

        if (n == 1 || n % 2 == 0)
            return false;

        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0)
                return false;

        return true;
    }

    @Override
    public String toString(int limit) {
        StringBuilder sb = new StringBuilder();
        int ct = 0;
        for (int i = 0; i < array1.length && ct < limit; i++) {
            if (array1[i] != null) {
                sb.append(i + ": " + array1[i] + "\n");
                ct++;
            }
        }
        for (int i = 0; i < array2.length && ct < limit; i++) {
            if (array2[i] != null) {
                sb.append(i + ": " + array2[i] + "\n");
                ct++;
            }
        }
        return sb.toString();
    }
    /**
     * Find an item in the hash table.
     * @param x the item to search for.
     * @return the matching item.
     */
    public Boolean find(String x) {
        int thisProbe = 0;
        //if it's in the first table, return the element
        //look in the second table
        //otherwise return value not found
        int location1 = hash1(x);
        int location2 = hash2(x);
        probeCt++;
        thisProbe++;
        if(maxProbeCt < thisProbe){
            maxProbeCt = thisProbe;
        }
        if(array1[location1] != null && array1[location1].equals(x)){
            return true;
        }
        probeCt++;
        thisProbe++;
        if(maxProbeCt < thisProbe){
            maxProbeCt = thisProbe;
        }
        if(array2[location2] != null && array2[location2].equals(x)){
            return true;
        }
        return false;
    }
    protected void rehash() {
        String[] oldArray1 = array1;
        String[] oldArray2 = array2;

        // Create a set of new tables that are doubled the size of the old ones and empty
        //where both arrays are updated in the allocateArray function
        allocateArray(2 * oldArray1.length);
        occupiedCt = 0;
        currentActiveEntries = 0;

        // insert the values back into the arrays
        for (String entry : oldArray1)
            if (entry != null)
                insert(entry);
        for (String entry : oldArray2)
            if (entry != null)
                insert(entry);
    }
    public void insert(String x) {
        int thisProbe = 0;
        if (find(x)){
            return;
        } // don’t insert duplicates
        //if the loop loops more than 100 times we can assume the loop is infinite and rehash the table
        for(int i = 0; i < 30; i++){
            int location1 = hash1(x);
            //if the location in table one is empty, insert the value in there
            probeCt++;
            thisProbe++;
            if(thisProbe > maxProbeCt){
                maxProbeCt = thisProbe;
            }
            if (array1[location1] == null){
                array1[location1]=x;
                return;
            }
            //if there is a value in the first location, get the old value
            String oldValue = array1[location1];
            //put x in the place of the old value
            array1[location1]=x;
            //and put the old value in its place in the second table
            int location2 = hash2(oldValue); //location for the displaced old value in table 2
            probeCt++;
            thisProbe++;
            if(thisProbe > maxProbeCt){
                maxProbeCt = thisProbe;
            }
            // if the location for the old value in table two is empty, put the old value in table 2
            if (array2[location2] == null){
                array2[location2]=oldValue;
                return;
            }
            // if there is already a value in the table 2 location, this value becomes the new x,
            // and we go through the loop again until the item is inserted into an empty field
            x=array2[location2];
            array2[location2]=oldValue;
        }
        rehash();
        insert(x);

    }
    /**
     * Insert all words in file into hashtable
     * @param sc File containing words to add
     * @param max Maximum number of words to add (used for debug)
     */
    public void insertAll(BufferedReader sc,int max) {
        DecimalFormat df = new DecimalFormat("0.00");
        try {
            probeCt = 0;
            maxProbeCt=0;
            insertCt = 0;
            rehashCt = 0;
            String w;
            while (insertCt <=max &&(w = (String) sc.readLine()) != null) {
                insert(w);
                insertCt++;
            }
            System.out.println("*** TableSize " + array1.length + " Inserted " + insertCt +
                    "  load factor (" + load + "%) probes " + probeCt + " Average Cost " + df.format(probeCt / (float) insertCt) + " maxCost = " + maxProbeCt);
            if (rehashCt > 0) System.out.println(" Rehashed " + rehashCt);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Try to find all words in a file
     * @param sc File containing words to find
     * @param msg Message to describe the kind of test this is (Not there, present, mixture)
     */
    public void findAll(BufferedReader sc, String msg) {
        try {
            DecimalFormat df = new DecimalFormat("0.00");
            probeCt = 0;
            maxProbeCt=0;
            int ct = 0;
            int foundCt = 0;
            rehashCt = 0;
            String w;
            while ((w = (String) sc.readLine()) != null) {
                ct++;
                if (find(w)) foundCt++;
                else {
                    if (debug) {
                        System.out.println(" Not Found  '" + w + "' at line " + ct);
                    }
                }
            }
            System.out.println(msg + " Looked for " + ct + " Found " + foundCt +  " probes " + probeCt +
                    " Average Cost " + df.format(probeCt / (float) ct)+ " maxCost = " + maxProbeCt);
            if (rehashCt > 0) System.out.println(" Rehashed " + rehashCt);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
