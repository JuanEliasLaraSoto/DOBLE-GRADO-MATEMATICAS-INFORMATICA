import java_cup.runtime.*;

%%

%int
%cup
%xstate STRING
%xstate UNICODE

%{
    StringBuffer str = new StringBuffer();
%}
%%

<YYINITIAL>{
// Funciones del lenguaje
[0-9]+"."[0-9]+(E[+-][0-9]+)?  { return new Symbol(sym.NUMERO_REAL, yytext()); }
[0-9]+            { return new Symbol(sym.NUMERO_ENTERO, yytext()); }

"if"        { return new Symbol(sym.IF);    }
"else"      { return new Symbol(sym.ELSE);  }
"do"        { return new Symbol(sym.DO);    }
"while"     { return new Symbol(sym.WHILE); }
"for"       { return new Symbol(sym.FOR);   }
"print"     { return new Symbol(sym.PRINT); }
"length"     { return new Symbol(sym.LENGTH); }
"case" {return new Symbol(sym.CASE);}
"switch" {return new Symbol(sym.SWITCH);}
"break" {return new Symbol(sym.BREAK);}
"default" {return new Symbol(sym.DEFAULT);}

// Aperturas y cierres
","        { return new Symbol(sym.COMA);    }
"("         { return new Symbol(sym.AP);    }
")"         { return new Symbol(sym.CP);    }

"["         { return new Symbol(sym.AC);    }
"]"         { return new Symbol(sym.CC);    }

"{"         { return new Symbol(sym.ALL);    }
"}"         { return new Symbol(sym.CLL);    }
"?"         { return new Symbol(sym.INTERROGACION);    }
":"         { return new Symbol(sym.DOSPUNTOS);    }
// Operadores lógicos
"=="        { return new Symbol(sym.EQ);    }
"!="        { return new Symbol(sym.NE);    }
"<="        { return new Symbol(sym.LE);    }
"<"         { return new Symbol(sym.LT);    }
">="        { return new Symbol(sym.GE);    }
">"         { return new Symbol(sym.GT);    }
"?:" {return new Symbol(sym.ELVIS);}

"&&"        { return new Symbol(sym.AND);   }
"||"        { return new Symbol(sym.OR);    }
"!"         { return new Symbol(sym.NOT);    }


// Operadores matemáticos
"++"         { return new Symbol(sym.MASMAS);   }
"+"         { return new Symbol(sym.MAS);   }
"--"         { return new Symbol(sym.MENOSMENOS);   }

"-"         { return new Symbol(sym.MENOS);   }
"*"         { return new Symbol(sym.POR);   }
"/"         { return new Symbol(sym.DIV);   }
"%"         { return new Symbol(sym.PORCENT);    }

"="         { return new Symbol(sym.ASIG); }


// Fin de sentencia
";"         { return new Symbol(sym.PYC);   }
"."         { return new Symbol(sym.PUNTO);   }

// Valores
"int"                    { return new Symbol(sym.INTEGER); }
"string"                    { return new Symbol(sym.ESTRING); }

// Números flotantes
"float"     { return new Symbol(sym.FLOAT); }
"char" { return new Symbol(sym.CHAR);}
[_a-zA-Z][_a-zA-Z0-9]*  { return new Symbol(sym.IDENT, yytext()); }
\"                                                      { str.setLength(0); yybegin(STRING); }
\'                                                      { str.setLength(0); yybegin(STRING);}

// Para todo lo demás
[^]         { }
}

<STRING>{
    \"                                                  { yybegin(YYINITIAL); return new Symbol(sym.CADENA, str.toString()); }
    \'                                                  { yybegin(YYINITIAL); return new Symbol(sym.CARACTER, ((int) str.charAt(0))); } 
    [^\n\r\"\'\\]                                 { str.append(yytext()); }
    \\\"                                                { str.append('\"'); }
    \\\'                                                { str.append('\''); }
    \\                                                  { str.append('\\'); }
    \\\\                                                { str.append('\\'); }
    \\u                                                 { yybegin(UNICODE); }
}

<UNICODE>{

    [a-zA-Z0-9]{4}                                    { int code = Integer.parseInt(yytext(),16); str.append((char)code); yybegin(STRING); }

}