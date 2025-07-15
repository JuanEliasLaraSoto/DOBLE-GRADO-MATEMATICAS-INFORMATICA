public class Suma extends Expresion {
    public Suma(AST izq, AST der) {
        super(izq, der);
        
        palabra=Generador.nuevaTemp();
        
    }
    public void generarCTD() {

        // se procesan ambas expresiones participantes en la suma
        if (izq != null) {
            izq.generarCTD();
        }

        if (der != null) {
            der.generarCTD();;
        }
        if((((Expresion)izq).getTipo().tipo().equals("char")&&((Expresion)der).getTipo().tipo().equals("char")
        )||((Expresion)izq).getTipo().tipo().equals("string")||((Expresion)der).getTipo().tipo().equals("string")){
            palabra=Generador.nuevaTemp();
            palabra=TablaSimbolos.declarandoConBloqueSinNiv(palabra);
            TablaSimbolos.putConNiv((palabra),new Tipo(Tipo.STRING));

        }
        // Una vez procesados, ya puede imprimirse ti = t1 + t2
        // donde t1 es la temporal asignada a la expresión 1 (igual con t2)
        // (aunque tmb puede tratarse de CONStANtE reales o enteras, porque estas tmb
        // son Tipo EXP)

        Tipo t1 = ((Expresion) izq).getTipo();
        Tipo t2 = ((Expresion) der).getTipo();
        String codIzq = ((Expresion) izq).getPalabra();
        String codDer = ((Expresion) der).getPalabra();
        if (t1.tipo().equals("float") && t2.tipo().equals("float")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            Generador.asignacion(this.palabra, codIzq + " +r " + codDer);
        } else if (t1.tipo().equals("float") && t2.tipo().equals("int")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            String tmp = Generador.nuevaTemp();
            Generador.asignacion(tmp, "(float) " + codDer);
            Generador.asignacion(this.palabra, codIzq + " +r " + tmp);
        } else if (t1.tipo().equals("int") && t2.tipo().equals("float")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            String tmp = Generador.nuevaTemp();
            Generador.asignacion(tmp, "(float) " + codIzq);
            Generador.asignacion(this.palabra, tmp + " +r " + codDer);
        } else if (t1.tipo().equals("int") && t2.tipo().equals("int")) {
            this.tipo = new Tipo(Tipo.INT);
            Generador.asignacion(this.palabra, codIzq + " + " + codDer);
        }else if(t1.tipo().equals("char") && t2.tipo().equals("char")){
            Generador.asignacion(palabra+"[0]",((Expresion)izq).getPalabra());
            Generador.asignacion(palabra+"[1]",((Expresion)der).getPalabra());
            Generador.asignacion(palabra+"_length","2");
            tipo=new Tipo(Tipo.STRING);

        }else if(t1.tipo().equals("string") && t2.tipo().equals("string")){
            String cont = Generador.nuevaTemp();
                        String inicio = Generador.nuevaLabel();
                        String aux= Generador.nuevaTemp();
                        this.tipo=new Tipo(Tipo.STRING);
                        
                        String inicio2 = Generador.nuevaLabel();
                        String aux2= Generador.nuevaTemp();
                        DosEtiq et = new DosEtiq(Generador.nuevaLabel(), Generador.nuevaLabel());
                        DosEtiq et2 = new DosEtiq(Generador.nuevaLabel(), Generador.nuevaLabel());
                        Generador.asignacion(cont, "0");

                        Generador.etiq(inicio);

                        Generador.comparacion( cont,"<", ((Expresion)izq).getPalabra() + "_length", et);
                        
                        Generador.etiq(et.getV());
                        
                        Generador.asignacion(aux,((Expresion)izq).getPalabra()+"["+cont+"]");
                        Generador.asignacion(palabra+"["+cont+"]",aux);
                        Generador.asignacion(cont, cont + " + 1");
                        Generador.salto(inicio);

                        Generador.etiq(et.getF());
//concat la segunda:
                        String suma=Generador.nuevaTemp();
                        Generador.asignacion(suma, ((Expresion)der).getPalabra() + "_length"+"+"+cont);
                        Generador.etiq(inicio2);
                        
                        
                        Generador.comparacion( cont,"<", suma, et2);
                        
                        Generador.etiq(et2.getV());
                        String resta=Generador.nuevaTemp();
                        Generador.asignacion(resta, cont+"-"+((Expresion)izq).getPalabra()+"_length");
                        Generador.asignacion(aux2,((Expresion)der).getPalabra()+"["+resta+"]");
                        Generador.asignacion(palabra+"["+cont+"]",aux2);
                        Generador.asignacion(cont, cont + " + 1");
                        Generador.salto(inicio2);

                        Generador.etiq(et2.getF());
                        
                        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length + "+((Expresion)izq).getPalabra()+"_length");
        }else if(t1.tipo().equals("string") && t2.tipo().equals("char")){
            String cont = Generador.nuevaTemp();
                        String inicio = Generador.nuevaLabel();
                        String aux= Generador.nuevaTemp();
                        this.tipo=new Tipo(Tipo.STRING);
                                               
                        DosEtiq et = new DosEtiq(Generador.nuevaLabel(), Generador.nuevaLabel());
                        Generador.asignacion(cont, "0");
                        
                        Generador.etiq(inicio);

                        Generador.comparacion( cont,"<", ((Expresion)izq).getPalabra() + "_length", et);
                        
                        Generador.etiq(et.getV());
                        
                        Generador.asignacion(aux,((Expresion)izq).getPalabra()+"["+cont+"]");
                        Generador.asignacion(palabra+"["+cont+"]",aux);
                        Generador.asignacion(cont, cont + " + 1");
                        Generador.salto(inicio);

                        Generador.etiq(et.getF());
//concat la segunda:

                        
                        
                        Generador.asignacion(palabra+"["+cont+"]",((Expresion)der).getPalabra());
                        Generador.asignacion(cont, cont + " + 1");


                        Generador.asignacion(palabra+"_length",((Expresion)izq).getPalabra()+"_length"+"+1");
           
        }else if(t1.tipo().equals("char") && t2.tipo().equals("string")){
            String cont = Generador.nuevaTemp();
                        String inicio = Generador.nuevaLabel();
                        String aux= Generador.nuevaTemp();
                        this.tipo=new Tipo(Tipo.STRING);
                        
                        DosEtiq et = new DosEtiq(Generador.nuevaLabel(), Generador.nuevaLabel());
                       
                        Generador.asignacion(cont, "0");
                        Generador.asignacion(palabra+"["+cont+"]",((Expresion)izq).getPalabra());
                        Generador.asignacion(cont, cont + " + 1");
                        
                        String suma=Generador.nuevaTemp();
                        Generador.asignacion(suma, ((Expresion)der).getPalabra() + "_length"+"+"+"1");
                        Generador.etiq(inicio);

                        Generador.comparacion( cont,"<",suma, et);
                        
                        Generador.etiq(et.getV());
                         String resta=Generador.nuevaTemp();
                        Generador.asignacion(resta, cont+"-"+"1");
                        Generador.asignacion(aux,((Expresion)der).getPalabra()+"["+resta+"]");
                        Generador.asignacion(palabra+"["+cont+"]",aux);
                        Generador.asignacion(cont, cont + " + 1");
                        Generador.salto(inicio);

                        Generador.etiq(et.getF());
//concat la segunda:

                        
                        
                        

                        
                        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length"+"+1");
        
        
        }else if(t1.tipo().equals("int") && t2.tipo().equals("char")){
            
            Generador.asignacion(palabra,codIzq+" + "+codDer);
            this.tipo=new Tipo("int");
        }else if(t1.tipo().equals("char") && t2.tipo().equals("int")){
            
            Generador.asignacion(palabra,codIzq+" + "+codDer);
            this.tipo=new Tipo("int");
        }
    }

}
