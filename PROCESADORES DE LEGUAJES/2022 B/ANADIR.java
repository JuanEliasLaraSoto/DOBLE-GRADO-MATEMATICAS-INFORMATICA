public class ANADIR extends Expresion{
    public ANADIR(String id,AST l){
        super(null,l);
        tipo=TablaSimbolos.getTipoConNiv(id);
        palabra=id;
    }
    public void generarCTD(){
        der.generarCTD();
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String aux=Generador.nuevaLabel();
        String i=Generador.nuevaTemp();
        String t0=Generador.nuevaTemp();
        String t1=Generador.nuevaTemp();
        String v2=Generador.nuevaLabel();
        String f2=Generador.nuevaLabel();
        String i2=Generador.nuevaTemp();
        String aux2=Generador.nuevaLabel();
        String v3=Generador.nuevaLabel();
        String f3=Generador.nuevaLabel();
        String t3=Generador.nuevaTemp();

        Generador.asignacion(t3,"0");
        Generador.asignacion(i,"0");
        Generador.etiq(aux);
        Generador.comparacion(i, "<", ((Expresion)der).getPalabra()+"_length", new DosEtiq(v, f));
        Generador.etiq(v);
        Generador.asignacion(t0, ((Expresion)der).getPalabra()+"["+i+"]");
        Generador.asignacion(t3,palabra+"_length"+"-"+t3);
        Generador.asignacion(t1, i+"+"+t3);
       
        //vemos si ya esat o no, en caso de q este no se añade
        Generador.asignacion(i2, "0");
        Generador.etiq(aux2);
        Generador.comparacion(i2, "<", palabra+"_length", new DosEtiq(v3, f3));
        Generador.etiq(v3);
        Generador.comparacion(palabra+"["+i2+"]", "==", t0, new DosEtiq(v2, f2));
        Generador.etiq(v2);
        Generador.asignacion(i,i+"+1");//
        Generador.asignacion(t3, t3+"+1");
        Generador.salto(aux);
        Generador.etiq(f2);
        Generador.asignacion(i2,i2+"+1");
        Generador.salto(aux2);
        Generador.etiq(f3);

        Generador.asignacion(palabra+"["+t1+"]", t0);
        Generador.asignacion(i,i+"+1");
        Generador.salto(aux);
        Generador.etiq(f);
        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length"+"+"+palabra+"_length");
    }
}
