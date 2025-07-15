public class VOID extends Expresion {
    public VOID(String id,AST listParam,AST sent){
        super(listParam,sent);
        tipo=new Tipo(Tipo.VOID);
        TablaSimbolos.putConNivF(TablaSimbolos.declarandoConBloqueSinNivF(id), tipo);
        palabra=id;
    }
    public void generarCTD(){
        Generador.function(palabra);
        if(izq!=null){
            izq.generarCTD();
        }
        if(der!=null){
            der.generarCTD();
        }
        Generador.end(palabra);
    }
    
}
