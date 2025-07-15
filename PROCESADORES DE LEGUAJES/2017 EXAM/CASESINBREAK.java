public class CASESINBREAK extends Expresion{
    protected String control,fuera,SINBREAK;
    public CASESINBREAK(String SINBREAK,String fuera,String control,AST condicion,AST sentencia){
        super(condicion,sentencia);
        this.control=control;
        this.fuera=fuera;
        this.SINBREAK=SINBREAK;
    }
    public void generarCTD(String x){
        if(izq!=null){
            izq.generarCTD();
        }
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        if(SINBREAK.equals("SI")){
            if(der!=null){
        der.generarCTD();
            }
        }else{
            Generador.comparacion(x, "==", ((Expresion)izq).getPalabra(), new DosEtiq(v, f));
            Generador.etiq(v);
            if(der!=null){
            der.generarCTD();
            }
            Generador.etiq(f); 
        }
    }
}
