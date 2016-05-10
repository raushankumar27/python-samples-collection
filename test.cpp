#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	int n, m, u, v, i, j;
	long s;
	char S[2];
	std::scanf("%d %d", &n, &m);
	vector<int> P(n+1);
	vector<int> E(n+1);
	for(i=1; i<=n; ++i)
		scanf("%d", &E[i]);
	P[1] = 1;
	for(i=0; i<n-1; ++i)
	{
		scanf("%d %d", &u, &v);
		P[v] = u;
	}
	vector< vector<int> >A(n+1);
	for(i=1; i<=n; ++i)
		A[i].push_back(i);
	for(i=2; i<=n; ++i)
		for(j = i; j!=1; j = P[j])
			A[P[j]].push_back(i);
	
	while(m--)
	{
		scanf("%s", S);
		switch(S[0])
		{
			case 'Q':	cin>>u;
						for(s=j=0; j<A[u].size(); ++j)
							s+=E[A[u][j]];
						cout<<s<<endl;
						break;
			case 'U':	cin>>u>>v;
						E[u] = v;
						break;
		}
	}
	return 0;
}