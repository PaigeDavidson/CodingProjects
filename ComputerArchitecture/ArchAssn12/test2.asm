.data
n: 10
result: 0
stack_pointer: 500

.text
main:
    # Load any arguments into registers
    lw R1, n # Load n into R1
    
    # Call the function
    jal sum_natural_numbers
    
    # Store the result in the result variable
    add R2, R0, R2   # Store the result in R2 (result)
    sw R2, result
    
    # Jump to the end of the program
    j end
    
sum_natural_numbers:
    # Base Case
    beq R1, R0, basecase   # Check if n == 0
    j recursivecase
    
    basecase:
        addi R2, R0, 0   # Set R2 to 0 (base case)
        jr R7

    # Recursive Case
    recursivecase:
        addi R6, R6, -8   # Allocate space on the stack
        sw R7, 0(R6)   # Save return address
        sw R1, 4(R6)   # Save n on the stack
        
        addi R1, R1, -1   # Decrement n by 1
        jal sum_natural_numbers   # Recursive call
        
        lw R1, 4(R6)   # Restore n from the stack
        lw R7, 0(R6)   # Restore return address from the stack
        addi R6, R6, 8   # Deallocate space on the stack
        
        add R2, R2, R1   # Add n to the result
        jr R7   # Return to the caller
    
end:
