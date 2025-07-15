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
        }else if(((Expresion)der).getTipo().tipo().equals("string")){
            if(TablaSimbolos.yaDeclaradaSinNiv(((Expresion)der).getPalabra())){
                Generador.print(((Expresion)der).getPalabra());
            }else{
                for(int i=0; i<((Expresion)der).getPalabra().length();i++){
                    Generador.writec((int)((Expresion)der).getPalabra().charAt(i));
                }
            }
        }

        }
    }
}
