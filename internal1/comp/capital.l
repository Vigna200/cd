%{
#include <stdio.h>
#include <ctype.h>
int newword = 1;
%}
%%
[ \t\n]   { putchar(yytext[0]); newword = 1; }
[a-zA-Z]
{
if(newword)
{
putchar(toupper(yytext[0]));
newword = 0;
}
else
putchar(yytext[0]);
}
.   { putchar(yytext[0]); newword = 0; }
%%
int main()
{
printf("Enter text:\n");
yylex();
return 0;
}
int yywrap()
{
return 1;
}
