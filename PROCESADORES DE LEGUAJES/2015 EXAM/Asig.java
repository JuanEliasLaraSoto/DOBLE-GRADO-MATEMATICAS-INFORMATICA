public class Asig extends Expresion {

        public Asig(String id,AST exp2){ //y=x; : ti=y; y=x; (el nuevo codigo es y, la x ya estaba def de antes, pero la novedad es y, y el codigo se genera de la novedad por eso se le asigna a apalabra)
            super(null,exp2);
            this.palabra=id;//codigo nuevo q se añade aqui
        }
       
        

        public void generarCTD(){
            if(der!=null){ 
                
                der.generarCTD();//primero genero el cod de lo de arriba, recuerda q cd tienes y=x;, primero sale ti=y; y=x;;

                String id=palabra;
                this.palabra=((Expresion)der).getPalabra();
                
                if(TablaSimbolos.yaDeclaradaConNiv(id)){
                    Tipo izquierda=TablaSimbolos.getTipoConNiv(id);
                    Tipo derecha=((Expresion)der).getTipo();
                    if(izquierda.tipo().equals(Tipo.ARRAYUNIDIM)&&derecha.tipo().equals(Tipo.ARRAYUNIDIM)){
                        if(izquierda.getSubtipo().equals(derecha.getSubtipo())){
                            if(izquierda.getLongitud()>=derecha.getLongitud()){
                            Generador.asignacion(id,((Expresion)der).getPalabra());
                            }else{
                                Generador.error("matrices incompatibles de tamano");
                            }
                            this.tipo=derecha;
                        }else{
                                Generador.error("ERROR DE TIPOS EN ASIG");
                        }    
                    }else if(izquierda.tipo().equals(Tipo.STRING)&&derecha.tipo().equals(Tipo.STRING)){
                        Generador.asignacion(id,((Expresion)der).getPalabra());

                    }else{

                        if(izquierda.equals(derecha)){
                            Generador.asignacion(id,((Expresion)der).getPalabra());
                            this.tipo=((Expresion)der).getTipo();
                        }else if(izquierda.tipo().equals(Tipo.FLOAT) && derecha.tipo().equals(Tipo.INT)){
                            Generador.asignacion(id,"(float)"+((Expresion)der).getPalabra());
                            this.tipo=new Tipo(Tipo.FLOAT);
                        }else{
                        Generador.error("Error de tipos en la asignacion");
                        }
                    }
                }else{                            

                    Generador.asignacion(id,((Expresion)der).getPalabra());
                    this.tipo=((Expresion)der).getTipo();//añado tipo para cd la veo yadeclarada encima hacer cosas
                }
            }
        }

        public String toString(){
            return "Asig("+tipo+"),";
        }
    

}
