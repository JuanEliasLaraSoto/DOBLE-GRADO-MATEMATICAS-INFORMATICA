public class MasUnario extends Expresion {
    public MasUnario (AST e){
        super(e,null);
        palabra=((Expresion)e).getPalabra();
        if(((Expresion)izq).getTipo().tipo().equals(Tipo.CHAR))
        tipo=new Tipo(Tipo.INT);
        else
        tipo=((Expresion)izq).getTipo();
    }
    public void generarCTD(){
        
izq.generarCTD();
        

    }
    
}
