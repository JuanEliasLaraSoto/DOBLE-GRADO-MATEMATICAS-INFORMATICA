public class SIZE extends Expresion{
    String id;
    public SIZE (String id){
        super(null,null);
        String t0=Generador.nuevaTemp();
        palabra=t0;
        tipo=new Tipo(Tipo.INT);
        this.id=id;
    }
    public void generarCTD(){
        Generador.asignacion(palabra,id+"_length");
    }
    
}
