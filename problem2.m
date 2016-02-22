
% Problem 2

p=0.7;
u1 = 2*rand(10000,1)-1;
u2 = 2*rand(10000,1)-1;
sample = zeros(10000,2);

for i=1:10000
    if nthroot( abs(u1(i))^p + abs(u2(i))^p , p ) <= 1
        sample(i,1) = u1(i);
        sample(i,2) = u2(i);
    end
end

plot(sample(:,1),sample(:,2),'.b');