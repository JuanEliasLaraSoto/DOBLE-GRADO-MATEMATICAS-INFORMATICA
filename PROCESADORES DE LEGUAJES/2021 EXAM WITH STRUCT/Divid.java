public class Divid extends Expresion {
    public Divid(AST izq, AST der) { // x/y : ti=x/y; (nuevo codigo aqui es ti loq genero , la x y la y ya estan generada de antes, pero la novedad es ti, y el codigo se genera de la novedad por eso se le asigna a palabra)
        super(izq, der);
        palabra=Generador.nuevaTemp();
    }
    public void generarCTD(){
        if(izq!=null)
            ((Expresion)izq).generarCTD();
        if(der!=null)
            ((Expresion)der).generarCTD();
        //ahora genero codigo de esta expresion 
        Tipo t1=((Expresion)izq).getTipo();
        Tipo t2=((Expresion)der).getTipo();
        String pal1=((Expresion)izq).getPalabra();
        String pal2=((Expresion)der).getPalabra();

        if(t1.tipo().equals("int") && t2.tipo().equals("int")){
            Generador.asignacion(palabra,pal1+" / "+pal2);
            this.tipo=new Tipo("int");
        }else if(t1.tipo().equals("float") && t2.tipo().equals("float")){
            Generador.asignacion(palabra,pal1+" /r "+pal2);
            this.tipo=new Tipo("float");
        }else if(t1.tipo().equals("int") && t2.tipo().equals("float")){
             /*
             * En el caso de ser de distintos tipos (gana float) se crea una
             * temporal para convertir la de tipo int en tipo float por casting
             */
            String ti=Generador.nuevaTemp() ;
            Generador.asignacion(ti,"(float)"+pal1);
            Generador.asignacion(palabra,ti+" /r "+pal2);
            this.tipo=new Tipo("float");
        }else if(t1.tipo().equals("float") && t2.tipo().equals("int")){
            /*
             * En el caso de ser de distintos tipos (gana float) se crea una
             * temporal para convertir la de tipo int en tipo float por casting
             */
            String ti=Generador.nuevaTemp() ;
            Generador.asignacion(ti,"(float)"+pal2);
            Generador.asignacion(palabra,pal1+" /r "+ti);
            this.tipo=new Tipo("float");
        }else if(t1.tipo().equals("char") && t2.tipo().equals("char")){
            
            Generador.asignacion(palabra,pal1+" / "+pal2);
            this.tipo=new Tipo("int");
        }else if(t1.tipo().equals("int") && t2.tipo().equals("char")){
            
            Generador.asignacion(palabra,pal1+" / "+pal2);
            this.tipo=new Tipo("int");
        }else if(t1.tipo().equals("char") && t2.tipo().equals("int")){
            
            Generador.asignacion(palabra,pal1+" / "+pal2);
            this.tipo=new Tipo("int");
        }
    }
    
}
