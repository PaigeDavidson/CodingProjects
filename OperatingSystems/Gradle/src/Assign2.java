import java.lang.Runtime;

public class Assign2 {
    public static void main(String[] args) {
        //If no arguments, do nothing
        if(args.length == 0){
            ;
        }
        // loop through arguments and call function depending on command line arguments 
        for(int i = 0; i < args.length; i++){
            if(args[i].equals("-cpu")){
                System.out.println("Processors   : " + Runtime.getRuntime().availableProcessors());

            }else if(args[i].equals("-mem")){
                System.out.println("Free Memory   :     " + Runtime.getRuntime().freeMemory());
                System.out.println("Total Memory  :     " + Runtime.getRuntime().totalMemory());
                System.out.println("Max Memory    :     " + Runtime.getRuntime().maxMemory());

            }else if(args[i].equals("-dirs")){
                System.out.println("Working Directory   : " + System.getProperty("user.dir"));
                System.out.println("User Home Directory : " + System.getProperty("user.home"));

            }else if(args[i].equals("-os")){
                System.out.println("OS Name             : " + System.getProperty("os.name"));
                System.out.println("OS Version          : " + System.getProperty("os.version"));

            }else if(args[i].equals("-java")){
                System.out.println("Java Vendor         : " + System.getProperty("java.vendor"));
                System.out.println("Java Runtime        : " + System.getProperty("java.runtime.name"));
                System.out.println("Java Version        : " + System.getProperty("java.version"));
                System.out.println("Java VM Version     : " + System.getProperty("java.vm.version"));
                System.out.println("Java VM Name        : " + System.getProperty("java.vm.name"));

            }else{
                // For invalid arguments, do nothing
                ;
            }
            
        }
    }
}

//to compile: gradle build or gradle run

// user@Users-MacBook-Pro-2 Assign2 % gradle -q run -PrunArgs="-cpu"
// Processors   : 8


// user@Users-MacBook-Pro-2 Assign2 % gradle -q run -PrunArgs="-mem"
// Free Memory   :     134204768
// Total Memory  :     136314880
// Max Memory    :     2147483648


// user@Users-MacBook-Pro-2 Assign2 % gradle -q run -PrunArgs="-dirs"
// Working Directory   : /Users/user/OperatingSystems/Assign2
// User Home Directory : /Users/user


// user@Users-MacBook-Pro-2 Assign2 % gradle -q run -PrunArgs="-os"
// OS Name             : Mac OS X
// OS Version          : 12.6.9


// user@Users-MacBook-Pro-2 Assign2 % gradle -q run -PrunArgs="-java"
// Java Vendor         : Homebrew
// Java Runtime        : OpenJDK Runtime Environment
// Java Version        : 21.0.2
// Java VM Version     : 21.0.2
// Java VM Name        : OpenJDK 64-Bit Server VM
