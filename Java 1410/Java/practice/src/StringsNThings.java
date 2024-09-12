import java.util.*;

public class StringsNThings {
    public static void main(String[] args) {

        //demo some random numbers
        int howMany = 10;
        while(howMany-- > 0){
            double result = Math.random();
            System.out.println(result);
            int card = 1 + (int)(result * 52);
            System.out.println(card);
        }
        //letters
        char letter = (char)65;
        System.out.println("the character for 65 is: " + letter);
        letter++;
        System.out.println("the next character is: " + letter);

        int letterValue = (int)'A';
        System.out.println("the numeric value for 'A' is: " + letterValue);

        //adding to a string
        String message = "this is an example string";
        System.out.println(message);
        message = message + ", that I just added some more stuff to.";
        System.out.println(message);

        //special characters
        String quotes = "This is a \"quote\"";
        System.out.println(quotes);

        // strings
        Scanner input = new Scanner(System.in);
        System.out.println("enter a string: ");
        String s1 = input.nextLine();

        System.out.println("enter another string: ");
        String s2 = input.nextLine();

        if (s1.equals(s2)){
            System.out.println("the strings are equivalent");
        }else {
            System.out.println("The strings are not equivalent ");
        }

//        //parse a string
//        Scanner input = new Scanner(System.in);
//        System.out.println("enter a number: ");
//        String userInput = input.next();
//        int value = Integer.parseInt(userInput);
//        System.out.println(value);


//        Scanner input = new Scanner(System.in);
//        System.out.println("enter the field width: ");
//        int width = input.nextInt();
//
//        String Format1 = "formatting value1: %+" + width + "d\n";
//
//
//        int value1 = 1234;
//        double value2 = 123.456;
//        int negativeValue = -1234;
//
//        System.out.printf(Format1, value1);
//        System.out.printf("formatting 'value1': %6d\n", value1);
//        System.out.printf("formatting 'value2': %4.2f\n", value2);
//        System.out.printf("formatting 'negativeValue': %+d\n", negativeValue);



    }
}