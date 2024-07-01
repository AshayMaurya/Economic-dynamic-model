// logistic_map.cpp
extern "C" {
    double logistic_map(double x, double r) {
        return r * x * (1 - x);
    }
}
