% función para verificar si el perceptrón ha clasificado correctamente todos
% los patrones de entrada en los datos
function isCorrect = CheckPattern(Data, W)
    isCorrect = true;
    for i = 1:size(Data, 1)
        [Input, Output, Target] = ValoresIOT(Data, W, i);
        if Signo(Output ~= Target) ~= Data(i, end)%% podria haber puesto esto nada mas aqui Output ~= Target
            isCorrect = false;
            break;
        end
    end
end
