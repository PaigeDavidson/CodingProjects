# store integers in variables
li $t0, 20
li $t1, 7

# preform addition or subtraction and store result in t0
sub $t0, $t1, $t0

# print
# move output from t0 to a0
add $a0, $t0, $zero
# store a 1 in the vo register (op code for printing integer)
li $v0, 1
# call syscall
syscall