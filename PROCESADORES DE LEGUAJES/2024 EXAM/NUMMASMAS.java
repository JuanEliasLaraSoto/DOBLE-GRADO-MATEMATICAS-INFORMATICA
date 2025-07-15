public class NUMMASMAS extends Expresion{ 
    protected String id;
    public NUMMASMAS (String id){
        super(null,null);
        palabra=Generador.nuevaTemp();
        this.id=id;    
        this.tipo=TablaSimbolos.getTipoConNiv(id);

    }
    public void generarCTD(){
        Generador.asignacion(palabra,id);
        Generador.asignacion(id, id+"+1");
        
    }

}
