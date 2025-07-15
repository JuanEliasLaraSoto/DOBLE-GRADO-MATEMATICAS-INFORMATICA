public class FORIN extends Expresion {
    protected String x;
    public FORIN(String x,AST exp, AST sent){
        super(exp,sent);
        this.x=x;
    }
    public void generarCTD(){

        /*
         * 

            i = 0;//lacreo yo
            L0:
            if (i < arr_length) goto L1;
            goto L2;
            L1:
            //aqui esta el truco de forin trducido a un while
            x = arr[i];
            //genero sent
            print x;
            //incremento i
            i = i + 1;
            goto L0;
            L2:

         */

        String aux=Generador.nuevaLabel();
        String temp=Generador.nuevaTemp();
        String verdadero=Generador.nuevaLabel();
        String falso=Generador.nuevaLabel();
        String temp2=Generador.nuevaTemp();
        Generador.asignacion(temp,"0");
        
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.etiq(aux);
        Generador.ifsolomenorig(temp,(((Expresion)izq).getTipo().getLongitud()).toString(),verdadero);
        Generador.salto(falso);
        Generador.etiq(verdadero);
        Generador.asignacion(temp2, ((Expresion)izq).getPalabra()+"["+temp+"]");//t0=a[i]
        Generador.asignacion(x,temp2);//x=t0 (asi es como se hacen asignaciones con elem d arrays(a[i]))
        if(der!=null){
            der.generarCTD();
        }
        Generador.asignacion(temp,temp+"+1");
        Generador.salto(aux);
        Generador.etiq(falso);

    }
}
