public class MASMASNUM extends Expresion{ 
    protected String id;
    public MASMASNUM (String id){
        super(null,null);
        palabra=Generador.nuevaTemp();
        this.id=id;
        this.tipo=TablaSimbolos.getTipoConNiv(id);
    }
    public void generarCTD(){
        Generador.asignacion(palabra,id+"+1");
        Generador.asignacion(id, palabra);
        
    }

}
