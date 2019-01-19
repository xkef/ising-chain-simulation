#include <iostream>
using namespace std;

#include <array>
#include <math.h>
#include <vector>
#include <numeric>


double rng()
{

    const unsigned long c = 44485709377909;
    const unsigned long p = 281474976710655;
    static unsigned long x = 42;
    x = (c * x) % p;

    return x / double(p);
}
void Metropolis(vector<vector<bool> > & latt, const int n, vector<double> & expl, const int i)
{
    // seed value
    int x, y;
    int c0 = 0;
    double t = 0;
    vector<int> index(n + 1);
    iota(index.begin(), index.end(), 0);
    index[n] = 0;
    index.insert(index.begin(), n - 1);
    for (int j = 0; j < i; j++)
    {
        // Select site randomly

        x = rng() * n;
        y = rng() * n;

        //Calculate energy of the site
        c0 = 0;
        c0 += (latt[x][y] == latt[x][index[y + 2]])+ (latt[x][y] == latt[x][index[y]]);

        //cout << c0 << endl;

        if (x < n - 1)
        {
            c0 += (latt[x][y] == latt[x + 1][y]);
        }
        if (x > 0)
        {
            c0 += (latt[x][y] == latt[x - 1][y]);
        }

        //Flip according to Metropolis rules
        if (c0 < 3)
        {
            latt[x][y] = !latt[x][y];
        }

        else
        {

            t = rng();

            if (t < expl[c0])
            {

                latt[x][y] = !latt[x][y];
            }
        }
    }
}
int main()
{

    const int n = 400;
    double coeff = 2.26918;
    int av=100;

    vector<vector<bool> > latt(n, vector<bool>(n, 1));
    vector<double> expl(5, 0);

    expl[3] = exp(-4 / coeff);
    expl[4] = exp(-8 / coeff);
    for(int i=0; i<av; i++){
        cout << i << endl;
        Metropolis(latt,n,expl,200*n*n);
    }

    return 0;
}

