train=load('Train_data');
test=load('Test_Data');
%data_train=load('Train_data.mat');
%data_test=load('Test_Data.mat');


T1= struct2table(train);
T2= struct2table(test);


writetable(T1,'D:\Amar_97\statistics_HW1\traindata.csv');
writetable(T2,'D:\Amar_97\statistics_HW1\testdata.csv');
