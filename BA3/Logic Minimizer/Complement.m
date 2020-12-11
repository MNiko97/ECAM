function Mtx_comp = Complement(Mtx_in, nbrvar)
    % STEP 1
    % check if matrix is empty
    if isempty(Mtx_in)
        Mtx_comp = ones(1, nbrvar)*3;
        
    % STEP 2 
    % check if there is one 'don't care' cube
    elseif any(all(Mtx_in == 3, 2))
        Mtx_comp = [];   
        
    % STEP 3
    % is the matrix contain only 1 cube, find the complement
    elseif size(Mtx_in,1) == 1
   
        % Get index where 1 need to be replaced by 2
        rowOne = find(Mtx_in == 1);
        colOne = rowOne;
        indexOne = sub2ind([nbrvar nbrvar],rowOne,colOne);
            
        % Get index where 2 need to be replaced by 1
        rowTwo = find(Mtx_in == 2);
        colTwo = rowTwo;
        indexTwo=sub2ind([nbrvar nbrvar],rowTwo,colTwo);
            
        % Create matrix filled with 3
        Mtx_comp = ones(nbrvar,nbrvar)*3;
            
        % Place 2 where 1 was before and place 1 where 2 was before
        Mtx_comp(indexOne)=2;
        Mtx_comp(indexTwo)=1;
            
        % Find and remove rows that contains only 3
        Mtx_comp(find(all(Mtx_comp == 3, 2)),:) = [];
        
    % STEP 4     
    else    
        % if there is 1 and 2 in the same column,
        % the result by summing the two logical matrix "any" will be 2
        % If there is a 2 in this result, then the matrix is biform
        isBiform = any(any(Mtx_in==1)+any(Mtx_in==2) == 2, 1);
        if(any(isBiform))
      
            % return index of all  biform variables
            allBiformIndex = find(isBiform==1);
            
            % return a matrix with two lines : 
            % line 1 = index of all biform variables 
            % line 2 = sum of three at those index
            threeSUM = [allBiformIndex; 
                        sum(Mtx_in(:,allBiformIndex)==3)];
                    
            % return the minimum value of sum of three
            minimum = min(threeSUM(2,:));
            
            % return the index where there is a minimum of three
            lessThreeIndex = find(all(threeSUM(2,:)== minimum,1));
            
            % return the global index (first line in matrix threeSUM
            % where there is less three possible (with lessThreeIndex) 
            variable = threeSUM(1,lessThreeIndex);

            % If there more than one most biform we take the more balanced one
            if(length(variable) > 1)
                Mtx_in(:,variable);
                numberOfOne = sum(Mtx_in(:,variable) == 1);
                numberOfTwo = sum(Mtx_in(:,variable) == 2);
                diff = abs(numberOfOne - numberOfTwo);
                variable = variable(find(diff == min(diff)));
                if(length(variable >1))
                    variable = variable(1);
                endif
            endif
        %if no biform variables then there is a monoform variable
        else
            allThreeSUM = sum(Mtx_in == 3);
            minimumOfThree = find(allThreeSUM == min(allThreeSUM));
            variable = minimumOfThree(1);
        endif
        variableColumn = Mtx_in(:,variable);
        
        % STEP 5
        % Make a copy of input matrix
        positiveCofactor = Mtx_in;
        negativeCofactor = Mtx_in;
        
        % Store index of one and two of the variable
        oneIndex = find(variableColumn == 1);
        twoIndex = find(variableColumn == 2);
        
        % Change 1 in 3 and remove all cube with 2 previously
        positiveCofactor(oneIndex,variable) = 3;
        positiveCofactor(twoIndex,:) = [];
        
        % Change 2 in 3 and remove all cube with 1 previously
        negativeCofactor(twoIndex,variable) = 3;
        negativeCofactor(oneIndex,:) = [];
        
        % STEP 6
        % Recursive Call
        P = Complement(positiveCofactor, nbrvar);
        N = Complement(negativeCofactor, nbrvar);
        
        % AND
        if !isempty(P)
            P(:,variable) = 1;
        endif
        if !isempty(N)
            N(:,variable) = 2;
        endif
        
        % OR
        Mtx_comp = [P;N];    
    endif
endfunction