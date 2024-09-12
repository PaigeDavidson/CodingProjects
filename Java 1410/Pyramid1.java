import java.util.Scanner;


public class Pyramid1 {
    public static void main(String[] args) {

        Scanner input = new Scanner((System.in));

        System.out.print("Enter the number of lines: ");
        int numberOfLines = input.nextInt();
        String stringNumOfLines = numberOfLines + "";
        int width = stringNumOfLines.length();
        String pyramid = "";


        pyramid = getPyramid(numberOfLines, pyramid, width);
        System.out.println(pyramid);


    }

    private static String getPyramid(int numberOfLines, String pyramid, int width) {
        String strInput = "" + numberOfLines;
        int spacePerNum = strInput.length();

        for(int n = 1; n <= numberOfLines; n++) {
            String beginningSpaces = addSpaces(numberOfLines, n);
            pyramid += beginningSpaces;
            //counts down form the row number
            for(int i = n; i > 0; i--){
                //gets the number of spaces to put after the number is printed
                String stringDigit = "" + i;
                int digits = stringDigit.length();
                //creates correct number of spaces and adds them to a string
                int spaces = 1 + (spacePerNum - digits);
                String spacing = "";
                for(int j = 0; j < spaces; j++){
                    spacing += " ";
                }
                //adds the new number to the pyramid plus the number of calculated spaces
                pyramid += i + spacing;
            }

            //counts back up the row number
            for(int i = 2; i <= n; i++){
                String string = "" + i;
                int digits = string.length();
                int spaces = 1 + (spacePerNum - digits);
                String spacing = "";
                for(int j = 0; j < spaces; j++){
                    spacing += " ";
                }
                pyramid += i + spacing;
            }
            pyramid += "\n";
        }


            return pyramid;

    }
    private static String addSpaces(int numberOfLines, int n) {
        String input = "" + numberOfLines;
        int spacePerNum = input.length();
        int numSpaces = ((numberOfLines - n) * (spacePerNum + 1));
        String spaces = "";
        for(int k=0; k < numSpaces; k++){
            spaces += " ";
        }
        return spaces;

    }
}