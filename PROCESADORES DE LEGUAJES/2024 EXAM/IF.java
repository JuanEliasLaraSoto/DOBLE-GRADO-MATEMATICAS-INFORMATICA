public class IF extends Expresion{
    protected String etiqFuera;
    public IF (AST cond, AST entraIF){
        super(cond,entraIF);

    }

    public String getEtiqFuera() {
        return this.etiqFuera;
    }

   

    public void generarCTD() {

        // como izq es la CONDICION, se imprimirán primero if(..) goto Li \n goto Lj
        ///////////if(..) goto Li \n goto Lj
        if (izq != null) {
            izq.generarCTD();
        }

        String etiqV = ((CONDBOOL) izq).getVF().getV(); // Li
        String etiqF = ((CONDBOOL) izq).getVF().getF(); // Lj

        // Ahora, antes de imprimir la sentencias, imprimimos la etiqueta del caso True
        // ////////("Li: ")
        Generador.etiq(etiqV);

        // esto es solo porque al final del caso True, necesitamos un goto a una
        // etiqueta
        // que marque cómo sigue el programa dps del IF (NO SE IPRIME AÚN)
         etiqFuera = Generador.nuevaLabel();

        // como der es la sentencia a ejecutar, se imprime ahora, dentro de la etiqueta
        // Li (al ser tipo EXP, ya se imprime en su propio ctd() automáticamente)
        //////imprime cod correspondiente de entrar en if
        if (der != null) {
            der.generarCTD();
        }

        // Una vez impresa la sentencia, se imprime el goto a la continuación del
        // programa
        ///////////goto lfuera
        Generador.salto(etiqFuera);

        // se imprime la etiqueta del caso False ("Lj: ")
        //////LJ: (etiqueta del else, si no hay else pues se qda Lj: y debajo se pone loq continua haciendo en ifelse)
        Generador.etiq(etiqF);//NO SE DA CONDICION
        // Como no es un IFELSE, no se ponen sentencias a ejecutar detrás de esta
        // etiqueta, es solo Lj:

        // Finalmente, imprimimos la etiqueta que da lugar a la continuación del código
        // Generador.printLabel(etiqFinal);
        // esto lo comentamos porque ahora se hace al final del IFELSE, que no es más
        // que un IF, al que a continuación de etiqueta Lj, se le añaden sentencias
    }
}
