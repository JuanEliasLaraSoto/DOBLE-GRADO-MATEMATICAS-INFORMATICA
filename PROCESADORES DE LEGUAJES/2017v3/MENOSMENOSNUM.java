public class MENOSMENOSNUM extends Expresion{ 
    protected String id;
    public MENOSMENOSNUM (String id){
        super(null,null);
        palabra=Generador.nuevaTemp();
        this.id=id; 
        this.tipo=TablaSimbolos.getTipoConNiv(id);

    }
    public void generarCTD(){
        Generador.asignacion(palabra,id+"-1");
        Generador.asignacion(id, palabra);
        
    }

}
