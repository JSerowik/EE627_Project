function Y = Logistic(X)
    sz = size(X);
    for i = 1:sz(1)
        Y(i,:) = 1 / (1 + exp(-X(i,:)));
        %Y(i,:) = log(X(i,:)/(X(i,:)-1));
    end
end