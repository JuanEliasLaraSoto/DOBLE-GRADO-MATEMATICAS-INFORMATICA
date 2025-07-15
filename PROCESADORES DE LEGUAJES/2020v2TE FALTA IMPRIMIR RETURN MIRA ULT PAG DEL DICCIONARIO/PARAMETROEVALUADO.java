public class PARAMETROEVALUADO  extends Expresion{
    public PARAMETROEVALUADO(AST exp,AST resto){
        super(exp,resto);
        palabra=((Expresion)izq).getPalabra();
        tipo=((Expresion)izq).getTipo();

    }
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
        if(der!=null){
            der.generarCTD();
        }else{
                        //es el primer param de esta funcion

            Generador.reiniciarParam();
        }
        Generador.asignacion("param "+Generador.numParamIncrementar(),palabra);
    }
}
