#include <iostream>
#include <string>
#include <map>
#include <Windows.h>
#include <unordered_map>

using namespace std;

int main() {
	int pos;
	string e;
	pos = 5;
	std::map<int, char> grid; // Creates grid
	for (int i = 0; i < 10; i = i + 1) {
		grid[i] = '.'; // Sets each second value of grid to .
	}
	grid[pos] = '#'; // Sets the position of the player to #
	while (true) {
		if ((GetKeyState('A') & 0x8000) && pos > 0) { // Checks if button is pressed and the player position is greater than zero
			grid[pos] = '.';
			pos = pos - 1;
			
		}
		else if ((GetKeyState('D') & 0x8000) && pos < 10) { // Checks if button is pressed and the player position is less than ten
			grid[pos] = '.';
			pos = pos + 1;
		}
		grid[pos] = '#';
		for (std::map<int, char>::iterator it = grid.begin(); it != grid.end(); ++it) // Runs for loop for length of grid
			std::cout << it->second; // Prints the second value of all of the grid values
		cout << endl;
	}

}