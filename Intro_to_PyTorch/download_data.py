import torch
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
# Use standard FashionMNIST dataset
train = datasets.MNIST(
    root = './data/MNIST',
    train = True,
    download = True,
    transform = transforms.Compose([
        transforms.ToTensor()
    ])
)
test = datasets.MNIST(root = './data/MNIST', train=False, download=True,
                       transform=transforms.Compose([transforms.ToTensor()]))
