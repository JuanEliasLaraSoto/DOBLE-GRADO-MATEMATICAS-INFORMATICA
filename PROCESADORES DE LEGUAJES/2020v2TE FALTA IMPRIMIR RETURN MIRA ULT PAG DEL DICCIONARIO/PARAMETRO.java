public class PARAMETRO extends Expresion{
    public PARAMETRO(String id, Tipo t,AST resto){
super(resto,null);
tipo=t;
TablaSimbolos.putConNiv(TablaSimbolos.declarandoConBloqueSinNiv(id), t);
palabra=TablaSimbolos.crearConBloqueSinNiv(id);
    }
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }else{
            //es el primer param de esta funcion
            Generador.reiniciarParam();
        }
        Generador.asignacion(palabra,"param "+Generador.numParamIncrementar());
    }
}