%{
int v = 0;
int c = 0;
%}
%%
[a|e|i|o|u|A|E|I|O|U]   {v++;}
[a-zA-Z]  {c++;}
.    ;
%%
int yywrap(void){
    return 1;
}
int main(){
    yylex();
    printf("Vowels = %d, Consonants = %d",v,c);
    return 0;
}