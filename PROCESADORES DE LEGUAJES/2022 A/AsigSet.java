public class AsigSet extends Expresion {//tan solo se usa en var, en la incializacion si hay una asig, en ese caso no se el tipo de id, asi q me creo esto para poder hacerlo bien, el tipo de id y se le asigna luego en lista sent, te dara error si usas asigarr en vez d esta en la linea         tipo=TablaSimbolos.getTipoConNiv(id); ya queel tipo de id se asigna luego y s mete luego en tabla simbolo(esto lo hago dentro de var pq quiero admitir set int c,b,d; pero si t la pela y solo hay un caso prueba q pide esto pues hazlo como los arrays)

    public AsigSet (String id,AST exp){
        super(null,exp);
        palabra=id;
        tipo=((Expresion)der).getTipo();
    }
    public void generarCTD(){
        der.generarCTD();
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String aux=Generador.nuevaLabel();
        String i=Generador.nuevaTemp();
        String t0=Generador.nuevaTemp();

        Generador.asignacion(i,"0");
        Generador.etiq(aux);
        Generador.comparacion(i, "<", ((Expresion)der).getPalabra()+"_length", new DosEtiq(v, f));
        Generador.etiq(v);
        Generador.asignacion(t0, ((Expresion)der).getPalabra()+"["+i+"]");
        Generador.asignacion(palabra+"["+i+"]", t0);
        Generador.asignacion(i,i+"+1");
        Generador.salto(aux);
        Generador.etiq(f);
        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length");
    }
}
