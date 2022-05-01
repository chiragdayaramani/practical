%{
int i;    
%}
%%
[0-9]+ {i=atoi(yytext);
        if (i%2==0)
        printf("EVEN");
        else
        printf("ODD");}
.   ;
%%
int yywrap(void){
    return 1;
}
int main(){
    yylex();
    return 0;
}