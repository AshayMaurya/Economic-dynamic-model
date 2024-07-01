// graphic_processing.cpp
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>

// Function to save logistic map data to a file for external visualization tools
extern "C" {
    void save_logistic_map_data(const char* filename, double* data, int length) {
        std::ofstream file(filename);
        if (file.is_open()) {
            for (int i = 0; i < length; ++i) {
                file << i << "," << data[i] << "\n";
            }
            file.close();
        }
    }
}
