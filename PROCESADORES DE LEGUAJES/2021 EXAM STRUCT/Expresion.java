public class Expresion extends AST {
    protected String palabra;
    protected Tipo tipo;
    public Expresion(AST izq, AST der) {//es un ast pero con codigo, son todas las asig,suma,resta que llevan codigo q tiene q ser generado, es el ti=x; o ti=2*4; es el t basicamente q se genera
        super(izq, der);
        this.palabra="";
    }


    public String getPalabra() {
        return this.palabra;
    }

   public void generarCTD(){//
        if(izq!=null)
            ((Expresion)izq).generarCTD();
        if(der!=null)
            ((Expresion)der).generarCTD();
    }
    public void generarCTD(String x){//
        if(izq!=null)
            ((Expresion)izq).generarCTD(x);
        if(der!=null)
            ((Expresion)der).generarCTD(x);
    }
    public void setTipo(Tipo t){
        this.tipo=t;
    }
    
        public Tipo getTipo() {
            return this.tipo;
        }
}
