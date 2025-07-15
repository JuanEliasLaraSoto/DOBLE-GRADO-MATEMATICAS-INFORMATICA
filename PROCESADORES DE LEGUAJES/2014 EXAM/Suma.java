public class Suma extends Expresion {
    public Suma(AST izq, AST der) {
        super(izq, der);
        palabra=Generador.nuevaTemp();
    }
    public void generarCTD() {

        // se procesan ambas expresiones participantes en la suma
        if (izq != null) {
            izq.generarCTD();
        }

        if (der != null) {
            der.generarCTD();;
        }

        // Una vez procesados, ya puede imprimirse ti = t1 + t2
        // donde t1 es la temporal asignada a la expresión 1 (igual con t2)
        // (aunque tmb puede tratarse de CONStANtE reales o enteras, porque estas tmb
        // son Tipo EXP)

        Tipo t1 = ((Expresion) izq).getTipo();
        Tipo t2 = ((Expresion) der).getTipo();
        String codIzq = ((Expresion) izq).getPalabra();
        String codDer = ((Expresion) der).getPalabra();
        if (t1.tipo().equals("float") && t2.tipo().equals("float")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            Generador.asignacion(this.palabra, codIzq + " +r " + codDer);
        } else if (t1.tipo().equals("float") && t2.tipo().equals("int")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            String tmp = Generador.nuevaTemp();
            Generador.asignacion(tmp, "(float) " + codDer);
            Generador.asignacion(this.palabra, codIzq + " +r " + tmp);
        } else if (t1.tipo().equals("int") && t2.tipo().equals("float")) {
            this.tipo = new Tipo(Tipo.FLOAT);
            String tmp = Generador.nuevaTemp();
            Generador.asignacion(tmp, "(float) " + codIzq);
            Generador.asignacion(this.palabra, tmp + " +r " + codDer);
        } else if (t1.tipo().equals("int") && t2.tipo().equals("int")) {
            this.tipo = new Tipo(Tipo.INT);
            Generador.asignacion(this.palabra, codIzq + " + " + codDer);
        }else if(t1.tipo().equals("char") && t2.tipo().equals("char")){
            
            Generador.error("intentas sumar dos char, pues -*/ pero no sumar dos chars pq se confunde con concat");

        }else if(t1.tipo().equals("int") && t2.tipo().equals("char")){
            
            Generador.asignacion(palabra,codIzq+" + "+codDer);
            this.tipo=new Tipo("int");
        }else if(t1.tipo().equals("char") && t2.tipo().equals("int")){
            
            Generador.asignacion(palabra,codIzq+" + "+codDer);
            this.tipo=new Tipo("int");
        }
    }

}
