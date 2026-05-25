%{
    #include <stdio.h>
%}
%%
0[0-7]+      {printf("octal");}
0[xX][0-9a-fA-F]+     {printf("hexadecimal");}
. | \n       {    }
%%
int main(){
    printf("enter exp: ");
    yylex();
    return 0;
}
int yywrap(){
    return 1;
}