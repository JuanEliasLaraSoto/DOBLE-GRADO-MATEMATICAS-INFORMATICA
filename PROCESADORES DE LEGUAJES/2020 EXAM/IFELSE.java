public class IFELSE extends Expresion{
    public IFELSE (AST parteIf,AST seVaElse){
         
        super(parteIf,seVaElse);

    }
    public void generarCTD(){
        /////genero lo de nates de if
        if(izq!=null){
            izq.generarCTD();
        }
        /////genero interior del else, si no hay pues no lo genero por eso el !=null
        if(der!=null){
        der.generarCTD();}
        
       String etiqFuera=((IF)izq).getEtiqFuera();
       //////Lfuera:
       Generador.etiq(etiqFuera);
        

    }
}
