%{
int p = 0;
int s = 0;    
%}
%%
"printf"   {ECHO,p++;}
"scanf"    {ECHO,s++;}

%%
int yywrap(void){
    return 1;
}
int main(int argc,char *argv[]){
    FILE *fp;
    fp=fopen(argv[1],"r");
    yyin = fp;
    yylex();
    printf("Printf = %d,Scanf = %d",p,s);
    return 0;
}