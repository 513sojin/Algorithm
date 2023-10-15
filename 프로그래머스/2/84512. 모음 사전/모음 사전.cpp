#include <string>
#include <vector>

using namespace std;

vector<char> temp;
vector<char> alp = {'A', 'E', 'I', 'O', 'U'};
int num = 0;

int bfs(string word) {
    string tmp_word(temp.begin(), temp.end());
    if (word == tmp_word) {
        return num;
    }
    if (temp.size() == 5) {
        return -1;  // Equivalent to Python's "return"
    }

    for (char a : alp) {
        num++;
        temp.push_back(a);
        int result = bfs(word);
        if (result != -1) {
            return result;
        }
        temp.pop_back();
    }

    return -1;
}

int solution(string word) {
    int result = bfs(word);
    return result;
}
