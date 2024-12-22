#include <iostream>
#include <vector>

int main()
{
    std::vector<long> input;
    while (true) {
        long num;
        std::cin >> num;

        if (std::cin.eof())
            break;

        input.push_back(num);
    }

    long a {};
    long b {};

    std::vector<long> scores(19 * 19 * 19 * 19);
    std::vector<long> seen(19 * 19 * 19 * 19, -1);

    std::vector<long> suffix;
    for (long i = 0; i < input.size(); ++i) {
        long secret = input[i];
        long last = secret % 10;

        suffix.clear();

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

            suffix.push_back(delta + 9);
            if (suffix.size() > 4) {
                suffix.erase(suffix.begin());
            } else {
                continue;
            }

            long idx = 6859 * suffix[0] + 361 * suffix[1] + 19 * suffix[2] + suffix[3];
            if (seen[idx] < i) {
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
