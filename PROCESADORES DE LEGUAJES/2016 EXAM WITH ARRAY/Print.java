public class Print extends Expresion {
    
    public Print ( AST der) {
        super(null, der);
    }
    public void generarCTD(){
        if(der!=null){
            ((Expresion)der).generarCTD();
        if(((Expresion)der).getTipo().tipo().equals("int")
        ||((Expresion)der).getTipo().tipo().equals("float")){
        Generador.print(((Expresion)der).getPalabra());
        }else if(((Expresion)der).getTipo().tipo().equals("char")){
            Generador.printc(((Expresion)der).getPalabra());

        }else if(((Expresion)der).getTipo().tipo().equals(Tipo.ARRAYUNIDIM)){
            /*
                 * Si es un array, se toma una temporal que va tomando el valor de cada elem t1
                 * = x[i]
                 * y se hace print(t1) cada vez
                 */
            if(((Expresion)der).getTipo().getSubtipo().equals("char")){

            String temp =Generador.nuevaTemp();
            for(int i=0;i<((Expresion)der).getTipo().getLongitud();i++){
                Generador.asignacion(temp,((Expresion)der).getPalabra()+"["+i+"]");
                Generador.printc(temp);
            }
            }else{
                String temp =Generador.nuevaTemp();
            for(int i=0;i<((Expresion)der).getTipo().getLongitud();i++){
                Generador.asignacion(temp,((Expresion)der).getPalabra()+"["+i+"]");
                Generador.print(temp);
            }
        }
        }else if(((Expresion)der).getTipo().tipo().equals(Tipo.ARRAYMULTIDIM)){
            /*
                 * Si es un array, se toma una temporal que va tomando el valor de cada elem t1
                 * = x[i]
                 * y se hace print(t1) cada vez
                 */
            
            
                String temp =Generador.nuevaTemp();
            for(int i=0;i<((Expresion)der).getTipo().getLongitud();i++){
                for(int j=0;j<((Expresion)der).getTipo().getLongitud2();j++){
                int p=i*((Expresion)der).getTipo().getLongitud2() +j;
                Generador.asignacion(temp,((Expresion)der).getPalabra()+"["+p+"]");
                Generador.print(temp);
                }
            }
        
        }else if(((Expresion)der).getTipo().tipo().equals("string")){
            String i=Generador.nuevaTemp();
            String v=Generador.nuevaLabel();
            String v2=Generador.nuevaLabel();
            String f=Generador.nuevaLabel();
            String t0=Generador.nuevaTemp();
            Generador.asignacion(i,"0");
            Generador.etiq(v2);
            Generador.comparacion(i, "<",((Expresion)der).getPalabra()+"_length", new DosEtiq(v, f));
            Generador.etiq(v);
            Generador.asignacion(t0,((Expresion)der).getPalabra()+"["+i+"]");
            Generador.writec(t0);
            Generador.asignacion(i,i+"+1");
            Generador.salto(v2);
                        Generador.writec(10);
        Generador.etiq(f);   

        }

        }
    }
}
