clc; clear; close all;

A=rand(3,3);
B=rand(3,3);

for i=1:3
for j=1:3
    C(i,j)=0;
    for k=1:3
        C(i,j)=C(i,j)+A(i,k)*B(k,j);


    end
end
end

C
A*B