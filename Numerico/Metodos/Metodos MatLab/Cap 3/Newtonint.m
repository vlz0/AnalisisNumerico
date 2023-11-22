%Newtonint: Calcula los coeficienetes del polinomio de interpolación de
% grado n-1 para el conjunto de n datos (x,y), mediante el método de Newton
% con diferencias divididas.
function [Tabla] = Newtonint(x,y)
    n=length(x);
    Tabla=zeros(n,n+1);
    Tabla(:,1)=x;
    Tabla(:,2)=y;
    for j=3:n+1
        for i=j-1:n
            Tabla(i,j)=(Tabla(i,j-1)-Tabla(i-1,j-1))/(Tabla(i,1)-Tabla(i-j+2,1));
        end
    end
    % Crear el polinomio resultante
    polinomio = zeros(1, n);
    for k = 1:n
        polinomio = polinomio + Tabla(k, k + 1) * poly([1, -Tabla(k, 1)]);
    end

    % Graficar el polinomio interpolante
    figure;
    xx = linspace(min(x), max(x), 1000);
    yy = polyval(polinomio, xx);
    plot(x, y, 'o', xx, yy, '-');
    title('Polinomio de Interpolación de Newton');
    xlabel('x');
    ylabel('y');
    legend('Datos', 'Polinomio Interpolante');
    grid on;
end