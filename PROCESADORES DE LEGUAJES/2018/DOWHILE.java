public class DOWHILE extends Expresion {
    public DOWHILE(AST cond,AST dentro){
        super(cond,dentro);
    }
    public void generarCTD(){
        
        Generador.etiq(((Condicion)izq).getVF().getV());
        if(der!=null){
            der.generarCTD();
        }
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.etiq(((Condicion)izq).getVF().getF());

    }
}
