#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define rrep(i, n) for (ll i = n - 1; -1 < i; i--)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }


int main(){
    int H, W, K;
    cin >> H >> W >> K;
    vector<vector<int>> S(H, vector<int>(W)), G(H, vector<int>(W));
    rep(i, H) rep(j, W) cin >> S[i][j];
    rep(k, K) {
        rep(i, H) {
            rep(j, W) {
                if (i == 0) {
                    if (j == 0) G[i][j] = (S[i+1][j] + S[i][j+1]) % 2;
                    else if (j == W-1) G[i][j] = (S[i+1][j] + S[i][j-1]) % 2;
                    else G[i][j] = (S[i+1][j] + S[i][j+1] + S[i][j-1]) % 2;
                }
                else if (i == H-1) {
                    if (j == 0) G[i][j] = (S[i-1][j] + S[i][j+1]) % 2;
                    else if (j == W-1) G[i][j] = (S[i-1][j] + S[i][j-1]) % 2;
                    else G[i][j] = (S[i-1][j] + S[i][j+1] + S[i][j-1]) % 2;
                }
                else {
                    if (j == 0) G[i][j] = (S[i-1][j] + S[i][j+1] + S[i+1][j]) % 2;
                    else if (j == W-1) G[i][j] = (S[i-1][j] + S[i][j-1] + S[i+1][j]) % 2;
                    else G[i][j] = (S[i-1][j] + S[i][j+1] + S[i][j-1] + S[i+1][j]) % 2;
                }
            }
        }
        rep(i, H) rep(j, W) S[i][j] = G[i][j];
    }

    rep(i, H) {
        rep(j, W) {
            cout << S[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}