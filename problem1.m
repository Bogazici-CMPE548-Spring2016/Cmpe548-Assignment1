
% Problem 1

syms x;
syms y;
u = rand(1000,1);
m = rand(1000,1);

theta = 2 * pi ;
cdf_theta(x) = x / theta;
inverse_theta = finverse(cdf_theta);
ranT = double(inverse_theta(u));

cdf_rho(y) = y ^ 2;
inverse_rho = finverse(cdf_rho);
ranR = double(inverse_rho(m));

varT = linspace(0, 2 * pi);
varX = cos(varT);
varY = sin(varT);

sampleX = cos(ranT) .* ranR;
sampleY = sin(ranT) .* ranR;

figure
plot(varX, varY, '-r', sampleX,sampleY,'.b');

