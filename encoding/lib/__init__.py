import os
import torch
from torch.utils.cpp_extension import load

cwd = os.path.dirname(os.path.realpath(__file__))
cpu_path = os.path.join(cwd, 'cpu')
gpu_path = os.path.join(cwd, 'gpu')

cpu = torch.ops.load_library(os.oath.join(cpu_path, r"/home/tuongnh/Codes/PyTorch-Encoding-test/encoding/lib/cpu/enclib_cpu.so"))

if torch.cuda.is_available():
    gpu = torch.ops.load_library(os.oath.join(gpu_path, r"/home/tuongnh/Codes/PyTorch-Encoding-test/encoding/lib/gpu/enclib_gpu.so"))
