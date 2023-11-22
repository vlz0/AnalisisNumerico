%MatJacobiSeid: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método de Jacobi o
%de Gauss Seidel (Matricial), depende del método elegido, se elige 0 o 1 en met
%respectivamente

function [E,s] = MatJacobiSeid(x0,A,b,Tol,niter,met)
    
    % Verificar si A es cuadrada
    [m, n] = size(A);
    if m ~= n
        error('La matriz A no es cuadrada.');
    end

    % Verificar si las dimensiones de b coinciden con A
    if numel(b) ~= n
        error('Las dimensiones del vector b no coinciden con la matriz A.');
    end
    
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);
    while error>Tol && c<niter
        if met==0
            T=inv(D)*(L+U);
            C=inv(D)*b;
            x1=T*x0+C;
        end
        if met==1
            T=inv(D-L)*(U);
            C=inv(D-L)*b;
            x1=T*x0+C;
        end
        E(c+1)=norm(x1-x0,'inf');
        error=E(c+1);
        x0=x1
        c=c+1;
    end
     % Mostrar resultados
    if error < Tol
        s = x0;
        iter = c;
        disp('Tabla de resultados:');
        disp('Iteración      Error');
        disp([1:c; error_history(1:c)]);
        fprintf('La solución es: %s\n', mat2str(s));
        fprintf('Se alcanzó una aproximación con una tolerancia de %f en %d iteraciones.\n', Tol, iter);
    else
        s = x0;
        iter = c;
        fprintf('Fracasó en %d iteraciones.\n', niter);
    end
end