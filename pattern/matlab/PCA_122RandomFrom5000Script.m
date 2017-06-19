mixdata = importdata('testOutput.txt');
[coeff_mix,score_mix,latent_mix] = pca(mixdata,'NumComponents',2);
% figure(4);
% plot(score_mix,'.');

first_half = mixdata(1:100,:);
second_half = mixdata(124:223,:);

% diff = corr2(first_half,second_half);
minus_value = minus(first_half,second_half);
figure(1);
HeatMap(minus_value);
figure(2);
HeatMap(first_half);
figure(3);
HeatMap(second_half);