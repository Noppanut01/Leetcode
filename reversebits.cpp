#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  int reverseBits(int n) {
    int digit = 32;
    int q = 0;
    int r = 0;
    int result = 0;
    vector<int> temp;
    while (n > 0) {
        q = n / 2;
        r = n % 2;
        n = q;
        temp.push_back(r);
    }

    reverse(temp.begin(), temp.end());
    vector<int> bits(digit - temp.size(), 0);
    bits.insert(bits.end(), temp.begin(), temp.end());

    for (int i = bits.size() - 1; i >= 0; i--){
        result = (result << 1) | bits[i];
    }
    return result;
  }
};
