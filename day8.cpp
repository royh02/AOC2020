#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int signedOp(int, string);
int tryExec(vector<string>);

int main() 
{
  ifstream infile("./puzzle-inputs/day8.txt");
  string line;
  vector<string> inputs;
  while (getline(infile, line))
  {
    inputs.push_back(line);
  }
  for (int i = 0; i < inputs.size(); ++i)
  {
    string temp = inputs[i];
    if (inputs[i][0] == 'j')
    {
      inputs[i] = "nop " + inputs[i].substr(4); 
    }
    else if (inputs[i][0] == 'n')
    {
      inputs[i] = "jmp " + inputs[i].substr(4);
    }
    if (tryExec(inputs))
    {
      break;
    }
    else
    {
      inputs[i] = temp;
    }
  }
}

int signedOp(int a, string s)
{
  if (s[0] == '+')
  {
    return a + stoi(s.substr(1));
  }
  else if (s[0] == '-')
  {
    return a - stoi(s.substr(1));
  }
  else
  {
    throw invalid_argument("where is the sign??");
  }
}

int tryExec(vector<string> inputs) 
{
  int sum = 0;
  int pos = 0;
  vector<int> posHist;
  while (find(posHist.begin(), posHist.end(), pos) == posHist.end() and 
         pos < inputs.size())
  {
    cout << "pos:" << pos << "\nsum:" << sum << endl;
    posHist.push_back(pos);
    string action = inputs.at(pos).substr(0, 3);
    string dist = inputs.at(pos).substr(4);

    if (action == "acc")
    {
      sum = signedOp(sum, dist);
      ++pos;
    }
    else if (action == "jmp")
    {
      pos = signedOp(pos, dist);
    }
    // just nop now
    else
    {
      ++pos;
    }
  }
  cout << sum << endl;
  return pos == inputs.size();
}