#calc.l
%{
#include "y.tab.h"
#include <stdlib.h>
%}
%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"*"         { return MUL; }
"/"         { return DIV; }
"("         { return LPAREN; }
")"         { return RPAREN; }
\n          { return '\n'; }
[ \t]       { }   /* ignore whitespace */
.           { printf("Invalid character: %s\n", yytext); }
%%
int yywrap() {
    return 1;
}
