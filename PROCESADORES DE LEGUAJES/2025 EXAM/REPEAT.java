public class REPEAT extends Expresion{
    public REPEAT(AST e1,AST veces){
        super(e1,veces);


    }
    public void generarCTD(){
       
        
        String i=Generador.nuevaTemp();
        String v=Generador.nuevaLabel();
        String v2=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String t0=Generador.nuevaTemp();
        String v1=Generador.nuevaLabel();
        String fuera=Generador.nuevaLabel();
        String f1=Generador.nuevaLabel();
        String lim=Generador.nuevaTemp();
        
       

        Generador.asignacion(i,"0");
        Generador.etiq(v2);
        if(der!=null){
            der.generarCTD();
        }

        Generador.comparacion(((Expresion)der).getPalabra(), "<","0", new DosEtiq(v1,f1));
        Generador.etiq(v1);
        Generador.asignacion(lim, "1");
        Generador.salto(fuera);
        Generador.etiq(f1);
        Generador.asignacion(lim, ((Expresion)der).getPalabra());
        Generador.etiq(fuera);

        

        Generador.comparacion(i, "<",lim, new DosEtiq(v, f));
        Generador.etiq(v);
        if(izq!=null){
            izq.generarCTD();
        }
        Generador.asignacion(i,i+"+1");
        Generador.salto(v2);
        Generador.etiq(f);
    }
}
