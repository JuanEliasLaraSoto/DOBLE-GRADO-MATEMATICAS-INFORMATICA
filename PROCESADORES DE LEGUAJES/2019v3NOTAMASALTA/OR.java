public  class OR extends Condicion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
    public  OR(AST izq,AST der){
            super(izq, der,"OR");

    }
    ///recuerda q evaluamos en cortocircuito
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
        //IZQ.GENERARCTD me da : if () goto verdad
                   // goto false;
        //cond1 true--entramos en if direct
        

        /////caso false  cond1--seguimos
        Generador.etiq(((Condicion)izq).getVF().getF());
        if(der!=null){
            der.generarCTD();
        }
        Generador.etiq(((Condicion)izq).getVF().getV());
        Generador.salto(((Condicion)der).getVF().getV());
        
//IZQ V siempre es cierto y se va directamentr
        ///PARTE DONDE ENTRARA IF ES.GETV  Y DONDE ENTRA EL ELSE ES GETF
       this.vf=new DosEtiq(((Condicion)der).getVF().getV(), ((Condicion)der).getVF().getF());///////LAS DOS Q NO SE HAN USADO


    }
    
}
