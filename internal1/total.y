%{
    #include <stdio.h>
    #include <ctype.h>
    #include <stdlib.h>
    int yylex();
    void yyerror(const char *s);
%}
%token NUMBER PLUS MINUS MUL DIV LPAREN RPAREN
%%
input : expr '\n'  {printf("Result: %d\n",$1);}
;
expr: expr PLUS term     {$$=$1+$3;}
| expr MINUS term   {$$=$1-$3;}
| term     {$$=$1;}
;
term : term  MUL  factor    {$$=$1*$3;}
| term DIV factor   {$$=$1/$3;}
| factor   {$$=$1;}
;
factor: NUMBER  {$$=$1;}
| LPAREN  expr  RPAREN    {$$=$2;}
;
%%
int main(){
    printf("enter3: ");
    yyparse();
    return 0;
}
void yyerror(const char *s){
    printf("error");
}