public class CONDBOOL extends Expresion {
    DosEtiq vf ;
    public  CONDBOOL(AST exp){
        super(exp,null);
        palabra=((Expresion)izq).getPalabra();
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        vf=new DosEtiq(v,f);
        tipo=new Tipo(Tipo.BOOLEAN);
    }
    public void generarCTD(){
        izq.generarCTD();
        
        String fuera=Generador.nuevaLabel();

        Generador.comparacion("0", "<", ((Expresion)izq).getPalabra(), vf);
        //Generador.etiq(v);
        //Generador.asignacion(palabra,"1");
        //Generador.salto(fuera);
        //Generador.etiq(f);
        //Generador.asignacion(palabra, "0");
        //Generador.etiq(fuera);
    }
    public DosEtiq getVF(){
        return vf;
    }
}
