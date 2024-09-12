/**
 * Assignment 4 for CS 1410
 * This program evaluates the linear and binary searching, along
 * with comparing performance difference between the selection sort
 * and the built-in java.util.Arrays.sort.
 *
 * @author James Dean Mathias
 */

import java.util.Random;
import java.util.Arrays;
public class EvaluationDriver {
    static final int MAX_VALUE = 1_000_000;
    static final int MAX_ARRAY_SIZE = 100_000;
    static final int ARRAY_INCREMENT = 20_000;
    static final int NUMBER_SEARCHES = 50_000;

    public static void main(String[] args) {

        demoLinearSearchUnsorted();
        demoLinearSearchSorted();
        demoBinarySearchSelectionSort();
        demoBinarySearchFastSort();
    }

    public static void demoLinearSearchUnsorted(){
        Random rand = new Random();
        System.out.println("--- Linear Search Timing (unsorted) ---");

        int numItem = 0;

        for(int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i = i + ARRAY_INCREMENT){
            int[] randomArray = generateNumbers(i,MAX_VALUE);
            int timesFound = 0;
            long searchTime = 0;
            long startTime = System.currentTimeMillis();
            numItem += ARRAY_INCREMENT;
            for(int j = 1; j <= NUMBER_SEARCHES; j++){
                int randomNumber = rand.nextInt(MAX_VALUE + 1);
                if(randomArray != null && linearSearch(randomArray, randomNumber)){
                    timesFound += 1;
                }

            }
            long endTime = System.currentTimeMillis();
            searchTime += endTime - startTime;
            System.out.println("Number of items       : " + numItem);
            System.out.println("Times value was found : " + timesFound);
            System.out.println("Total search time     : " + searchTime + " ms");
            System.out.println();
        }
    }

    public static void demoLinearSearchSorted(){
        Random rand = new Random();
        System.out.println("--- Linear Search Timing (Selection Sort) ---");
        int numItem = 0;

        for(int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i = i + ARRAY_INCREMENT){
            int[] randomArray = generateNumbers(i,MAX_VALUE);
            int timesFound = 0;
            long searchTime = 0;
            long startTime = System.currentTimeMillis();
            numItem += ARRAY_INCREMENT;
            if(randomArray != null){
                //sort once
                selectionSort(randomArray);
                // generate random number and then do a linear search NUMBER_SEARCHES times
                for(int j = 1; j <= NUMBER_SEARCHES; j++){
                    int randomNumber = rand.nextInt(MAX_VALUE + 1);
                    if(linearSearch(randomArray, randomNumber)){
                        timesFound += 1;
                    }
                }

            }
            long endTime = System.currentTimeMillis();
            searchTime += endTime - startTime;
            System.out.println("Number of items       : " + numItem);
            System.out.println("Times value was found : " + timesFound);
            System.out.println("Total search time     : " + searchTime + " ms");
            System.out.println();
        }
    }

    public static void demoBinarySearchSelectionSort(){
        Random rand = new Random();
        System.out.println("--- Binary Search Timing (Selection Sort) ---");
        int numItem = 0;

        for(int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i = i + ARRAY_INCREMENT){
            int[] randomArray = generateNumbers(i,MAX_VALUE);
            int timesFound = 0;
            long searchTime = 0;
            long startTime = System.currentTimeMillis();
            numItem += ARRAY_INCREMENT;
            if(randomArray != null){
                //sort once
                selectionSort(randomArray);
                // generate random number and then do a binary search NUMBER_SEARCHES times
                for(int j = 1; j <= NUMBER_SEARCHES; j++){
                    int randomNumber = rand.nextInt(MAX_VALUE + 1);
                    if(binarySearch(randomArray, randomNumber)){
                        timesFound += 1;
                    }
                }

            }
            long endTime = System.currentTimeMillis();
            searchTime += endTime - startTime;
            System.out.println("Number of items       : " + numItem);
            System.out.println("Times value was found : " + timesFound);
            System.out.println("Total search time     : " + searchTime + " ms");
            System.out.println();
        }

    }

    public static void demoBinarySearchFastSort(){
        Random rand = new Random();
        System.out.println("--- Binary Search Timing (Arrays.sort) ---");
        int numItem = 0;

        for(int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i = i + ARRAY_INCREMENT){
            int[] randomArray = generateNumbers(i,MAX_VALUE);
            int timesFound = 0;
            long searchTime = 0;
            long startTime = System.currentTimeMillis();
            numItem += ARRAY_INCREMENT;
            if(randomArray != null){
                //sort
                Arrays.sort(randomArray);
                // generate random number and then do a binary search NUMBER_SEARCHES times
                for(int j = 1; j <= NUMBER_SEARCHES; j++){
                    int randomNumber = rand.nextInt(MAX_VALUE + 1);
                        if(binarySearch(randomArray, randomNumber)){
                            timesFound += 1;
                        }
                }
            }
            long endTime = System.currentTimeMillis();
            searchTime += endTime - startTime;
            System.out.println("Number of items       : " + numItem);
            System.out.println("Times value was found : " + timesFound);
            System.out.println("Total search time     : " + searchTime + " ms");
            System.out.println();
        }


    }

    public static int[] generateNumbers(int howMany, int maxValue){
        if(howMany <= 0){
            return null;
        }else{
            int[] numArray = new int[howMany];
            for(int i  = 0; i < howMany; i++){
                numArray[i] = (int) (Math.random() * maxValue);
            }
            return numArray;
        }

    }
    public static boolean linearSearch(int[] data, int search){
        for(int i = 0; i < data.length; i++){
            if(data[i] == search){
                return true;
            }
        }
        return false;
    }
    public static boolean binarySearch(int[] data, int search){
        int lower = 0;
        int upper = data.length - 1;

        while(lower <= upper ){
            int middle = lower + (upper - lower) / 2;
            if(data[middle] == search){
                return true;
            }
            if(search <= data[middle]){
                upper = middle - 1;
            }else{
                lower = middle + 1;
            }
        }
        return false;
    }
    public static void selectionSort(int[] data){
        for(int i = 0; i < data.length - 1; i++){
            int smallest = data[i];
            int currentSmallest = i;
            for(int j = i + 1; j < data.length; j++){
                if(smallest > data[j]){
                    smallest = data[j];
                    currentSmallest = j;
                }
            }
            if(currentSmallest != i){
                data[currentSmallest] = data[i];
                data[i] = smallest;
            }

        }
    }


}
