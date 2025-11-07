function [difW, difT] = retropropagacionError(patron, Z, y, w, s, h, u, Beta, eta)
%% Función que calcula los diferenciales de los pesos W y T

nSalidas = size(y,1);
nOcultas = size(w,2);

delta2 = zeros(nSalidas, 1);
difW = zeros(nSalidas, nOcultas);
delta1 = zeros(nOcultas, 1);
difT = zeros(nOcultas, size(patron, 2));

err = (Z - y);
g1d = derivadaLogistica(h, Beta);
g2d = derivadaLogistica(u, Beta);

initDerivative = eta .* err .* g1d;
derivativeHL = (w' .* g2d);

difW = initDerivative * s';
difT = initDerivative * derivativeHL * patron;
end

