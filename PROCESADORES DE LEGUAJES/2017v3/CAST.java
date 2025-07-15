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

            }
        }else{
            palabra=((Expresion)der).getPalabra();
        }
        
    
        }
    }
}
    
