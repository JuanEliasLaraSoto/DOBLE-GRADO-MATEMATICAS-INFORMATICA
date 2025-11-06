% función que extrae los valores de entrada, salida predicha y la etiqueta
% objetivo (Target) de un patrón específico del conjunto de datos, basándose en
% los pesos actuales del perceptrón
function [Input, Output, Target] = ValoresIOT(Data, W, i)
    Input = Data(i, 1:end-1);
    Target = Data(i, end);
    Output = Signo(Input * W(1:end-1) - W(end));%w(end) es tita
end
