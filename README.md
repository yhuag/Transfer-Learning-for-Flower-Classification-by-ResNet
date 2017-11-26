# Transfer Learning for Flower Classification by Resnet

## Project Intro
Five categories of flowers' pictures are being trained by a CNN, based on ResNet and through transfer learning, to provide a classifier on flower categories. Flowers can be in the following categories: daisy, dandelion, roses, sunflowers or tulips. 

## File Structure
- Dataset: under `/flowers`, where you could find `/train` and `/val` for two collections of flowers' pictures for either training or validation.
- Indexing images: by running `image.py`, given *FILE_NAME* (`val.txt` or `train.txt`), a collection of flower images will be resized, renamed and reorganized into clear sets of training data or validation data.
- Training the dataset: by executing `cnn.py`, the model will be trained and validated. CUDA is enabled, so you could run it on your GPU as well.
- Detailed Explanation: for further illustrations on codes, please check the `transfer_learning.ipynb` notebook.

## Model Explanation
The model has 19 layers. 
The first 18 layers in based on pretrained 18 layers of ResNet. And an additional layer is added, as what transfer learning usually do, as the last layer to map the outputs into five categories of flowers, fully-connected. The loss is Cross Entropy Loss. And the Optimizer is SGD (Stochastic gradient descent), with momentum used. LR Scheduler is also in the play. CUDA can be enabled to support GPU training. You are also welcomes run the codes through jupyter notebook to see through steps. 