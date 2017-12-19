% Import tested solutions
S1 = importdata('DataMatrix/result08377.txt');
S2 = importdata('DataMatrix/result08255.txt');
S3 = importdata('DataMatrix/result08019.txt');
S4 = importdata('DataMatrix/result07615.txt');
S5 = importdata('DataMatrix/result06942.txt');
S6 = importdata('DataMatrix/result06927.txt');
S7 = importdata('DataMatrix/result05499.txt');
S8 = importdata('DataMatrix/result05483.txt');
S9 = importdata('DataMatrix/result05011.txt');
S10 = importdata('DataMatrix/result05003.txt');
S11 = importdata('DataMatrix/result04947.txt');
S = [S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11];
% Convert each element by 2*x - 1
t1 = convT(S1);
t2 = convT(S2);
t3 = convT(S3);
t4 = convT(S4);
t5 = convT(S5);
t6 = convT(S6);
t7 = convT(S7);
t8 = convT(S8);
t9 = convT(S9);
t10 = convT(S10);
t11 = convT(S11);
T = [t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 t11];
% (T^T)*T
temp = (T.')*T;
% Input error rates returned from submission website
err1 = (2*0.8377) - 1;
err2 = (2*0.8255) - 1;
err3 = (2*1.8019) - 1;
err4 = (2*0.7615) - 1;
err5 = (2*0.6942) - 1;
err6 = (2*0.6927) - 1;
err7 = (2*1.5499) - 1;
err8 = (2*0.5483) - 1;
err9 = (2*0.5011) - 1;
err10 = (2*0.5003) - 1;
err11 = (2*0.4947) - 1;
errT = [err1; err2; err3; err4; err5; err6; err7; err8; err9; err10; err11];
% ER = M*[2*correct rate - 1]
ER = size(T, 1).*errT;
% a = (T^T * T) T^T *tsol
a = temp*ER;
% S = S*a
Sopt = S*a;
md = mean(Sopt);
St = Logistic(Sopt, md);
Sout = correct(St);
fileID = fopen('DataMatrix/out1.txt','w');
nbytes = fprintf(fileID,'%d\n',Sout);
fclose(fileID);