clc;
clear;
close all;
%%%
%parameters
%change parameter p here!
n = 1000;
p1 = 0.03;
p2 = 0.3;
%%%
head_counter1 = 0;
probabiliy_array1 = zeros(2,n);
probabiliy_array1(1,:) = 1:n;

head_counter2 = 0;
probabiliy_array2 = zeros(2,n);
probabiliy_array2(1,:) = 1:n;

for i = 1:n
    if rand() <= p1
        head_counter1 = head_counter1 + 1;
    end
    probabiliy_array1(2,i) = head_counter1/i;
    if rand() <= p2
        head_counter2 = head_counter2 + 1;
    end
    probabiliy_array2(2,i) = head_counter2/i;
end
%%%plot for p = 0.03
x = probabiliy_array1(1,:);
y = ones(1,n)*p1;
plot(x,y,'--');
hold on;
plot(probabiliy_array1(1,:)',probabiliy_array1(2,:)');
ylim([0 1]);
title('probability of head for p = 0.03');
xlabel('# of fliping a coin');
ylabel('probability');
hold off;
%%%
figure();
%%%plot for p = 0.3
x = probabiliy_array2(1,:);
y = ones(1,n)*p2;
plot(x,y,'--');
hold on;
plot(probabiliy_array2(1,:)',probabiliy_array2(2,:)');
ylim([0 1]);
title('probability of head for p = 0.3');
xlabel('# of fliping a coin');
ylabel('probability');
hold off;