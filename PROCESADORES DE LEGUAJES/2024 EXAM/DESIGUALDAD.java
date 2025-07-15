public class DESIGUALDAD extends Expresion {
    protected OperandoCond operando;
    public DESIGUALDAD(AST izq, AST der,String operando) {
        super(izq, der);
        this.operando=new OperandoCond(operando);
        palabra=Generador.nuevaTemp();
        tipo=new Tipo(Tipo.BOOLEAN);
    }

   

    public String getOperando() {
        return operando.getOperadorExplicito();
    }
    
   

    public void generarCTD() {     
        DosEtiq vf=new DosEtiq(Generador.nuevaLabel(),Generador.nuevaLabel());

        if (izq != null) {
            ((Expresion) izq).generarCTD();
        }
        if (der != null) {
            ((Expresion) der).generarCTD();
        }
        String fuera=Generador.nuevaLabel();

        Generador.comparacion(((Expresion)izq).getPalabra(),operando.getOperadorExplicito(),((Expresion)der).getPalabra(),vf);
        Generador.etiq(vf.getV());
        Generador.asignacion(palabra,"1");
        Generador.salto(fuera);
        Generador.etiq(vf.getF());
        Generador.asignacion(palabra,"0");   
        Generador.etiq(fuera);     
    }
    
}
