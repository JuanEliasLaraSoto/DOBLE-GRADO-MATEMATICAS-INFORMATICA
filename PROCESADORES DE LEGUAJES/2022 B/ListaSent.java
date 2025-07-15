public class ListaSent extends Expresion {//le pongo el tipo a la variable, al array o al int x=1;
 public ListaSent(AST izq, AST letra) {//int  x,y=1,z ...
  super(izq, letra);
    this.tipo=((Expresion)letra).getTipo();
 }
 public void generarCTD(){
  if(izq!=null)
   ((Expresion)izq).generarCTD();
    if(der!=null)
    ((Expresion)der).generarCTD();
 
 }
}
