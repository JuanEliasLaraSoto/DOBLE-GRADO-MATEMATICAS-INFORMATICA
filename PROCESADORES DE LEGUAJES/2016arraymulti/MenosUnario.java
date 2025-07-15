public class MenosUnario extends Expresion {
    
        public MenosUnario( AST der) {
            super(null, der);
            palabra=Generador.nuevaTemp();
            if(((Expresion)der).getTipo().tipo().equals("char")){
                tipo=new Tipo(Tipo.INT);// Si se aplica a un carácter, lo convierte implícitamente en un numero entero
            }else{
            tipo=((Expresion)der).getTipo();
            }
        }
        public void generarCTD() {
            if (der != null)
                ((Expresion) der).generarCTD();
            // ahora genero codigo de esta expresion
            Tipo t1 = ((Expresion) der).getTipo();
            String pal1 = ((Expresion) der).getPalabra();
    
            if (t1.tipo().equals("int")) {
                Generador.asignacion(palabra, " - " + pal1);
            } else if (t1.tipo().equals("float")) {
                Generador.asignacion(palabra, " -r " + pal1);
            } else if (t1.tipo().equals("char")) {
                Generador.asignacion(palabra, " - " + pal1);
            }
        }
        
    }
     

