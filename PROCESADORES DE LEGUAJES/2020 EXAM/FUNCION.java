public class FUNCION extends Expresion {
    public FUNCION(Tipo t,String id,AST listParam,AST sent){
        super(listParam,sent);
        tipo=t;
        TablaSimbolos.putConNivF(TablaSimbolos.declarandoConBloqueSinNivF(id), t);

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
