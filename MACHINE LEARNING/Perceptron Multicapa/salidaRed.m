function [y, h, s, u] = salidaRed(patron, t, w, Beta)
%% Función que calcula la salida de la red (y), los pesos (h, s) y la salida de la capa oculta (s)

%% ->> Completar aquí <<-
%% ...
 u = t * patron';
 s = logistica(u, Beta);
 h = w * s;
 y = logistica(h, Beta);
end

