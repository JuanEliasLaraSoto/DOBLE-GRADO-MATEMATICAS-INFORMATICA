public class ELVIS extends Expresion {
        public ELVIS (AST cond,AST e1, AST e2){
            super(cond,new AST(e1,e2));
            palabra=Generador.nuevaTemp();
        }
        public void generarCTD(){
            if(izq!=null){
                izq.generarCTD();
            }
           String verdad=((Condicion)izq).getVF().getV();
           String falso=((Condicion)izq).getVF().getF();
           String fuera=Generador.nuevaLabel();
    
           Generador.etiq(verdad);
           Generador.asignacion(palabra,((Expresion)der.izq).getPalabra());
           Generador.salto(fuera);
           Generador.etiq(falso);
           der.der.generarCTD();
           Generador.asignacion(palabra,((Expresion)der.der).getPalabra());
           Generador.etiq(fuera);
            tipo=((Expresion)der.izq).getTipo();
        }
    }
    