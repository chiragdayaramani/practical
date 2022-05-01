%{
int w = 0;
int c = 0;
int l = 1;    
%}
%%
\n {l++;}
[^ \n\t]+  {w++, c=c+yyleng;}
.  {c++;}
%%
int yywrap(void){
    return 1;
}
int main(){
    FILE *fp;
    fp = fopen(argv[1],"r");
    yyin = fp;
    yylex();
    printf("Words = %d,Characters = %d,Lines = %d",w,c,l);
    return 0;
}