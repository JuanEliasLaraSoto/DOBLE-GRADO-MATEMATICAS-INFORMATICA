public class ArrayUnidimELEM extends Expresion {
        public ArrayUnidimELEM(String id, AST pos, AST derecha){
            super(pos,derecha);
           this.tipo=new Tipo(TablaSimbolos.getTipoConNiv(id).getSubtipo());//importante, esto no tiene tipo arrayunidim sino q int float o char
           palabra=id; //luego la modifico y pasa a ser una temp, pero ahora mismola igualo a id para poder usar el id para hacer t0=x[i], el palabra=id me da esa x del x[i]
          
        }
        
        public void generarCTD(){
            if(izq!=null){
                izq.generarCTD();
            }
            if(der!=null){//x[i]=exp, imprimo eso literal
                der.generarCTD();
                if(tipo.tipo().equals(((Expresion)der).getTipo().tipo())){
                Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",((Expresion)der).getPalabra());

                }else if(tipo.tipo().equals(Tipo.FLOAT)&&((Expresion)der).getTipo().tipo().equals(Tipo.INT)){
                    String temp=Generador.nuevaTemp();
                    Generador.asignacion(temp,"(float) " +((Expresion)der).getPalabra());
                    Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",temp);
                    this.palabra=temp;
                }else if (tipo.tipo().equals("char")&&tipo.tipo().equals(((Expresion)der).getTipo().tipo())){
                    Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",((Expresion)der).getPalabra());

                }else{
                    Generador.error("ERROR DE TIPOS");
                }
               
            }else{//x[i] + 6: primero t0=x[i], luego t0+6 , lo tengo suelto
            String temp=Generador.nuevaTemp();
            String id=palabra;
            this.palabra=temp;
            
            Generador.asignacion(palabra,id+"["+((Expresion)izq).getPalabra()+"]");  

            }
        }
                  
}
