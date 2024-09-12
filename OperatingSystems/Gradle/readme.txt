Introduction
The purpose of this assignment is to help you get familiarized with the Gradle build tool while also learning how to discover information about the system, OS, and JVM platform.  Gradle is a powerful tool, however we will only be using a tiny bit of its capability.

Assignment
Write a program that accepts command line arguments which direct the program to report various pieces of information about the system, OS, and JVM platform.  Additionally, create a Gradle build file which can be used to build and run the program.

Command Line Arguments
-cpu : Reports the number of CPUs (physical and logical) available.
-mem : Reports the available free memory, total memory, and max memory.
-dirs : Reports the process working directory and the user's home directory.
-os : Reports the OS name and OS version.
-java : Reports the following items about the JVM
Java vendor
Java runtime name
Java version
Java VM version
Java VM name
Other notes

For invalid arguments, do nothing.
If no arguments, do nothing.
If multiple command line arguments are given, the program should process all of them.
Create a build.gradle file that contains instructions on how to build and run the program.  When correctly completed, a user should be able to type gradle build to compile the program or gradle run to compile (if needed) and run the program.  The grader will use your Gradle build file to build and execute your program;  be sure to verify code correctly builds.

Example Execution
The following show examples of running the program on my Raspberry Pi.

gradle -q run -PrunArgs="-cpu"

Processors   : 4
gradle -q run -PrunArgs="-mem"

Free Memory  :     15,449,856
Total Memory :     16,252,928
Max Memory   :    235,274,240
gradle -q run -PrunArgs="-dirs"

Working Directory   : /home/deanmathias/Assign2
User Home Directory : /home/deanmathias
gradle -q run -PrunArgs="-os"

OS Name             : Linux
OS Version          : 4.14.79-v7+
gradle -q run -PrunArgs="-java"

Java Vendor         : Oracle Corporation
Java Runtime        : Java(TM) SE Runtime Environment
Java Version        : 1.8.0_65
Java VM Version     : 25.65-b01
Java VM Name        : Java HotSpot(TM) Client VM