int x;
int y;
int z;
select x from 2 to 10 default -1 
   select y from 2 to 10 default -2
      select z from 2 to 10 default -3
         where ( x*y*z == x+y+z );
print(x);
print(y);
print(z);

