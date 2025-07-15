public class FORIN extends Expresion {
    protected String x;
    protected String miarray;
    public FORIN(String x,String miarray, AST sent){
        super(null,sent);
        this.x=x;
        this.miarray=miarray;
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
        
       
        Generador.etiq(aux);
        Generador.ifsolomenorig(temp,TablaSimbolos.getTipoConNiv(miarray).getLongitud().toString(),verdadero);
        Generador.salto(falso);
        Generador.etiq(verdadero);
        Generador.asignacion(temp2, miarray+"["+temp+"]");//t0=a[i]
        Generador.asignacion(x,temp2);//x=t0 (asi es como se hacen asignaciones con elem d arrays(a[i]))
        if(der!=null){
            der.generarCTD();
        }
        Generador.asignacion(temp,temp+"+1");
        Generador.salto(aux);
        Generador.etiq(falso);

    }
}
