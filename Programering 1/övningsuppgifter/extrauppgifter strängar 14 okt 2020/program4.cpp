#include <iostream>
#include <string>
#include <cstdlib>
// INTE KLART
int kontrollSiffra(const std::string personNmr)
{
    int summa = 0;
    bool omvaxel = false;
    for (size_t i = 0; i < 9; i++)
    {
       //  output += personNmr[i];
//  	    output += personNmr[i] - '0';
    	    if (omvaxel)
	    {
		summa += personNmr[i] - '0';
	    }
	    else 
	    {
		if ((personNmr[i] - '0') * 2 >= 10)
		{
			for (size_t n = 0; n <= std::to_string((personNmr[i] - '0') * 2).length(); n++)
			{
				summa += std::to_string( (personNmr[i] - '0') * 2)[n] - '0';
			}
		}
		else 
		{
			summa += (personNmr[i] - '0') * 2;
		}


 	    }
	    omvaxel = !omvaxel;	    
    }
    return summa;
}

std::string formateraPersonNmr(std::string personNmr)
{
    std::string output;

    for (size_t i = 0; i < personNmr.length(); i++)
    {
        if (personNmr[i] != '-') 
            output += personNmr[i];
    }

    return output;
}

int main()
{

    std::string personNummer = "031110-3014";
    std::cout << kontrollSiffra(formateraPersonNmr(personNummer)) << std::endl; 
    int variabel = kontrollSiffra(formateraPersonNmr(personNummer));

    std::cout << "VARIABEL + KONTROLLSIFFRAI:" << std::endl; 	 
    
    std::cout << (variabel + (personNummer[9] - '0'))  << std::endl;

    return 0;
}
