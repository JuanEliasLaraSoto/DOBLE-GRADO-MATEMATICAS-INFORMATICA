% función para actualizar los pesos del perceptrón cuando la predicción Output
% no coincide con la etiqueta real Target
function W = UpdateNet(W, LR, Output, Target, Input)
    diffW = LR * (Target - Output) * [Input -1];
    W = W + diffW';
end
