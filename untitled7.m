clear; clc; close all;

D=4e-11; %확산계수
L=2.5e-4; % 전체 길이
Cs=0.2; % 표면농도
C0=0.1; %초기농도
dx=5.e-6;
dt=3e-1;
kk=D*dt/dx^2;
tm=100; % 최대 타임스텝
totalL=[0:dx:L];
xm=numel(totalL)
C=zeros(xm,tm);

% initial condition
for i=1:xm
    C(i,1)=C0;
end
C(1,1)=Cs;
%-------------------------------

%calculation
for t=1:tm
   % boundarary condition
   C(1,t)=Cs;
   C(xm,t)=C0;
    for x=2:xm-1
        C0=C(x,t);
        C1=C(x+1,t);
        C2=C(x-1,t);
        dc_dx=C1-2*C0+C2;
        C(x,t+1)=kk*dc_dx+C0;
   end 

end

plot(totalL,C(:,100),'k');