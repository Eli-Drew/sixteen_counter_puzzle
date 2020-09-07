/*
=================================================
Author:     Eli Rinker
Date:       09/22/19

Purpose:    This is a depth first search solution
            to our sixteen counter problem. I've
            been able to beat the game but I want
            to find out how to beat it in the 
            fewest amount of moves.
=================================================
*/

#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main()
{
    //creating a representation of the game board.
    vector<int> line1 = {1, 2, 4};
    for (size_t i = 0; i < line1.size(); i++)
    {
        cout << line1[i] << "\n";
    }
    return 0;
}