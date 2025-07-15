public class TERNARIO extends Expresion{
    public TERNARIO (AST cond, AST dosexp){
        super(cond,dosexp);

        this.palabra=Generador.nuevaTemp();
    }
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
        String etiqFuera=Generador.nuevaLabel();
        String verd=((CONDBOOL)izq).getVF().getV();
        Generador.etiq(verd);
        ((Expresion)der.izq).generarCTD();
        Generador.asignacion(palabra,((Expresion)izq).getPalabra());
        Generador.salto(etiqFuera);


        String fals=((CONDBOOL)izq).getVF().getF();
        Generador.etiq(fals);
        ((Expresion)der.der).generarCTD();
        Generador.asignacion(palabra,((Expresion)izq).getPalabra());


        Generador.etiq(etiqFuera);
        


    }
}
