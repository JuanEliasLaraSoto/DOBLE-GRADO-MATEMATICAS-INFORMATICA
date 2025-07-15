public  class OR extends Expresion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
   
  public  OR(AST izq,AST der){
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
      String temp2=Generador.nuevaTemp();
      Generador.asignacion(temp2,((Expresion)der).getPalabra()+" - "+temp);
      String temp3=Generador.nuevaTemp();
      Generador.asignacion(temp3,((Expresion)izq).getPalabra()+" + "+temp2);

      Generador.comparacion("0", "<", temp3,new DosEtiq(v,f) );
      Generador.etiq(v);
      Generador.asignacion(palabra,"1");
    Generador.salto(fuera);
    Generador.etiq(f);
    Generador.asignacion(palabra, "0");
    Generador.etiq(fuera);
        
    }
    
}
