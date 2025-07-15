public class SELECTLAST extends Expresion{
    String n1,n2;
    Integer step;
    Integer d;
    public SELECTLAST(AST exp,String n1, String n2,AST cond,Integer step,Integer d){
        super(exp,cond);
        this.n1=n1;
        this.n2=n2;
        this.step=step;
        this.d=d;

    }
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
        String i=Generador.nuevaTemp();
        String v=Generador.nuevaLabel();
        String v2=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String t0=Generador.nuevaTemp();
        String resultado=Generador.nuevaTemp();
        
        Generador.asignacion(resultado,d+"");
        Generador.asignacion(i,n1);
        Generador.etiq(v2);
        Generador.comparacion(i, "<=",n2, new DosEtiq(v, f));
        Generador.etiq(v);

        Generador.asignacion(((Expresion)izq).getPalabra(),i);
        if(der!=null){
            der.generarCTD();
        }
        Generador.etiq(((Condicion)der).getVF().getV());
        Generador.asignacion(resultado,i);
        Generador.etiq(((Condicion)der).getVF().getF());
        Generador.asignacion(i,i+"+"+step);
        Generador.salto(v2);
        Generador.etiq(f);
        Generador.asignacion(((Expresion)izq).getPalabra(), resultado);
    }
    
}
