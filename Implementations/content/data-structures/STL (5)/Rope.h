/**
 * Description: insert element at $i$-th position,
	* cut a substring and re-insert somewhere else
 * Time: O(\log N) per operation? not well tested
 * Source: https://codeforces.com/blog/entry/10355
 * Verification: CEOI 2018 Day 2 Triangles
 */

#include <ext/rope>
using namespace __gnu_cxx;
void ropeExample() {
	rope<int> v(5, 0); // initialize with 5 zeroes
	F0R(i,sz(v)) v.mutable_reference_at(i) = i+1; 
	F0R(i,5) v.pb(i+1); // constant time pb
	rope<int> cur = v.substr(1,2); 
	v.erase(1,3); // erase 3 elements starting from 1st element
	for (rope<int>::iterator it = v.mutable_begin(); 
		it != v.mutable_end(); ++it)
		cout << *it << " ";  
	cout << "\n"; // 1 5 1 2 3 4 5
	v.insert(v.mutable_begin()+2,cur); // index or const_iterator
	v += cur;
	F0R(i,sz(v)) cout << v[i] << " ";  
	cout << "\n"; // 1 5 2 3 1 2 3 4 5 2 3
}
