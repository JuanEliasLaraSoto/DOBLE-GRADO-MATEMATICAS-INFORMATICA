public class FORALL extends Expresion {
    String id;
    public FORALL(String id,AST exp){
        super(exp,null);
        this.id=id;
        palabra=Generador.nuevaTemp();
        tipo=new Tipo(Tipo.BOOLEAN);
    }
    public void generarCTD(){
        
       String id1= Generador.nuevaTemp();
       String id2= Generador.nuevaTemp();
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String fuera=Generador.nuevaLabel();
        String valororiginal=Generador.nuevaTemp();
        Generador.asignacion(valororiginal,id);

        if(izq!=null){
            izq.generarCTD();
        }

       Generador.asignacion(id1,((Expresion)izq).getPalabra());
       Generador.asignacion(id, "1 - "+id);
       if(izq!=null){
        izq.generarCTD();
        }
        Generador.asignacion(id2,((Expresion)izq).getPalabra());

        Generador.comparacion(id1, "==", id2, new DosEtiq(v, f));
        Generador.etiq(v);
        Generador.asignacion(palabra,"1");
        Generador.salto(fuera);
        Generador.etiq(f);
        Generador.asignacion(palabra,"0");
        Generador.etiq(fuera);
        Generador.asignacion(id, valororiginal);

    }
    
}
