#include<iostream>
using namespace std;
class sap{
    public:
    int x;
    string y="44";
};
int main(){
    sap obj;
    obj.x = 10;
    sap o =sap();
    cout<<o.y;
    return 0;
}