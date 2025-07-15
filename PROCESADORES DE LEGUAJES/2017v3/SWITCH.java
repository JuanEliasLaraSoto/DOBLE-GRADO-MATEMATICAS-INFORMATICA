public class SWITCH extends Expresion{
    protected String fuera;
    public SWITCH (String fuera,AST e1,AST e2){
        super(e1,e2);
        this.fuera=fuera;
    }
    public void generarCTD(){
        izq.generarCTD();
        der.generarCTD(((Expresion)izq).getPalabra());
        Generador.etiq(fuera);
    }
    
}
