#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> // Include for exit() and EXIT_FAILURE

int main() {
    char hostname[256]; // Buffer to hold the hostname
    if (gethostname(hostname, sizeof(hostname)) == 0) {
        printf("Hostname: %s\n", hostname);
    } else {
        perror("gethostname");
        exit(EXIT_FAILURE); // Use exit(EXIT_FAILURE) on error
    }
    return 0;
}
