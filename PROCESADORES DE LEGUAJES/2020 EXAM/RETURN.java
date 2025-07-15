public class RETURN extends Expresion{
    public RETURN(AST exp){
        super(exp,null);
        tipo=((Expresion)izq).getTipo();
        palabra=((Expresion)izq).getPalabra();
    }
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.asignacion("param 0",((Expresion)izq).getPalabra());
    }
    
}
