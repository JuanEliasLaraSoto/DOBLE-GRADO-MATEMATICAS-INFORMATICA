public class Cadena extends Expresion {
     public Cadena (String cadena){
        super(null,null);
        tipo=new Tipo("string");
        palabra=cadena;
    }
   
}
