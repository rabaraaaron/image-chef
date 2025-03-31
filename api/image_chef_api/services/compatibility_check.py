import torch
import subprocess
import platform


def get_gpu_memory_nvidia_smi():
    """
    Use nvidia-smi to get more accurate GPU memory information
    Works on Windows and Linux
    """
    try:
        if platform.system() == "Windows":
            # For Windows, use full path to nvidia-smi
            cmd = '"C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe"'
        else:
            cmd = "nvidia-smi"

        output = subprocess.check_output(
            [cmd, "--query-gpu=memory.total,memory.used", "--format=csv,nounits,noheader"])
        output = output.decode('utf-8').strip().split('\n')[0].split(', ')
        return {
            "total_memory": float(output[0]),
            "used_memory": float(output[1])
        }
    except Exception as e:
        print(f"Error using nvidia-smi: {e}")
        return None


def detailed_gpu_memory_check():
    # PyTorch CUDA Memory Check
    print("=== PyTorch CUDA Memory Check ===")
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        props = torch.cuda.get_device_properties(device)
        print(
            f"PyTorch Reported Total Memory: {props.total_memory / 1e9:.2f} GB")
        print(
            f"Allocated Memory: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
        print(f"Cached Memory: {torch.cuda.memory_reserved() / 1e9:.2f} GB")

    # nvidia-smi Check
    print("\n=== nvidia-smi Memory Check ===")
    nvidia_smi_info = get_gpu_memory_nvidia_smi()
    if nvidia_smi_info:
        print(f"Total Memory: {nvidia_smi_info['total_memory']} MB")
        print(f"Used Memory: {nvidia_smi_info['used_memory']} MB")

    # Additional diagnostic information
    print("\n=== Additional Diagnostics ===")
    print(f"CUDA Device Name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Device Capability: {torch.cuda.get_device_capability(0)}")
