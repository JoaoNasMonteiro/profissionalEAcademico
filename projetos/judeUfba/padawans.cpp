#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
using namespace std;


struct jedi {
	string nome;
	int totalMissoes;
	int missoesFalhadas;
	int missoesCompletadas;
};

bool cmp(const jedi& a, const jedi& b) {
    return a.nome > b.nome;
}

int main(){
	vector<jedi> padawans;
	jedi padawan;
	int num;

	cin >> num;
	
	for(int i = 0; i < num; i++){
		cin >> padawan.nome >> padawan.totalMissoes >> padawan.missoesFalhadas;
		padawan.missoesCompletadas = padawan.totalMissoes - padawan.missoesFalhadas;
		padawans.push_back(padawan);
	}

	sort(padawans.begin(), padawans.end(), cmp);
	


}