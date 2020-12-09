// g++ -std=c++11 program3.cpp -o p3.exe

#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> split(std::string input, char deliminator = ' ')
{
    bool vaxel;
    std::string part;
    std::vector<std::string> output;

    // För varje tecken så ska den lägga i olika ord. 
    // Men om input[i] är lika med deliminator så ska den växla till nästa
    for (int i = 0; i <= input.length(); i++)
    {
        
        if (input[i] != deliminator)
                part += input[i];
        else
        {
            output.push_back(part);
            part.clear();
        }
    }
    
    output.push_back(part);

    // Returnera vectorn
    return output;
} 

int main()
{
    std::string tid = "12:55";
    std::string tid1, tid2;

    std::cout << "Write in a time in the format hh:mm > ";
    std::cin >> tid1;

    std::cout << "\nWrite in another time in the format hh:mm > ";
    std::cin >> tid2;

    std::vector<std::string> uppDeladTid1 = split(tid1, ':');
    std::vector<std::string> uppDeladTid2 = split(tid2, ':');

    int tidDiff = ( (std::stoi(uppDeladTid2[0]) * 60) - (std::stoi(uppDeladTid1[0]) * 60))  + ( std::stoi(uppDeladTid2[1]) - std::stoi(uppDeladTid1[1]) );

    if (tidDiff < 0)
            tidDiff += 24*60;

    std::cout << tidDiff << std::endl;

    

}

