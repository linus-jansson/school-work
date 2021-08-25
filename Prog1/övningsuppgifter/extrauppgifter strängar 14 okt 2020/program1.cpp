#include <iostream>
#include <string>

std::string removeBlankSpace(std::string input){
    std::string output;

    for (size_t i = 0; i <= input.length(); i++)
    {
       if (input[i] != ' ') output += input[i];
    }


    return output;

}

int count(std::string text, char letter)
{
    int count = 0;


    for (size_t i = 0; i < text.length(); i++)
    {
       if (text[i] == letter) count++;

    }

    return count;
}

int main()
{

    bool anagram = false;

    std::string text1, text2, text1new, text2new;

    // Tar in mening eller ord från användaren och sätter det till text 1 och 2
    std::cout << "Write a word or a scentence\n";
    std::getline(std::cin, text1);

    std::cout << "Write another word or a scentence\n";
    std::getline(std::cin, text2);

    // Tar bort alla blanksteg från texterna och sätter resultatet till nya variabler
    text1new = removeBlankSpace(text1);
    text2new = removeBlankSpace(text2);

    // Jämför om antalet bokstäver är lika i båda texterna
    for (size_t i = 0; i < text1new.length(); i++)
    {
        if (count(text1new, text1new[i]) == count(text2new, text1new[i]))
        {
            anagram = true;
        }
        else {
            anagram = false;
            break;
        }
    }

    if (anagram)
    {
        std::cout << text1 << " is possible to be made into " << text2;
    }
    else
    {
        std::cout << text1 << " is not possible to be made into " << text2;
    }


    return 0;
}