int x;
int y;
repeat {
   x = 2;
   repeat {
       print(x+y); 
       y=x+1; 
   } x times;
   if (x<y) y=x;
} x times; 

