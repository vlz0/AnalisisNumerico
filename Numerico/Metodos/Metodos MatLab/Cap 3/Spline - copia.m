function [coefs] = Spline(x, y, degree)
    n = length(x);
    
    % Inicializar matrices
    A = zeros((degree + 1) * (n - 1));
    b = zeros((degree + 1) * (n - 1), 1);
    
    % Calcular potencias de x hasta el grado deseado
    powers = zeros(degree + 1, n);
    for i = 1:(degree + 1)
        powers(i, :) = x.^(degree + 1 - i);
    end
    
    % Construir sistema de ecuaciones
    c = 1;
    h = 1;
    for i = 1:(n - 1)
        A(h:(h + degree), c:(c + degree + 1)) = powers(:, i:(i + degree + 1))';
        b(h:(h + degree)) = y(i:(i + degree + 1));
        c = c + degree + 1;
        h = h + degree + 1;
    end
    
    % Resolver el sistema de ecuaciones
    coefs = A \ b;
    
    % Graficar el spline interpolante
    x_interp = linspace(min(x), max(x), 1000);
    y_interp = zeros(1, length(x_interp));
    
    for i = 1:(n - 1)
        idx = (i - 1) * (degree + 1) + 1:i * (degree + 1);
        y_interp((x_interp >= x(i)) & (x_interp <= x(i + 1))) = polyval(coefs(idx), x_interp((x_interp >= x(i)) & (x_interp <= x(i + 1))));
    end
    
    figure;
    plot(x, y, 'ro', x_interp, y_interp, 'b-');
    title('Spline Interpolante');
    xlabel('x');
    ylabel('y');
    legend('Datos', 'Spline Interpolante');
    grid on;
end
