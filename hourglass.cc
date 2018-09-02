#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int main(){
    int vec[6][6];
    int sum{0};
    int _max = INT_MIN;
    for (int i = 0; i < 6; ++i){
        for(int j = 0; j < 6; ++j){
            int element;
            cin >> element;
            vec[i][j] = element;
        }
    }

    for (int i = 0; i < 4; ++i){
        for(int j = 0; j < 4; ++j){
            sum = vec[i][j] + vec[i][j + 1] + vec[i][j + 2]
                + vec[i + 1][j + 1]
                + vec[i + 2][j] + vec[i + 2][j + 1] + vec[i + 2][j + 2];
            _max  = max(sum, _max);
        }
    }
    cout << _max;
}