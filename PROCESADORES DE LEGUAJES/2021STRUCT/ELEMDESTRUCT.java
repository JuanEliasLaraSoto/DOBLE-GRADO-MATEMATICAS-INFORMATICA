public class ELEMDESTRUCT extends Expresion {
    String id,t;
    public ELEMDESTRUCT(Tipo t, String id,AST resto){
        super(null,resto);
        this.id=id;
        this.tipo=t;
    }
    public void generarCTD(String x){
        if(der!=null){
            der.generarCTD(x);
        }

        String porcent=x+"$"+id;
        palabra=TablaSimbolos.declarandoConBloqueSinNiv(porcent);

        TablaSimbolos.putConNiv(palabra, tipo);
    }
}
