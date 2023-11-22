function [polinomio] = Vandermonde(x, y)
    % Construir la matriz de Vandermonde
    n = length(x);
    A = fliplr(vander(x));

    % Resolver el sistema de ecuaciones lineales
    a = A \ y;

    % Polinomio resultante
    polinomio = flip(a');

    % Graficar el polinomio interpolante
    xpol = linspace(min(x), max(x), 1000);
    p = polyval(polinomio, xpol);

    figure;
    plot(x, y, 'r*', xpol, p, 'b-');
    title('Polinomio de Interpolación de Vandermonde');
    xlabel('x');
    ylabel('y');
    legend('Datos', 'Polinomio Interpolante');
    grid on;
end