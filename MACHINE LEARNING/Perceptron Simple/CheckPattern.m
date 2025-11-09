% Comprueba si todos los patrones del conjunto están correctamente clasificados
function isCorrect = CheckPattern(Data, W)
    isCorrect = true;
    for i = 1:size(Data, 1)
        [Input, Output, Target] = ValoresIOT(Data, W, i);% Obtiene entrada, salida y etiqueta real
        if Signo(Output ~= Target) ~= Data(i, end)%% podria haber puesto esto nada mas aqui Output ~= Target
            isCorrect = false;
            break;
        end
    end
end
