import java.util.Scanner;

public class ArraysNThings {
    public static void main(String[] args) {

        int[] myArray = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
        int whichOne = 23;
        if binarySearch(primes, whichOne)) {
            System.out.println();
        }else{
            System.out.println("the value was not found");
        }


        public static boolean binarySearch(int[] data, int search){
            int lower = 0;
            int upper = data.length - 1;

            while (lower <= upper) {
                int middle = lower / 2 + upper / 2;
                if (data[middle] == search) {
                    return true;
                }
                if (search < data[middle]) {

                } else {
                    lower = middle + 1
                }
                return false;
            }
        }
    }
}