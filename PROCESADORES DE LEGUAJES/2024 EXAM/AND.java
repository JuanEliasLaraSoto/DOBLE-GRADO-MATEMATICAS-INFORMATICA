public class AND extends Expresion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
    public  AND(AST izq,AST der){
            super(izq, der);
palabra=Generador.nuevaTemp();
tipo=new Tipo(Tipo.BOOLEAN);

    }
    ///recuerda q evaluamos en cortocircuito
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
      if(der!=null){
        der.generarCTD();
      }
      String fuera=Generador.nuevaLabel();
      String v=Generador.nuevaLabel();
      String f=Generador.nuevaLabel();

      String temp=Generador.nuevaTemp();
      Generador.asignacion(temp,((Expresion)izq).getPalabra()+" * "+((Expresion)der).getPalabra());
      Generador.comparacion("0", "<", temp,new DosEtiq(v,f) );
      Generador.etiq(v);
      Generador.asignacion(palabra,"1");
    Generador.salto(fuera);
    Generador.etiq(f);
    Generador.asignacion(palabra, "0");
    Generador.etiq(fuera);
        

    }
    
}