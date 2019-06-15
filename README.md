# Final Project

Lihang Gong, lgong@ucsd.edu\
Di Gu, dgu@ucsd.edu

## Abstract Proposal

There are countless black&white manga available. However, few of them are colorized as it spends much additional time for comic book creators to paint from the black&white version. What if we have an auto painter that convert b&w manga into colorized ones? In project 4, a manga colorization solution was developed based on pix2pix model. It was able to colorize b&w manga pages based on some colorized samples. However the synthetic color was sometimes unnature. For final project, we will try to refine the results and make them more natural. Also, we will try some style transfer during colorization. Colored image genearted from model will be presented in the final presentation.

## Project Report

[Report](Report.pdf)

## Model/Data

Files that are included in repository:
- datasets/: includes all the train/test/validation images
- checkpoints can be downloaded at [GoogleDrive](https://drive.google.com/drive/folders/1m5wf2Fb_9XDbyAkBhNHY2E4LMIoEuDrn?usp=sharing)

## Code

- data/: scripts that play with datasets
- models/: contains several models but only pix2pix is used
- scripts/ and util/: auxiliary files

- Guide to repeat this project: colorization.ipynb
- test.py and train.py: for customized use 

## Results

Several result pages is included in result/

## Technical Notes

- Requirements are included in colorization.ipynb
- Tested on Datahub

## Reference

- [pix2pix paper](https://arxiv.org/pdf/1611.07004.pdf)
- [Pytorch implementation of pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

