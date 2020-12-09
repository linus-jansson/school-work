// Kompilera med g++: g++ -std=c++11 program.cpp -o program.exe

#include <iostream>
#include <string>

double f(double x) {
    // x^3 + 2x +5
    return (x*x*x) + (2.0*x) + 5.0;
}

double primaX(double a, double h) {
    return ( f(a + h) - f(a) ) / h;
}

int main()
{   

    int a = 4.0;
    float h = 1.0f;

    for (int i = 0; i <= 10; i++) {
        h /= 10.0;
        std::cout << "f'(4) = " << std::to_string( primaX(a, h) ) << std::endl;

    }

    return 0;
}