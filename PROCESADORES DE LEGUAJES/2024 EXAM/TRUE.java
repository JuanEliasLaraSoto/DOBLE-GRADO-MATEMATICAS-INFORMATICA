public class TRUE extends Expresion{
    public TRUE(){
        super(null,null);
        palabra=Generador.nuevaTemp();
        tipo=new Tipo(Tipo.BOOLEAN);
    }
    public void generarCTD(){
        Generador.asignacion(palabra,"1");
    }
    
}
