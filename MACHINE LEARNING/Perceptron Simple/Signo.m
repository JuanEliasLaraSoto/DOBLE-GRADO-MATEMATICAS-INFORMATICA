 % Función que implementa la función signo bipolar del perceptrón
function Out=Signo(inp)
Out=sign(inp); % Devuelve 1 si inp>=0, -1 si inp<0
Out(Out==0)=1;% En caso de ser 0, se considera como clase positiva (+1)
