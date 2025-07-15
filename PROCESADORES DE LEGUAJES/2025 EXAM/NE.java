public class NE extends Expresion {
    protected DosEtiq vf;
    public NE(AST izq, AST der) {
        super(null, der);
        vf=new DosEtiq(Generador.nuevaLabel(), Generador.nuevaLabel());

    }

    public void generarCTD() {
        if (izq != null) {
            ((Expresion) izq).generarCTD();
        }
        if (der != null) {
            ((Expresion) der).generarCTD();
        }
        Generador.comparacion("","!=",((Expresion)der).getPalabra(),vf);
        
    }
    
}
