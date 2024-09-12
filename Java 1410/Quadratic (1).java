import java.util.Scanner;

public class Quadratic {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a, b, c: ");
        double aNumber = scan.nextDouble();
        double bNumber = scan.nextDouble();
        double cNumber = scan.nextDouble();

        //computations
        double discriminant = Math.pow(bNumber, 2) - (4*aNumber*cNumber);
        double rootOne = (-bNumber + Math.sqrt(discriminant)) / (2 * aNumber);
        double rootTwo = (-bNumber - Math.sqrt(discriminant)) / (2 * aNumber);

        //output
        if (discriminant > 0 ) {
            System.out.println("There are two roots for the quadratic equation with these coefficients.");
            System.out.println("r1 = " + rootOne);
            System.out.println("r2 = " + rootTwo);
        }else if (discriminant == 0) {
            System.out.println("There is one root for the quadratic equation with these coefficients.");
            System.out.println("r1 = " + rootOne);
        }else{
            System.out.println("There are no roots for the quadratic equation with these coefficients.");
        }

    }
}