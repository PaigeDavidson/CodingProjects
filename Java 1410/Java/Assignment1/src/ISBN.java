import java.util.Scanner;

public class ISBN {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first 9 digits of an ISBN: ");
        int wholeNumber = input.nextInt();

        //get individual numbers
        int firstDigit = wholeNumber / 100000000;
        int secondDigit = (wholeNumber / 10000000) % 10;
        int thirdDigit = (wholeNumber / 1000000) % 10;
        int fourthDigit = (wholeNumber / 100000) % 10;
        int fifthDigit = (wholeNumber / 10000) % 10;
        int sixthDigit = (wholeNumber / 1000) % 10;
        int seventhDigit = (wholeNumber / 100) % 10;
        int eighthDigit = (wholeNumber / 10) % 10;
        int ninthDigit = (wholeNumber) % 10;

        //checksum calculation
        int checksum = (firstDigit + secondDigit * 2 + thirdDigit * 3 + fourthDigit * 4 + fifthDigit * 5 +
                sixthDigit * 6 + seventhDigit * 7 + eighthDigit * 8 + ninthDigit * 9) % 11;

        if (checksum == 10) {
            System.out.println("The ISBN-10 number is: " + firstDigit + secondDigit + thirdDigit + fourthDigit + fifthDigit +
                    sixthDigit + seventhDigit + eighthDigit + ninthDigit + "X");
        }else{
            System.out.println("The ISBN-10 number is: " + firstDigit+secondDigit+thirdDigit+fourthDigit+fifthDigit+
                    sixthDigit+seventhDigit+eighthDigit+ninthDigit+checksum);
        }

        }
    }