function Sc = correct(X)
    sz = size(X, 1)/6;
    ct1 = 0;
    ct0 = 0;
    flag = 0;
    Sc = zeros(sz, 1);
    for i = 1:sz
        step = (i-1)*6;
        %[step]
        for j = 1:6
            if X((step+j),:) == 1

                if ct1 > 2
                    Sc(step+j) = 0;
                else
                    ct1 = ct1 + 1;
                    Sc(step+j) = 1;
                end
            elseif X((step+j),:) == 0

                if ct0 > 2
                    Sc(step+j) = 1;
                else
                    ct0 = ct0 + 1;
                    Sc(step+j) = 0;
                end
            else
                flag = j;
            end
        end
        if flag > 0
            if ct1 < 3
                Sc(flag+step) = 1;
            else
                Sc(flag+step) = 0;
            end
        end
        flag = 0;
        ct1 = 0;
        ct0 = 0;
    end

end