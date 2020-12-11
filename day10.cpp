#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int recursiveCombo(vector<int>, int);

int main()
{
  ifstream infile("./puzzle-inputs/day10.txt");
  string line;
  vector<int> inputs(1);
  while (getline(infile, line))
  {
    inputs.push_back(stoi(line));
  }
  sort(inputs.begin(), inputs.end());
  inputs.push_back(inputs.back() + 3);

  // PART 1 ----- joltage diff counters
  int ones, threes;

  for (int i = 0; i < inputs.size() - 1; ++i)
  {
    if (inputs[i+1] - inputs[i] == 1) { ++ones; }
    else if (inputs[i+1] - inputs[i] == 3) { ++threes; }
  }

  // part 1 cout
  cout << ones * threes << endl;

  // PART 2 ----- Count diff arrangements of adaptors
  vector<long int> arr = {1};
  for (int i = 1; i < inputs.size(); ++i)
  {
    int j = i - 1;
    long int combo = arr[j];
    while (--j >= 0 && inputs[i] - inputs[j] <= 3)
    {
      combo += arr[j];
    }
    arr.push_back(combo);
  }

  // part 2 cout
  cout << arr.back() << endl;

  return 0;
}