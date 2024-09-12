.data
    n: 10
    result: 0
    stack_pointer: 500

.text
main:
    # Load n and initialize result to 0
    lw R1, n
    add R2, R0, R0  # Initialize result to 0
    
    # Call the function
    jal sum_natural_numbers
    
    # Store the result
    sw R2, result

    # End program
    j end

sum_natural_numbers:
    # Base Case: If n == 0, return 0
    beq R1, R0, base_case
    
    # Save return address on the stack
    addi R6, R6, -1
    sw R7, 0(R6)
    
    # Recursive Case: Add n to the result and call sum_natural_numbers(n-1)
    add R2, R2, R1
    addi R1, R1, -1
    j sum_natural_numbers
    
    # Restore return address from the stack
base_case:
    lw R7, 0(R6)
    addi R6, R6, 1
    
    jr R7

end:
    # End program
