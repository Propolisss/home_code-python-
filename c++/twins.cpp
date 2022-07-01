#include <iostream>
#include <math.h>

int simple(int n)
{
	for (int i = 3; i < sqrt(n) + 1; i += 2)
	{
		if (n % i == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int num, numm, count = 0, sr;
	for (int i = 500001; i < 1666666 + 1; i++)
	{
		num = 6 * i - 1;
		numm = 6 * i + 1;
		if (simple(num) && simple(numm))
		{
			count++;
			sr = (num + numm) / 2;
		}
	}
	std::cout << count << ' ' << sr << std::endl;
	return 0;
}