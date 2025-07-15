int x;
int y;
select y from 1 to 10 
   select x from 1 to 10 
      where ( x*y == 24 );
print(x);
print(y);

