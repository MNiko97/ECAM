clc;
% Load Matrix
A = dlmread('etape1OK.cubes');
B = dlmread('etape2OK.cubes');
C = dlmread('etape3OK.cubes');

% Find Complement Functions 
A_N = complement(A,5)
B_N = complement(B,4)
C_N = complement(C,6)