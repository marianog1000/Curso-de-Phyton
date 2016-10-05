# Left Bit Shift (<<)  
#0b000001 << 2 == 0b000100 (1 << 2 = 4)
#0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
#0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
#0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 


shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)
