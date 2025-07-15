public class AST{
    protected AST izq,der;
    public AST(AST izq,AST der){
        this.izq=izq;
        this.der=der;

    }
    public AST(){
        this(null,null);
        
    }
    

    public AST getIzq() {
        return this.izq;
    }

   

    public AST getDer() {
        return this.der;
    }


    public void generarCTD(){
        if(izq!=null){izq.generarCTD();}
        if(der!=null){der.generarCTD();}
    }
    @Override
    public String toString() {
        return "AST(" +izq+","+der+")";
            
    }

}