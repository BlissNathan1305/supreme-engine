
#include <iostream>

int main() {
    for (int i = 5; i <= 20; i++) {
        std::cout << "Multiplication table for " << i << ":\n";
        for (int j = 1; j <= 10; j++) {
            std::cout << i << " * " << j << " = " << i * j << std::endl;
        }
        std::cout << std::endl;
    }
    return 0;
