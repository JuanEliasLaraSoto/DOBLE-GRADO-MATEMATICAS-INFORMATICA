int x,y;
select last x from 1 to 10
   select first y from 1 to 10
       where (x+2*y+1 == x*y );
print(x);
print(y);

