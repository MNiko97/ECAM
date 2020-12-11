clc;
clear all;
wd = 'C:/Users/Niko/OneDrive - ECAM/ECAM/BA3/Q1/E3010 Microcontroller and Logic Design 6ECTS/Logic Minimizer Project/';

% Load simple matrix
A = dlmread(strcat(wd,'Etape/etape1OK.cubes'));
B = dlmread(strcat(wd,'Etape/etape2OK.cubes'));
C = dlmread(strcat(wd,'Etape/etape3OK.cubes'));
D = dlmread(strcat(wd,'Etape/etape4bif.cubes'));
E = dlmread(strcat(wd,'Etape/etape4mono.cubes'));
F = dlmread(strcat(wd,'Etape/etape5.cubes'));
G = dlmread(strcat(wd,'Etape/etape6.cubes'));
    
% Find Complement Functions 
A_N = Complement(A,5);
B_N = Complement(B,4);
C_N = Complement(C,6);
D_N = Complement(D,3);
E_N = Complement(E,3);
F_N = Complement(F,3);
G_N = Complement(G,3);

% Load more complex matrix
A1 = dlmread(strcat(wd,'fonction/function1.cubes'));
A1_comp = dlmread(strcat(wd,'fonction/function1comp.cubes'));
A1_N = Complement(A1, 6);

A2 = dlmread(strcat(wd,'fonction/function2.cubes'));
A2_comp = dlmread(strcat(wd,'fonction/function2comp.cubes'));
A2_N = Complement(A2, 6);

A3 = dlmread(strcat(wd,'fonction/function3.cubes'));
A3_comp = dlmread(strcat(wd,'fonction/function3comp.cubes'));
A3_N = Complement(A3, 6);

A4 = dlmread(strcat(wd,'fonction/function4.cubes'));
A4_comp = dlmread(strcat(wd,'fonction/function4comp.cubes'));
A4_N = Complement(A4, 6);

test1 = IsSameFunction(A1_N,A1_comp,6)
test2 = IsSameFunction(A2_N,A2_comp,6)
test3 = IsSameFunction(A3_N,A3_comp,6)
test4 = IsSameFunction(A4_N,A4_comp,6)