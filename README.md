# Custom PyTorch C++ Operator using pybind11

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=flat&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)
![pybind11](https://img.shields.io/badge/pybind11-binding-blueviolet.svg)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)

This project demonstrates how to build a custom high-performance C++ operator and expose it to Python using **pybind11** and **PyTorch C++ extensions**.

It shows the full pipeline:

> Python → PyTorch Tensor → C++ computation → Python result

---

## 📦 Project Structure

```text
my_custom_op/
├── custom_op.cpp
├── setup.py
└── test.py
```

---

## ⚙️ Requirements

### Python packages

```bash
pip install torch pybind11 setuptools
```

* **PyTorch** → provides tensor system and extension API
* **pybind11** → binds C++ functions to Python
* **setuptools** → builds C++ extension module

### System requirements (Windows)

Install **Visual Studio Build Tools**:

* **Workload**: ✔ Desktop development with C++
* **Components**:
  * MSVC v143 compiler
  * Windows 10/11 SDK

#### Why MSVC is required

PyTorch C++ extensions on Windows require the **Microsoft Visual C++ compiler (`cl.exe`)**. This is used to compile `custom_op.cpp` into a Python-loadable binary.

---

## 🧾 Files Explanation

### 1. `custom_op.cpp`
Contains the C++ implementation. It:
* Defines a tensor operation: `y = x * x + 2`
* Uses the PyTorch C++ API (`torch::Tensor`)
* Exposes the function using pybind11

### 2. `setup.py`
Build script that:
* Compiles C++ code
* Links against PyTorch libraries
* Creates a Python extension module

It uses:
```python
from torch.utils.cpp_extension import CppExtension, BuildExtension
```

### 3. `test.py`
Python test script that:
* Imports the compiled module
* Passes a PyTorch tensor
* Prints the result

---

## 🚀 Build & Run Commands

**Step 1:** Open MSVC environment
Open: **x64 Native Tools Command Prompt for VS**

**Step 2:** Enable build environment variables
```cmd
set DISTUTILS_USE_SDK=1
set MSSdk=1
```

**Step 3:** Build extension
```cmd
python setup.py build_ext --inplace
```
*What this does:*
* Compiles `custom_op.cpp`
* Uses MSVC (`cl.exe`)
* Links with PyTorch libraries
* Generates `.pyd` binary module

**Step 4:** Run test
```bash
python test.py
```

### 🧪 Output
```text
tensor([ 3.,  6., 11.])
```

---

## 🏗️ System Architecture

```text
                +----------------------+
                |   Python (test.py)   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   PyTorch Tensor     |
                | (input data flow)    |
                +----------+-----------+
                           |
                           v
        +--------------------------------------+
        |  pybind11 Binding Layer              |
        |  (Python ↔ C++ interface)            |
        +----------------+---------------------+
                         |
                         v
        +--------------------------------------+
        |   C++ Extension (custom_op.cpp)      |
        |   High-performance computation       |
        +----------------+---------------------+
                         |
                         v
        +--------------------------------------+
        |  Compiled Binary (.pyd / .so)        |
        |  Built using MSVC compiler           |
        +--------------------------------------+
```

### Why this architecture is powerful
* **Python** handles orchestration (easy development)
* **C++** handles compute-heavy operations (speed)
* **PyTorch** provides tensor backend (ML support)
* **pybind11** connects both worlds (binding layer)

## Key Concepts Learned
* Building native Python extensions
* Using MSVC compiler on Windows
* Integrating C++ with PyTorch
* Writing high-performance tensor operations
* Understanding Python ↔ C++ interoperability

## Use cases of this pattern
* Custom PyTorch operations
* Deep learning optimizations
* GPU kernel extensions (CUDA version)
* High-performance scientific computing
* Production ML inference engines

---

This project demonstrates how to extend Python with fast C++ code using PyTorch’s extension system and pybind11 bindings. It is a foundational pattern used in real-world ML frameworks and research systems.

