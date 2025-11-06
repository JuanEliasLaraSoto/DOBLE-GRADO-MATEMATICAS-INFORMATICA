% función para inicializar los pesos
function W = PerceptronWeigthsGenerator(Data)
    NInp = size(Data, 2);          % número de columnas
    W = rand(NInp, 1) - 0.5;       % genera valores entre -0.5 y 0.5
end
