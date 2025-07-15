public class AND extends Condicion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
    public  AND(AST izq,AST der){
            super(izq, der,"AND");

    }
    ///recuerda q evaluamos en cortocircuito
    public void generarCTD(){//mira if lo q hace para entender lo bien
        if(izq!=null){
            izq.generarCTD();
        }
        //IZQ.GENERARCTD me da : if () goto verdad
                   // goto false;
        ////caso false cond1---CORTOCIRCUITO,DEJO DE EVALUAR Y ME VOY A LA PARTE DEL ELSE
      
        /////caso true cond1(si es false voy a false del tiron)(cortocircuito)
        /// 
        Generador.etiq(((Condicion)izq).getVF().getV());
        if(der!=null){
            der.generarCTD();
        }
        Generador.etiq(((Condicion)izq).getVF().getF());
        Generador.salto(((Condicion)der).getVF().getF());


        ///PARTE DONDE ENTRARA IF ES.GETV  Y DONDE ENTRA EL ELSE ES GETF
       this.vf=new DosEtiq(((Condicion)der).getVF().getV(), ((Condicion)der).getVF().getF());///////LAS DOS Q NO SE HAN USADO


    }
    
}