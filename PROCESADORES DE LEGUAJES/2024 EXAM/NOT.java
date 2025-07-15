public class NOT extends Expresion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
    public  NOT(AST izq){
            super(izq, null);
            palabra=Generador.nuevaTemp();
            tipo=new Tipo(Tipo.BOOLEAN);

    }
    ///recuerda q evaluamos en cortocircuito
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
      
      String fuera=Generador.nuevaLabel();
      String v=Generador.nuevaLabel();
      String f=Generador.nuevaLabel();

   

      String temp3=Generador.nuevaTemp();
      Generador.asignacion(temp3,"1 - "+((Expresion)izq).getPalabra());

      Generador.comparacion("0", "<", temp3,new DosEtiq(v,f) );
      Generador.etiq(v);
      Generador.asignacion(palabra,"1");
    Generador.salto(fuera);
    Generador.etiq(f);
    Generador.asignacion(palabra, "0");
    Generador.etiq(fuera);
    }
    
}