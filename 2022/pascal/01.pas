program day01;
uses Math;

var
  current_sum: longint;
  largest_sum: longint;
  top: array[1..3] of longint;


procedure endOfGroup;
  var 
    i, j: integer;
    
  begin
    for i := 1 to 3 do
      if current_sum > top[i] then 
        begin
          for j := 3 downto i + 1 do
            top[j] := top[j-1];
              
          top[i] := current_sum;
          break
        end;
    
    largest_sum := max(largest_sum, current_sum);
    current_sum := 0;
    readln
  end;


procedure nextNumber;
  var 
    n: longint;
    
  begin 
    readln(n);
    current_sum := current_sum + n
  end;
  

begin
  while not eof do
    if eoln then 
      endOfGroup
    else
      nextNumber;
 
    writeln(largest_sum);
    writeln(top[1] + top[2] + top[3])
end.