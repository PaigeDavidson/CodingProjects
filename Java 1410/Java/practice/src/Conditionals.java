import java.util.Scanner;

public class Conditionals {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a day number of the week (1 - 7: ");
        int dayNumber = input.nextInt();
        String dayString = "";
        String dayType = "";

        switch (dayNumber) {
            case 1:
                dayString = "Monday";
                break;
            case 2:
                dayString = "Tuesday";
                break;
            case 3:
                dayString = "Wednesday";
                break;
            case 4:
                dayString = "Thursday";
        }
        System.out.print("the day of the week is" + dayString);
    }
}