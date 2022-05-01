%{
int count_k=0,count_i=0,count_o=0;
%}
%%
"printf"|"scanf"|"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while" {count_k++;printf("\nkeywords : %s", yytext);}
[a-zA-Z_]+[a-zA-Z0-9_]* {count_i++;printf("\nidentifier : %s", yytext);}
"<="|"=="|"="|"++"|"-"|"*"|"+" {count_o++;printf("\noperator : %s", yytext);}
. ;
%%
int yywrap()
{
return 1;
}
int main(int argc, char *argv[])
{
FILE *fp;
fp=fopen(argv[1],"r");
yyin=fp;
yylex();
fclose(fp);
printf("\nNo of Keywords = %d",count_k);
printf("\nNo of Identifire = %d",count_i);
printf("\nNo of Operator = %d",count_o);
return 0;
}