#include <stdio.h>
int main()
{
    char s1[100], s2[100], m, n;
    scanf("%s", s1);
    scanf("%s", s2);
    for(m = 0; s1[m] != '\0'; ++m);
    for(n = 0; s2[n] != '\0'; ++n, ++m)
    {
        s1[m] = s2[n];
    }

    s1[m] = '\0';
    printf("%s", s1);
    return 0;
}
