int x;
int y;
int z;
int t;
int w;
int p;
select x from 1 to 10 
   select y from 1 to 10 
      select z from 1 to 10 
         select t from 1 to 10 
            select w from 1 to 10 
               select p from 1 to 10 
                    where ( x*y*z*t*w*p == x+y+z+t+w+p);
print(x);
print(y);
print(z);
print(t);
print(w);
print(p);

