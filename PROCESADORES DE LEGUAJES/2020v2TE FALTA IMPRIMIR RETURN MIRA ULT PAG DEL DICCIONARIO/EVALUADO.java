public class EVALUADO extends Expresion {
    String id;
    public EVALUADO(String id,AST listaParam){
        super(null,listaParam);
        this.id=id;
        tipo=TablaSimbolos.getTipoConNiv(TablaSimbolos.crearConBloqueSinNiv(id));
        if(!tipo.getTipo().equals(Tipo.VOID)){
            String t0=Generador.nuevaTemp();
            palabra=t0;
        }else{
            palabra=id;
        }
    }
    public void generarCTD(){        

        if(der!=null){
            der.generarCTD();
        }
        Generador.call(id);
        if(!tipo.getTipo().equals(Tipo.VOID)){

        Generador.asignacion(palabra, "param 0");
        }

    }
    
}
