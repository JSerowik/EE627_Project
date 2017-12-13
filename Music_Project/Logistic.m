function Y = Logistic(X, md)
    sz = size(X);
    for i = 1:sz(1)
        Y(i,:) = 1 / (1 + exp(-0.1*(X(i,:)-md)));
        %Y(i,:) = log(X(i,:)/(X(i,:)-1));
    end
end