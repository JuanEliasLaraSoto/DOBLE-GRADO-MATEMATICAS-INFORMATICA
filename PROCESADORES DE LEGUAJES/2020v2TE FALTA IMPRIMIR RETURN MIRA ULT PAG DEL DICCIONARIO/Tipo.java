public class Tipo {
    private String tipo;
    private String subtipo;
    protected Integer longitud;

    public static final String INT="int";
    public static final String FLOAT="float";
    public static final String CHAR="char";
    public static final String ARRAYUNIDIM="arrayunidim";
    public static final String STRING="string";
    public static final String VOID="void";
    public static final String FUNCION="funcion";


    public Tipo(String tipo){
        this.tipo=tipo;
    }
    public Tipo(String tipo,String subtipo,Integer longitud){
        this.subtipo=subtipo;
        this.tipo=tipo;
        this.longitud=longitud;
    }
    public Tipo(String tipo,String subtipo){
        this.subtipo=subtipo;
        this.tipo=tipo;
    }
    public String getTipo(){
        return this.tipo;
    }
   public void setTipo(String tipo){
        this.tipo=tipo;
    }
    public boolean equals(Object obj){
        if(obj instanceof Tipo){
            Tipo t=(Tipo)obj;
            return this.tipo.equals(t.tipo);
        }
        return false;
    }
    public String tipo(){
        return this.tipo;
    }
    public String getSubtipo(){
        return this.subtipo;
    }
   public void setSubtipo(String subtipo){
        this.subtipo=subtipo;
    }
    public boolean subtipo(Object obj){
        if(obj instanceof Tipo){
            Tipo t=(Tipo)obj;
            return this.subtipo.equals(t.subtipo);
        }
        return false;
    }
    public String subtipo(){
        return this.subtipo;
    }
   public Integer getLongitud(){
    return this.longitud;
   }

    @Override
    public String toString() {
        return "Tipo("+tipo+")";
    }
    
}
