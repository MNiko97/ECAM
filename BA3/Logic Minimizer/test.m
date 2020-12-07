clc;
wd = 'C:/Users/Niko/OneDrive - ECAM/ECAM/BA3/Q1/E3010 Microcontroller and Logic Design 6ECTS/Logic Minimizer Project/';

% Load Matrix
A = dlmread(strcat(wd,'Etape/etape1OK.cubes'));
B = dlmread(strcat(wd,'Etape/etape2OK.cubes'));
C = dlmread(strcat(wd,'Etape/etape3OK.cubes'));

    
% Find Complement Functions 
A_N = Complement(A,5)
B_N = Complement(B,4)
C_N = Complement(C,6)