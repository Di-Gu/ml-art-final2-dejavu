# Final Project

Lihang Gong, lgong@ucsd.edu\
Di Gu, dgu@ucsd.edu

## Abstract Proposal

There are much more monocolor mangas available than colorized version, as mass production is required to fill all the color. Most of them are repetitive works since these mangas follow the same pattern. How to automatically paint the sketch into the color fit their style is a useful application to reduce their workload and can help ordinary people to generate the artist style they like on their own sketch.In this project, we are interested in solving this by employing deep neural networks and applying other existing techniques. 

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
- test.py and train.py: for customized useage 

## Results

See details in results/

## Technical Notes

- Requirements are included in colorization.ipynb
- Tested on Datahub

## Reference

- [pix2pix paper](https://arxiv.org/pdf/1611.07004.pdf)
- [Pytorch implementation of pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

