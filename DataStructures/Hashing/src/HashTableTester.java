import java.io.BufferedReader;
import java.io.FileReader;

public class HashTableTester {
    public static void main(java.lang.String[] args) {
        int FILESIZE = 12972;
        int TESTMAX = 4;
        HashTableInterface H;
        try {
            for (int test = 1; test <= TESTMAX; test++)
                for (int load = 30; load < 100; load += 5) {
                    int tablesize = FILESIZE * 100 / load;
                    switch (test) {
                        case 1:
                            System.out.println("LINEAR PROBING");
                            H = new HashTableLinear(tablesize, load);
                            break;
                        case 2:
                            System.out.println("QUADRATIC PROBING");
                            H = new HashTable(tablesize, load);
                            break;
                        case 3:
                            System.out.println("DOUBLE HASHING");
                            H = new HashTableDouble(tablesize, load);
                            break;
                        default:
                            System.out.println("CUCKOO HASHING");
                            H = new HashTableCuckoo(tablesize, load);
                    }

                    BufferedReader words = new BufferedReader(new FileReader("words5.txt"));
                    H.insertAll(words, FILESIZE);
                    words.close();

                    BufferedReader randomWords = new BufferedReader(new FileReader("5words.txt"));
                    H.findAll(randomWords, " Present ");
                    randomWords.close();


                    BufferedReader capWords = new BufferedReader(new FileReader("wordCap.txt"));
                    H.findAll(capWords, " NotThere");
                    capWords.close();
                }
        } catch (Exception e) {
            System.out.println("Exception " + e);
        }
    }


}