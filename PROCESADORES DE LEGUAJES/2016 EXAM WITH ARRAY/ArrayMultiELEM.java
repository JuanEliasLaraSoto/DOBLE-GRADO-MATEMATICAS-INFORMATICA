public class ArrayMultiELEM extends Expresion {
    public ArrayMultiELEM(String id, AST pos1,AST pos2, AST sent){
        super(new AST(pos1,pos2),sent);
        palabra=id;
        tipo=new Tipo(TablaSimbolos.getTipoConNiv(id).getSubtipo());

    }
    public void generarCTD(){
        izq.izq.generarCTD();
        izq.der.generarCTD();
        if(der!=null){//puede ser null en caso q sea uno suelto a[2][3] y no un a[2][3]=der;
            der.generarCTD();
            
            if(tipo.tipo().equals(((Expresion)der).getTipo().tipo())){
                String t0=Generador.nuevaTemp();
                String t1=Generador.nuevaTemp();
                Generador.asignacion(t0,((Expresion)izq.izq).getPalabra()+" * "+TablaSimbolos.getTipoConNiv(palabra).getLongitud2());
                Generador.asignacion(t1,t0+" + "+((Expresion)izq.der).getPalabra());
                Generador.asignacion(palabra+"["+t1+"]",((Expresion)der).getPalabra());
               

            }
        }else{
                String id2=palabra;
                palabra=Generador.nuevaTemp();
                String t0=Generador.nuevaTemp();
                String t1=Generador.nuevaTemp();
                Generador.asignacion(t0,((Expresion)izq.izq).getPalabra()+" * "+TablaSimbolos.getTipoConNiv(id2).getLongitud2());
                Generador.asignacion(t1,t0+" + "+((Expresion)izq.der).getPalabra());
                Generador.asignacion(palabra,id2+"["+t1+"]");
            
        }


    }
}
