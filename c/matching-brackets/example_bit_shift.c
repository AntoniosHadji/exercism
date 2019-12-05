#include <stdbool.h>

#define OPEN(b,n) case b : x <<= 2; x |= n; break
#define CLOSE(b,n) case b : if ((x&3) == n) {x >>= 2; break;} return 0

bool is_paired(const char * t) {
    unsigned long long x = 0;
    while (*t) switch(*t++) {
        OPEN('[',1); CLOSE(']',1);
        OPEN('{',2); CLOSE('}',2);
        OPEN('(',3); CLOSE(')',3);
        default : ;
    }
    return !x;
}

#undef OPEN
#undef CLOSE


// bool is_paired(const char * t) {
//     unsigned long long x = 0;
//     while (*t) switch(*t++) {
//         OPEN('[',1);
//         case b :
//           x <<= 2;
//           x |= n;
//           break;
//         CLOSE(']',1);
//         case b :
//           if ((x&3) == n) {
//           x >>= 2;
//           break;
//           }
//           return 0;
//         OPEN('{',2);
//         CLOSE('}',2);
//         OPEN('(',3);
//         CLOSE(')',3);
//         default : ;
//     }
//     return !x;
// }
