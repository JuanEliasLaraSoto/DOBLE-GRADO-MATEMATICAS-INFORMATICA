public class NOT extends Condicion {/////PIENSA EN LOQ HACE LUEGO EL IF BASICAMENTE
    public  NOT(AST izq){
            super(izq, null,"NOT");

    }
    ///recuerda q evaluamos en cortocircuito
    public void generarCTD(){
        if(izq!=null){
            izq.generarCTD();
        }
       
       this.vf=new DosEtiq(((Condicion)izq).getVF().getF(), ((Condicion)izq).getVF().getV());///////LAS DOS Q NO SE HAN USADO


    }
    
}