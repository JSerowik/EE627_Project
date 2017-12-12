function T = convT(X)
    sz = size(X);
    T = zeros(sz);
    for i = 1:sz(1)
        T(i) = (2*X(i))-1;
    end
end