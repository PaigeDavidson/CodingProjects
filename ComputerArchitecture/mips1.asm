#addi $t0, $zero, 12
# fibbonacci sequence
#addi $t0, $zero, 0
#addi $t1, $zero, 1
#add $t2, $t1, $t0
#add $t3, $t2, $t1

#practice problem (5-3)+ (10-5)
# store final result in $t7

#store first 4 values in registers
addi $t0, $zero, 5
addi $t1, $zero, 3
addi $t2, $zero, 10
#addi $t3, $zero, 5
#preform subtractions
sub $t1, $t0, $t1
sub $t0, $t2, $t0
# add numbers together
add $t7, $t4, $t5
