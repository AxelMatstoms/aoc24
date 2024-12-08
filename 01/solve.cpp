#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    std::vector<long> left{};
    std::vector<long> right{};
    while (true) {
        int l, r;
        std::cin >> l >> r;
        if (std::cin.eof())
            break;

        left.push_back(l);
        right.push_back(r);
    }

    // part 1
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    std::cout << std::inner_product(left.begin(), left.end(), right.begin(), 0L, std::plus{}, [](long l, long r) { return std::abs(l - r); }) << "\n";

    // part 2
    std::unordered_map<long, long> counts;
    std::for_each(right.begin(), right.end(), [&](long v){ counts[v]++; });
    std::cout << std::accumulate(left.begin(), left.end(), 0L, [&](long acc, long l) { return acc + l * counts[l]; }) << "\n";

    return 0;
}
