public class MINaMAYUSC extends Expresion{
    protected String id;
    public MINaMAYUSC (String id){
        super(null,null);
        palabra=Generador.nuevaTemp();
        this.id=id;
        tipo=TablaSimbolos.getTipoConNiv(id);
        }
    public void generarCTD(){
        Generador.asignacion(palabra,id+"-32");
        Generador.asignacion(id, palabra);
        
    }



}
