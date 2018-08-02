# HDP-Net: Haze Density Prediction Network for Nighttime Dehazing
Yinghong Liao, Zhuo Su, Xiangguo Liang, and Bin Qiu 

Released in 24/05/2018. The test codes are partly based on [DehazeNet](https://github.com/zlinker/DehazeNet).

# Abstract
Nighttime dehazing is a challenging ill-posed problem. Affected by unpredictable factors at night, daytime methods may be incompatible with night haze removal. In this paper, we propose an end-to-end learning-based solution to remove haze from night images. Different from the most-used atmospheric scattering model, we use a novel model to represent a night hazy image. We first present an estimator
to predict the haze density in patches of the image. Based on this, a CNN, called Haze Density Prediction Network (HDP-Net), is adopted
to obtain a haze density map so that it can be subtracted by the original hazy input to generate the desired haze-free output. The range of hue in night images may be altered by artificial light sources. To improve the dehazing capability in the certain range of hue, we devise four datasets under white light and yellow light conditions for network training. Finally, our method is compared with the state-of-the-art nighttime dehazing methods and demonstrated to have a superior performance. The project is available at https://github.com/suzhuoi/HDP-Net.

# Environment Requirement
[Caffe](https://github.com/BVLC/caffe)

[OpenCV](https://opencv.org/)

# Description
This is a test implementation for paper: HDP-Net: Haze Density Prediction Network for Nighttime Dehazing. Here we provide the test demo.

# Usage
Run the python file <code>HDP-Net_test.py</code> with the code like <code>python HDP-Net_test.py img/*.jpg</code> in command. 

# Datasets
We also provide the [datasets](https://pan.baidu.com/s/1cY8O5H8EYIwetPdb6xdupA) adopted in the work: Haze-Free, NightHaze-1, NightHaze-2, Haze-Free-Yellow, YellowHaze-1 and YellowHaze-2. Due to the limited capability of building datasets, these datasets are merely provided as reference. The initial size of images is not 128 x 128 but they are downsampled to smaller resolution before training. Dehazing effects may vary when a different dataset is trained. If you have any question, please contact us and we are willing to answer.

# Citation
        
	@inproceedings{hdpnet_liao_2018,		
	  title={HDP-Net: Haze Density Prediction Network for Nighttime Dehazing},
	  author={Liao, Yinghong and Su, Zhuo and Liang, Xiangguo and Qiu, Bin},
	  booktitle={The Pacific-Rim Conference on Multimedia (PCM)},
	  year={2018}
	} 

# Examples
<img src="https://github.com/nicholasly/HDP-Net/blob/master/img/01.jpg" width="250px" height="280px" align=left />
<img src="https://github.com/nicholasly/HDP-Net/blob/master/result/Dehaze_01.jpg" width="250px" height="280px" align=right/>

<img src="https://github.com/nicholasly/HDP-Net/blob/master/img/02.bmp" width="280px" height="180px" align=left />
<img src="https://github.com/nicholasly/HDP-Net/blob/master/result/Dehaze_02.bmp" width="280px" height="180px" align=right/>

<img src="https://github.com/nicholasly/HDP-Net/blob/master/img/03.jpeg" width="250px" height="280px" align=left />
<img src="https://github.com/nicholasly/HDP-Net/blob/master/result/Dehaze_03.jpeg" width="250px" height="280px" align=right/>

<img src="https://github.com/nicholasly/HDP-Net/blob/master/img/04.bmp" width="280px" height="180px" align=left />
<img src="https://github.com/nicholasly/HDP-Net/blob/master/result/Dehaze_04.jpg" width="280px" height="180px" align=right/>

<img src="https://github.com/nicholasly/HDP-Net/blob/master/img/05.bmp" width="280px" height="180px" align=left />
<img src="https://github.com/nicholasly/HDP-Net/blob/master/result/Dehaze_05.bmp" width="280px" height="180px" align=right/>
