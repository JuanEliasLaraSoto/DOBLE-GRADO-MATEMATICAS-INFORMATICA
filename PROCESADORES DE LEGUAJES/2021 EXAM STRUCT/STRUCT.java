public class STRUCT extends Expresion {
    public STRUCT(String i,AST l){
        super(null,l);
        tipo=new Tipo(Tipo.STRUCT);
        palabra=i;
        if(der!=null){
            der.generarCTD(palabra);
        }
    }
    //AQUI HABRIA Q DEFINIR EL generarCTD(String p) para cd haya un struct dentro d otro pues la palabra nocreoqmal , mal pq la palbr ahay q asignarla arriba en la declaracion, de todas formas este generarctd(String p) solo seria llamado por el struct padrisimo pq los de mas arriba del struc padre no llaman a generar(String) sino q a generarctd() y este en este caso en generarctd esta vacio no genera codigo
    public void generarCTD(){
        
    }
}
