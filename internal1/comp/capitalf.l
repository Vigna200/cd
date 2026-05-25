#-----------------------------------------capitalize an entire string---
%{
#include <stdio.h>
#include <ctype.h>
%}
%%
[a-z]      { putchar(toupper(yytext[0])); }   /* convert lowercase to uppercase */
[A-Z]      { putchar(yytext[0]); }            /* keep uppercase as it is */
\n         { putchar('\n'); }                 /* print newline */
.          { putchar(yytext[0]); }            /* print other characters */
%%
int main()
{
printf("Enter a string:\n");
yylex();
return 0;
}

int yywrap()
{
return 1;
}
