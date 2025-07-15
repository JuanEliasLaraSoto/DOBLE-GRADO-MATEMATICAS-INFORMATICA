int x;
int y;
select x from 2 to 10 step 2 
   select y from 2 to 10 step 2
      where ( x*y == 24 );
print(x);
print(y);

