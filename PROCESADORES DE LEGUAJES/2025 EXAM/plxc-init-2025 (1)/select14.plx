int x;
int y;
int z;
int t;
select x from 1 to 10 
   select y from 1 to 10 
      select z from 1 to 10 
         select t from 1 to 10 
            where ( x*y*z*t == x+y+z+t);
print(x);
print(y);
print(z);
print(t);

