
public class FORALLINTSTEP extends Expresion {
    String id,n1,n2,n3;
    public FORALLINTSTEP (String id, String n1,String n2,String n3,AST sent){
        super(null,sent);
        this.id=id;
        this.n1=n1;
        this.n2=n2;
        this.n3=n3;
        palabra=Generador.nuevaTemp();
        tipo=new Tipo(Tipo.BOOLEAN);

    }
    public void generarCTD(){
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String v2=Generador.nuevaLabel();
        String f2=Generador.nuevaLabel();
        String todobien=Generador.nuevaLabel();
        String aux=Generador.nuevaLabel();
String valororiginalid=Generador.nuevaTemp();
String resultado=Generador.nuevaTemp();

Generador.asignacion(resultado, "1");
        Generador.asignacion(valororiginalid, id);
        Generador.asignacion(id, n1);
        Generador.etiq(aux);
        Generador.comparacion(id,"<=", n2, new DosEtiq(v,f));
        Generador.etiq(v);
        if(der!=null){
            der.generarCTD();
        }

        Generador.comparacion("0","<",((Expresion)der).getPalabra(),new DosEtiq(v2,f2) );
        Generador.etiq(v2);
        Generador.salto(todobien);
        Generador.etiq(f2);
        Generador.asignacion(resultado, "0");
        Generador.salto(f);

        Generador.etiq(todobien);
        Generador.asignacion(id,id+" + "+n3);
        Generador.salto(aux);
        Generador.etiq(f);
        Generador.asignacion(palabra, resultado);
    }
    
}
