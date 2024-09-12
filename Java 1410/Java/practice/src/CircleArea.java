import java.util.Scanner;

public class CircleArea {
    public static void main(String[] args) {

        Scanner input  = new Scanner(System.in);
        System.out.println("enter a radius: ");
        double radius = input.nextDouble();
        double area = radius * radius * Math.PI;

        System.out.println("the area for the circle of radius " + radius + " is " + area);
    }
}