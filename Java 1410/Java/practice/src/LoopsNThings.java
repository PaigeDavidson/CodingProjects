import java.util.Scanner;

public class LoopsNThings {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        boolean done = false;
        double sum = 0;

        do{
            System.out.println("enter a value to add 'end' to quit:");
            String userInput = input.next();
            if (!userInput.equalsIgnoreCase("end")){
                sum += Double.parseDouble(userInput);
            }else{
                done = true;
            }
        }while (done);
    }
}