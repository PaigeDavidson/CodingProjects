public class Teacups {
    // amt: Number of teacups left to divide
    // soFar is the teaset sizes I’ve already decided to use
    // currentSize maximum additional teaset size I’m considering (helps to make progress)
    //valueSoFar amount of money I get from selling the teacup sets listed in soFar.
    int[][] matrix;
    int setSizes;
    int teacups;
    int[] setSizeValues;

    public Teacups(int setSizes, int teacups, int[] setSizeValues){
        this.setSizes = setSizes;
        this.teacups = teacups;
        matrix = new int[setSizes + 1][teacups + 1];
        this.setSizeValues = setSizeValues;

    }

    void printChoices(int amt, String soFar, int currentSize, int valueSoFar){
        if(amt == 0){
            System.out.println(soFar + " $" + valueSoFar);
            return;
        }
        if(currentSize > 1){
            printChoices(amt, soFar, currentSize - 1, valueSoFar);
        }
        // If the current size is within the desired amount
        if (currentSize <= amt) {
            printChoices(amt - currentSize, soFar + " " + currentSize, currentSize, valueSoFar + setSizeValues[currentSize]);
        }
    }

    public void printTable(){
        //set zeros for first row
        for(int i = 0; i <= setSizes; i++){
            matrix[i][0] = 0;
        }
        for(int i = 0; i <= teacups; i++){
            matrix[0][i] = 0;
        }
        //populate
        for (int i = 1; i <= setSizes; i++) {
            for (int j = 1; j <= teacups; j++) {
                int dontUse = matrix[i-1][j];
                if(j < i){
                    matrix[i][j] = dontUse;
                }else{
                    int value = setSizeValues[i];
                    int use = matrix[i][j-i] + value;
                    matrix[i][j] = Math.max(use, dontUse);
                }
            }
        }
        //print table
        System.out.print("\t");
        for(int top = 0; top <= teacups; top++){
            System.out.print(top + "\t");
        }
        System.out.println();
        for (int i = 0; i <= setSizes; i++) {
            System.out.print(i + "\t");
            for (int j = 0; j <= teacups; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }

    }

    void pickBest(int teacups){
        //print the best dollar amount possible from the sale and the way the cups were divided for sale.
        String choices = "";
        int remainingTeacups = teacups;
        int size = setSizes;
        while(remainingTeacups > 0){
            if(matrix[size][remainingTeacups] != matrix[size - 1][remainingTeacups]){
                choices = choices + " " + size;
                remainingTeacups -= size;
            }else{
                size--;
            }
        }
        System.out.println("Best sum for (" + teacups + ") : $" + matrix[setSizes][teacups] + " " + choices);
    }

    public static void main(String[]args){
        int[] testSet1 = {0, 1, 3, 7, 9, 10, 15, 17, 18, 19, 22, 25, 27};
        Teacups teacup1 = new Teacups(12, 24, testSet1);
//        recursion
        System.out.println("TEST 1 *****************");
        System.out.println("Recursive Solution");
        teacup1.printChoices(12, "", 12, 0);
//        dynamic programming
        System.out.println("Dynamic Programming");
        teacup1.printTable();
        for(int t = 1; t <= 24; t++){
            teacup1.pickBest(t);
        }


        // test 2
        int[] testSet2 = {0, 2, 5, 8, 9, 10, 15, 19, 23, 24, 29, 30, 32};
        Teacups teacup2 = new Teacups(12, 24, testSet2);
        System.out.println("TEST 2 **************************");
        System.out.println("Recursive Solution");

        teacup2.printChoices(12, "", 12, 0);

        System.out.println("Dynamic Programming");

        teacup2.printTable();
        for(int t = 1; t <= 24; t++){
            teacup2.pickBest(t);
        }


    }
}
