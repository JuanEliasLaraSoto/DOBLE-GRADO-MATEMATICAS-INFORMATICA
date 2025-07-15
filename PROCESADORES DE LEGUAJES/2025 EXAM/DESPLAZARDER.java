public class DESPLAZARDER extends Expresion {
    String n;
    public DESPLAZARDER(AST exp,AST exp2){
        super(exp,exp2);
        this.tipo=new Tipo(Tipo.INT);
        this.palabra=Generador.nuevaTemp();
    }
    public void generarCTD(){
        if (izq!=null) {
            izq.generarCTD();
        }
        if(der!=null){
            der.generarCTD();
        }
        String palabraExp=((Expresion)izq).getPalabra();

        String i=Generador.nuevaTemp();
        String v=Generador.nuevaLabel();
        String aux=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String v2=Generador.nuevaLabel();
        String f2=Generador.nuevaLabel();
        String t0=Generador.nuevaTemp();
        String fuera=Generador.nuevaLabel();


        Generador.asignacion(i,"0");
        Generador.etiq(aux);
        Generador.comparacion(i, "<",((Expresion)der).getPalabra(), new DosEtiq(v, f));
        Generador.etiq(v);

        Generador.comparacion(i, "==", "0", new DosEtiq(v2, f2));
        Generador.etiq(v2);
        Generador.asignacion(palabra, palabraExp +" / "+"2");
        Generador.salto(fuera);
        Generador.etiq(f2);
        Generador.asignacion(palabra, palabra +" / "+"2");
        
        Generador.etiq(fuera);
        Generador.asignacion(i,i+"+1");
        Generador.salto(aux);
        Generador.etiq(f);



       /* for(int i=0; i<Integer.parseInt(n);i++){
            if(i==0){
                Generador.asignacion(palabra, palabraExp +" / "+((Expresion)der).getPalabra());

            }else{
                Generador.asignacion(palabra, palabra +" / "+((Expresion)der).getPalabra());

            }
        }*/
    }
    
}
