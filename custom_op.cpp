#include <torch/extension.h>

// Simple operation: y = x^2 + 2
torch::Tensor my_op(torch::Tensor x) {
    return x * x + 2;
}

// Binding code
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("my_op", &my_op, "My custom operation");
}