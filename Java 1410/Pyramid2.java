import java.util.Scanner;

public class Pyramid2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of lines: ");
        int numLines = input.nextInt();
        String pyramid = "";

        getPyramid(numLines, pyramid);


    }
    private static void getPyramid(int numLines, String pyramid){
        //get width of the biggest number
        double bigNumber = Math.pow(2,(numLines -1));
        //get width of the biggest number for spacing
        String big = " " + bigNumber;
        int numDigits = big.length();
        String format = String.format("%%%dd", numDigits - 2);

        String strInput = "" + numLines;
        int spacePerNum = strInput.length();

        int rowNumber = 1;
        for(int n = 1; n <= numLines; n++){
            //adds spaces so it makes a pyramid
            String beginningSpaces = addSpaces(bigNumber, n, numLines);
            System.out.print("" + beginningSpaces);
            // doubles up to the row number
            for(int i = 1; i < rowNumber; i *= 2){
                System.out.printf(format, i);
            }
            //goes back down to one
            for(int i = rowNumber; i >= 1; i /= 2){
                System.out.printf(format, i);
            }
            System.out.println();
            rowNumber *= 2;
        }

    }


    private static String addSpaces(double bigNumber, int n, int numLines){
        String input = "" + bigNumber;
        int spacePerNum = input.length() - 2;
        int numSpaces = ((numLines - n) * (spacePerNum + 1));
        String spaces = "";
        for(int k=0; k < numSpaces; k++){
            spaces += " ";
        }
        return spaces;
    }
}