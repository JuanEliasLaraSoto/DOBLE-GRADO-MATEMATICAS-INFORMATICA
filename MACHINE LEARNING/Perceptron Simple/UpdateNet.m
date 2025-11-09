   % Actualiza los pesos sinápticos del perceptrón
function W = UpdateNet(W, LR, Output, Target, Input)
    diffW = LR * (Target - Output) * [Input -1];% Cálculo del cambio en los pesos (incluye umbral)
    W = W + diffW';% Actualización del vector de pesos
end
