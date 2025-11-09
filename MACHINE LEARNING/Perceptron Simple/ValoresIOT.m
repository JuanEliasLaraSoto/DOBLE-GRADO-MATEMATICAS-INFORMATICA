% Extrae el patrón i del conjunto de datos y calcula su salida
function [Input, Output, Target] = ValoresIOT(Data, W, i)
    Input = Data(i, 1:end-1);  % Vector de entrada (todas las columnas menos la última)
    Target = Data(i, end);% Salida deseada del patrón (última columna)
    Output = Signo(Input * W(1:end-1) - W(end));% Salida predicha por el perceptrón (w(end) = umbral o tita)
end
