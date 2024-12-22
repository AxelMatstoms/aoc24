#include <ios>
#include <iostream>
#include <vector>

int main()
{
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    long a {};
    long b {};

    std::vector<long> scores(19 * 19 * 19 * 19);
    std::vector<long> seen(19 * 19 * 19 * 19, -1);

    long secret;
    long i = -1;
    while (++i, std::cin >> secret) {
        long last = secret % 10;

        long idx {};

        for (int k = 0; k < 2000; ++k) {
            secret ^= secret << 6;
            secret &= 0xffffff;

            secret ^= secret >> 5;
            secret &= 0xffffff;

            secret ^= secret << 11;
            secret &= 0xffffff;

            long digit = secret % 10;
            long delta = digit - last;
            last = digit;

            idx *= 19;
            idx += delta + 9;
            idx %= 130321;
            if (k >= 4 && seen[idx] < i) {
                scores[idx] += digit;
                seen[idx] = i;
                b = std::max(b, scores[idx]);
            }
        }

        a += secret;
    }

    std::cout << a << "\n";
    std::cout << b << "\n";
}
