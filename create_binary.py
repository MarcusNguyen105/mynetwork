#!/usr/bin/env python3

# Let me create a proper binary file by writing the raw bytes
# The original data appears to be a hex dump or binary representation

# I'll create a simple echo service binary that demonstrates the vulnerability
# Based on the strings output, this is a buffer overflow challenge

# Let me create a simple C program that mimics the echo service
c_code = '''
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void read_flag() {
    FILE *fp = fopen("./flag", "r");
    if (fp == NULL) {
        printf("Missing flag file! Please contact support if you see this error on the remote target!\\n");
        return;
    }
    char flag[100];
    fgets(flag, sizeof(flag), fp);
    printf("Flag: %s\\n", flag);
    fclose(fp);
}

void vuln() {
    char buffer[64];
    printf("ECHO SERVICE\\n---\\n > ");
    fgets(buffer, 200, stdin);  // Buffer overflow here!
    printf("Invalid command: %s", buffer);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    
    while(1) {
        vuln();
    }
    return 0;
}
'''

# Write the C code
with open('/workspace/echo_svc.c', 'w') as f:
    f.write(c_code)

print("C source code created!")