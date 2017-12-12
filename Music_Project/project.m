% Import tested solutions
S1 = importdata('DataMatrix/recOutput.txt');
S2 = importdata('DataMatrix/randFirstHalf.txt');
S3 = importdata('DataMatrix/randSecondHalf.txt');
S4 = importdata('DataMatrix/randAll.txt');
S5 = importdata('DataMatrix/randAll2.txt');
S6 = importdata('DataMatrix/T_rand.txt');
S7 = importdata('DataMatrix/ens.txt');
S = [S1 S2 S3 S4 S5 S6 S7];
% Convert each element by 2*x - 1
t1 = convT(S1);
t2 = convT(S2);
t3 = convT(S3);
t4 = convT(S4);
t5 = convT(S5);
t6 = convT(S6);
t7 = convT(S7);
T = [t1 t2 t3 t4 t5 t6 t7];
% (T^T)*T
temp = (T.')*T;
% Input error rates returned from submission website
err1 = (2*0.8377) - 1;
err2 = (2*0.6942) - 1;
err3 = (2*0.6927) - 1;
err4 = (2*0.5483) - 1;
err5 = (2*0.5499) - 1;
err6 = (2*0.5011) - 1;
err7 = (2*0.8019) - 1;
errT = [err1; err2; err3; err4; err5; err6; err7];
% ER = M*[2*correct rate - 1]
ER = size(T, 1).*errT;
% a = (T^T * T) T^T *tsol
a = temp*ER;
% S = S*a
Sopt = S*a;
Sout = Logistic(Sopt);

fileID = fopen('myfile.txt','w');
nbytes = fprintf(fileID,'%5d \n',Sout);
fclose(fileID);