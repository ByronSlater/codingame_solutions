#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

class Fraction
{
public:
  long numerator, denominator;
  
  Fraction(long n, long d)
  {
    numerator = n;
    denominator = d;
  }

  Fraction simplify()
  {
    if(denominator % numerator != 0)
    {
      return Fraction(numerator, denominator);
    }
    else
    {
      return Fraction(1, denominator / numerator);
    }
  }

  friend bool operator== (Fraction& f1, Fraction& f2)
  {
    return f1.numerator == f2.numerator && f1.denominator == f2.denominator;
  }

  friend ostream& operator<< (ostream& os, const Fraction& f)
  {
    os << f.numerator << "/" << f.denominator;
    return os;
  }

  vector<pair<Fraction, Fraction>> getEquivalents()
  {
    vector<pair<Fraction, Fraction>> result;

    long min, max;

    min = denominator + 1;
    max = denominator * 2;

    for(long i = min; i <= max; ++i)
    {
      Fraction toTest = Fraction(1, i);
      Fraction diff = this->minus(toTest).simplify();

      if(diff.numerator == 1)
      {
        result.push_back({diff, toTest});
      }
    }

    return result;
  }

  Fraction minus(const Fraction& f)
  {
    return Fraction(numerator * f.denominator - denominator * f.numerator, denominator * f.denominator);
  }
};

int main()
{
  long denominator;

  cin >> denominator; cin.ignore();

  auto fracToTest = Fraction(1, denominator);
  auto equivs = fracToTest.getEquivalents();


  for(auto p : equivs)
  {
    cout << fracToTest << " = " << p.first << " + " << p.second << endl;
  }
}

