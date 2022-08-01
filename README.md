## For Learning YOLOv5 Only, not recommend to use this in game.


### Get Start
1) Install 
   - CUDA 11.7
    `https://developer.nvidia.com/cuda-downloads`
    - Conda (Anaconda/Miniconda)
       - Anaconda `https://www.anaconda.com/products/distribution`
       - Miniconda `https://docs.conda.io/en/latest/miniconda.html`

2) Create and activate a conda virtual environment:
    ```
    conda create -n csgo-yolov5 python=3.9.12 -y
    conda activate csgo-yolov5
    ```
3) Install PyTorch and torchvision (CUDA is required):
    `conda install pytorch==1.12.0 torchvision==0.13.0 cudatoolkit=11.6 -c pytorch`

4) Install required libraries
    `pip install to-requirements.txt`

5) Star this project and raise an issue for getting the trained model
   
6) Put the model in the correct path and run:
   `python main.py`
