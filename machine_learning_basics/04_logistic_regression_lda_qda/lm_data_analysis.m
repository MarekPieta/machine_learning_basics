%
%   TOPIC: Data analysis
%
% ------------------------------------------------------------------------

close all
clearvars

smarket = readtable('data/smarket.csv');
smarket.Direction = categorical(smarket.Direction, {'Up','Down'});
summary(smarket)

smarket_cor_tbl = smarket(:, 1:8);

% smarket_cor_tbl - tabela zawieraj�ca "okrojone" dane (bez cechy `Direction`)
% Cor, p_val - macierze zawieraj�ce odpowiednio wsp�czynniki korelacji i p-warto�ci

[Cor pvals] = corrcoef(table2array(smarket_cor_tbl));
Cor = array2table(Cor);
Cor.Properties.VariableNames = smarket_cor_tbl.Properties.VariableNames;
Cor.Properties.RowNames = smarket_cor_tbl.Properties.VariableNames;
pvals = array2table(pvals);
pvals.Properties.VariableNames = smarket_cor_tbl.Properties.VariableNames;
pvals.Properties.RowNames = smarket_cor_tbl.Properties.VariableNames;
Cor
pvals