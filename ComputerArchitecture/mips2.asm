.data
	intVar: .word 56
	otherVar: .word 127
	otherOtherVar: .word 48
	array: .word 5, 10, 20, 25, 30
	msg: .asciiz
	myvar: .space 4 # reserves 4 bites of memory in space
	
.text
	lw $t0, ($zero)
	lw $t1, 4($zero)
	
	li $t2, 8
	lw $t3, ($t2)
	
	#or do lw $t0, intVar
	
	#La (load adress)
	la $t0, otherOtherVar