// data_analysis.cpp
#include <iostream>
#include <cmath>

extern "C" {
    double compute_mean(double* data, int length) {
        double sum = 0.0;
        for (int i = 0; i < length; ++i) {
            sum += data[i];
        }
        return sum / length;
    }

    double compute_stddev(double* data, int length, double mean) {
        double sum = 0.0;
        for (int i = 0; i < length; ++i) {
            sum += (data[i] - mean) * (data[i] - mean);
        }
        return sqrt(sum / length);
    }
}
