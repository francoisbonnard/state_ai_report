## Vérifie si CUDA est détecté

```py
import torch
print(torch.version.cuda)  # None
print(torch.cuda.is_available()) #  False

```

Si torch.cuda.is_available() retourne False, PyTorch ne détecte pas CUDA, et il faut réinstaller PyTorch avec le support CUDA activé.

pip install torch --index-url https://download.pytorch.org/whl/cu118

## check cuda version 

    nvidia-smi

+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 552.22                 Driver Version: 552.22         CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------|
| GPU  Name                     TCC/WDDM  | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        | MIG M.               |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...  WDDM  |   00000000:01:00.0 Off |               N/A    |
| N/A   39C    P8              5W /   55W |       0MiB /   8188MiB |      0%      Default |
|                                         |                        |               N/A    |

##  install Torch with 12.4 cuda version 

poetry add torch@https://download.pytorch.org/whl/cu121/torch-2.0.1+cu121-cp311-cp311-win_amd64.whl

poetry remove torch (version 2.5.1)
poetry add torch@2.0.1
