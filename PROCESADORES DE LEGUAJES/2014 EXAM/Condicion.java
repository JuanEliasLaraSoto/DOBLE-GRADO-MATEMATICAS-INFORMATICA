public class Condicion extends Expresion {
    protected DosEtiq vf;
    protected OperandoCond operando;
    public Condicion(AST izq, AST der,String operando) {
        super(izq, der);
        this.operando=new OperandoCond(operando);
        vf=new DosEtiq(Generador.nuevaLabel(),Generador.nuevaLabel());

    }

   

    public String getOperando() {
        return operando.getOperadorExplicito();
    }
    public DosEtiq getVF(){
        return vf;
    }
   

    public void generarCTD() {
        if (izq != null) {
            ((Expresion) izq).generarCTD();
        }
        if (der != null) {
            ((Expresion) der).generarCTD();
        }
        Generador.comparacion(((Expresion)izq).getPalabra(),operando.getOperadorExplicito(),((Expresion)der).getPalabra(),vf);
        
    }
    
}
