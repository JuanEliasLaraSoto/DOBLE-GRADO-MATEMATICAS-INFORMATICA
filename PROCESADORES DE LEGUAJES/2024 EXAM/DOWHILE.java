public class DOWHILE extends Expresion {
    public DOWHILE(AST cond,AST dentro){
        super(cond,dentro);
    }
    public void generarCTD(){
        
        Generador.etiq(((CONDBOOL)izq).getVF().getV());
        if(der!=null){
            der.generarCTD();
        }
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.etiq(((CONDBOOL)izq).getVF().getF());

    }
}
