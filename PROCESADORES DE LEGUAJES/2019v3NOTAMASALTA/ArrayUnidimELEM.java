public class ArrayUnidimELEM extends Expresion {
        public ArrayUnidimELEM(String id, AST pos, AST derecha){
            super(pos,derecha);
            if(TablaSimbolos.getTipoConNiv(id).getTipo().equals("string")){
           this.tipo=new Tipo("string");//importante, esto no tiene tipo arrayunidim sino q int float o char
            }else{
                this.tipo=new Tipo(TablaSimbolos.getTipoConNiv(id).getSubtipo());//importante, esto no tiene tipo arrayunidim sino q int float o char

            }
           palabra=id; //luego la modifico y pasa a ser una temp, pero ahora mismola igualo a id para poder usar el id para hacer t0=x[i], el palabra=id me da esa x del x[i]
          
        }
        
        public void generarCTD(){
            String v=Generador.nuevaLabel();
                String f=Generador.nuevaLabel();
                String fuera=Generador.nuevaLabel();
                String id2=palabra;
                DosEtiq dos=new DosEtiq(v, f);
            if(izq!=null){
                izq.generarCTD();
            }
            if(der!=null){//x[i]=exp, imprimo eso literal
                der.generarCTD();
                if(tipo.tipo().equals(((Expresion)der).getTipo().tipo())){
                    Generador.comparacion(((Expresion)izq).getPalabra(), "<", TablaSimbolos.getTipoConNiv(id2).getLongitud()+"", dos);
                    Generador.etiq(v);
                    Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",((Expresion)der).getPalabra());
                    Generador.salto(fuera);
                    Generador.etiq(f);
                    Generador.errorNoParar("error en dimernsiones array");
                    Generador.etiq(fuera);

                }else if(tipo.tipo().equals(Tipo.FLOAT)&&((Expresion)der).getTipo().tipo().equals(Tipo.INT)){
                    Generador.comparacion(((Expresion)izq).getPalabra(), "<", TablaSimbolos.getTipoConNiv(id2).getLongitud()+"", dos);
                    Generador.etiq(v);
                    String temp=Generador.nuevaTemp();
                    Generador.asignacion(temp,"(float) " +((Expresion)der).getPalabra());
                    Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",temp);
                    this.palabra=temp;                    Generador.salto(fuera);
                    Generador.etiq(f);
                    Generador.errorNoParar("error en dimernsiones array");
                    Generador.etiq(fuera);
                    
                }else if (tipo.tipo().equals("char")&&tipo.tipo().equals(((Expresion)der).getTipo().tipo())){
                    Generador.comparacion(((Expresion)izq).getPalabra(), "<", TablaSimbolos.getTipoConNiv(id2).getLongitud()+"", dos);
                    Generador.etiq(v);
                    Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",((Expresion)der).getPalabra());
                    Generador.salto(fuera);
                    Generador.etiq(f);
                    Generador.errorNoParar("error en dimernsiones array");
                    Generador.etiq(fuera);
                }else if (tipo.tipo().equals("string")&&(Tipo.CHAR).equals(((Expresion)der).getTipo().tipo())){//le he puesto yo tipo char antes estaba tipo.tipo()
                    
                    Generador.comparacion(((Expresion)izq).getPalabra(), "<", palabra+"_length", dos);
                Generador.etiq(v);
                Generador.asignacion(palabra+"["+((Expresion)izq).getPalabra()+"]",((Expresion)der).getPalabra());
                Generador.salto(fuera);
                Generador.etiq(f);
                Generador.errorNoParar("error en dimernsiones string");
                Generador.etiq(fuera);
                tipo=new Tipo("char");
                }else{
                    Generador.error("ERROR DE TIPOS");
                }
               
            }else{//x[i] + 6: primero t0=x[i], luego t0+6 , lo tengo suelto
                
                
            String temp=Generador.nuevaTemp();
            this.palabra=temp;
            if(tipo.tipo().equals("string")){
                Generador.comparacion(((Expresion)izq).getPalabra(), "<", id2+"_length", dos);
                Generador.etiq(v);
            Generador.asignacion(palabra,id2+"["+((Expresion)izq).getPalabra()+"]");
            tipo=new Tipo("char");
            Generador.salto(fuera);
                Generador.etiq(f);
                Generador.errorNoParar("error en dimernsiones string");
                Generador.etiq(fuera);

            }else{
                Generador.comparacion(((Expresion)izq).getPalabra(), "<", TablaSimbolos.getTipoConNiv(id2).getLongitud()+"", dos);
                Generador.etiq(v);
                Generador.asignacion(palabra,id2+"["+((Expresion)izq).getPalabra()+"]");
                Generador.salto(fuera);
                Generador.etiq(f);
                Generador.errorNoParar("error en dimernsiones array");
                Generador.etiq(fuera);

            }  

            }
        }
                  
}
