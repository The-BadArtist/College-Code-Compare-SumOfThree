PROGRAM sumOfThree

! This is a simple program to add three numbers

! Type declarations
real :: x, y, z, sum


! Executable statements
x = 1.0
y = 2.0
z = 3.0
Sum = x + y + z
PRINT (*, '(I0, "+", I0, "+", I0, "=", I0)') x, y, z, Sum

END PROGRAM