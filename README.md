# Densepose2Texture

This is a Densepose to Texture model from Runway.

It takes an input UV image and a Texture image, returns an image with texture poses.
<img src="imgs/input.png" alt="input" title="input" width="200" /> + <img src="texture.png" alt="input" title="input" height="200" /> = <img src="imgs/output.png" alt="output" title="output" width="200" />

By chaining Densepose and Densepose2Texture together in runway, you can get the following effect:

<img src="imgs/runway1.png" alt="runway1" title="runway1" width="400" />
<img src="imgs/runway2.png" alt="runway1" title="runway2" width="400" />


### Credits / Source:
This is based on one of the [DensePose](https://github.com/facebookresearch/DensePose) notebooks: [
Texture Transfer Using Estimated Dense Coordinates](https://github.com/facebookresearch/DensePose/blob/master/notebooks/DensePose-RCNN-Texture-Transfer.ipynb)
