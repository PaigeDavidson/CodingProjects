import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.math.RoundingMode;

public class Assign1{

    public static Integer fibonacci(int num){
        if(num == 0){
            return 1;
        } else if(num == 1){
            return 1;
        }else{
            return fibonacci(num - 1) + fibonacci(num - 2);
        }

    }
    public static BigInteger factorial(int num){
        if(num == 0){
            return BigInteger.ONE;
        }
        BigInteger n = BigInteger.valueOf(num);
        if(n.equals(BigInteger.ONE)){
            return BigInteger.ONE;
        }else{
            return n.multiply(factorial(num - 1));
        }
    }
    public static BigDecimal eValue(int iterations){
        BigDecimal e = BigDecimal.ONE;
        BigDecimal term = BigDecimal.ONE;

        for(int i = 1; i <= iterations; i++){
            term = term.divide(BigDecimal.valueOf(i), MathContext.DECIMAL128);
            e = e.add(term);
        }
        return e.setScale(16, RoundingMode.HALF_UP);

    }
    public static boolean isInteger(String s) {
        try {
            Integer.parseInt(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    public static void main(String[] args) {
        // Check if there are command line arguments and that each argument has an associated integer input
        if (args.length > 0 && args.length % 2 == 0) {
            for (int i = 0; i < args.length; i+=2) {  
                String strInput = args[i+1];
                //check is input is an integer
                if(isInteger(strInput)){
                    int input = Integer.valueOf(args[i+1]);
                    //preform fibbonacci calculation
                    if(args[i].equals("-fib")){
                        //if input is in the correct range
                        if(0 <= input  && input <= 40){
                            int answer = fibonacci(input);
                            System.out.println("Fibonacci of " + input + " is " + answer);

                        }else{
                            System.out.println("Fibonacci valid range is [0, 40]");
                        }

                    }
                    else if(args[i].equals("-fac")){
                        if(0 <= input && input <= 2147483647){
                            BigInteger answer = factorial(input);
                            System.out.println("Factorial of " + input + " is " + answer);
                        }else{
                            System.out.println("Factorial valid range is [0, 2147483647]");
                        }
                    }
                    else if(args[i].equals("-e")){
                        if(1 <= input && input <= 2147483647){
                            BigDecimal answer = eValue(input);
                            System.out.println("Value of e using " + input + " iterations is " + answer);
                        }else{
                            System.out.println("Valid e iterations range is [1, 2147483647]");
                        }

                    }else{
                        System.out.println("Unknown command line argument: " + args[i]);
                    }
                }else {
                    System.out.println("Invalid input for argument " + args[i] + ": " + strInput + " is not a valid integer.");
                }
            }
        } else {
            // In the case of no or invalid number of parameters show help instructions
            System.out.println("--- Assign 1 Help ---");
            System.out.println("  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]");
            System.out.println("  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]");
            System.out.println(" -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]");
        }
        
    }
}