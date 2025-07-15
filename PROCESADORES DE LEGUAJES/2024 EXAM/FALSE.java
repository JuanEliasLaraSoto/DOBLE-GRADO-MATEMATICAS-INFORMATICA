public class FALSE extends Expresion{
    public FALSE(){
        super(null,null);
        palabra=Generador.nuevaTemp();
        tipo=new Tipo(Tipo.BOOLEAN);
    }
    public void generarCTD(){
        Generador.asignacion(palabra,"0");
    }
    
}
