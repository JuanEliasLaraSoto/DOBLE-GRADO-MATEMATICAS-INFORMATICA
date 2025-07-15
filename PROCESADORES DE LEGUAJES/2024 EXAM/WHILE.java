public class WHILE extends Expresion {
    public WHILE(AST cond,AST dentro){
        super(cond,dentro);
    }
    public void generarCTD(){
        String aux=Generador.nuevaLabel();
        Generador.etiq(aux);
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.etiq(((CONDBOOL)izq).getVF().getV());
        if(der!=null){
            der.generarCTD();
        }
        Generador.salto(aux);
        Generador.etiq(((CONDBOOL)izq).getVF().getF());

    }
}
