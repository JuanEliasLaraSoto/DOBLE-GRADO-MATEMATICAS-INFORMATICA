public class CAST extends Expresion {
    public CAST(Tipo tipoCast,AST exp){
        super(null,exp);
        this.tipo=tipoCast;
    }
    public void generarCTD(){
        if(der!=null){
            der.generarCTD();
        if(!(tipo.tipo().equals(((Expresion)der).getTipo().tipo()))){
            if(tipo.tipo().equals("int")||tipo.tipo().equals("float")){
                palabra=Generador.nuevaTemp();
                Generador.asignacion(palabra, "("+tipo.tipo()+") " +((Expresion)der).getPalabra());
            }else if(tipo.tipo().equals("char")){
                palabra=((Expresion)der).getPalabra();
                ((Expresion)der).tipo=new Tipo("char");

            }else if(tipo.tipo().equals("string")&&((Expresion)der).getTipo().tipo().equals("char")){
                String t0=Generador.nuevaTemp();
                palabra=TablaSimbolos.declarandoConBloqueSinNiv(t0);
                TablaSimbolos.putConNiv(t0, tipo);
                String t1=Generador.nuevaTemp();
                Generador.asignacion(t1,((Expresion)der).getPalabra());
                Generador.asignacion(palabra+"["+"0"+"]",t1);
               
                Generador.asignacion(palabra+"_length","1" );
            }else if(tipo.tipo().equals("string")&&((Expresion)der).getTipo().tipo().equals("arrayunidim")){
                String t4=Generador.nuevaTemp();
                palabra=TablaSimbolos.declarandoConBloqueSinNiv(t4);
                TablaSimbolos.putConNiv(t4, tipo);
                
               
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
                Generador.asignacion(palabra+"["+i+"]",t0);

                Generador.asignacion(i,i+"+1");
                Generador.salto(v2);
            Generador.etiq(f); 
            Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length" );

        }else if(tipo.tipo().equals("arrayunidim")&&((Expresion)der).getTipo().tipo().equals("string")){
            String t4=Generador.nuevaTemp();
            palabra=TablaSimbolos.declarandoConBloqueSinNiv(t4);
            TablaSimbolos.putConNiv(t4, tipo);
            
           
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
            Generador.asignacion(palabra+"["+i+"]",t0);

            Generador.asignacion(i,i+"+1");
            Generador.salto(v2);
        Generador.etiq(f); 
        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length" );
            
        }
        
        }else if(tipo.tipo().equals("arrayunidim")&&((Expresion)der).getTipo().tipo().equals("arrayunidim")){
            String t4=Generador.nuevaTemp();
            palabra=TablaSimbolos.declarandoConBloqueSinNiv(t4);
            TablaSimbolos.putConNiv(t4, tipo);

           
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
            Generador.asignacion(palabra+"["+i+"]",t0);

            Generador.asignacion(i,i+"+1");
            Generador.salto(v2);
        Generador.etiq(f); 
        Generador.asignacion(palabra+"_length",((Expresion)der).getPalabra()+"_length" );
            tipo=new Tipo(Tipo.ARRAYUNIDIM,tipo.getSubtipo(),((Expresion)der).getTipo().getLongitud());
        }        else{
            palabra=((Expresion)der).getPalabra();
        }
        
    
        }
    }
}
    
