## About People Counter 

People Counter is a python program designed to count person/people in an input image. It is based on an Object Detection algorithm (HOG + Linear SVM) to better detect people based on a pre-trained model.
This project uses the OpenCV library for the Image Processing and Detection part.

It is my final project for the Image Processing course in [USC](http://usc.ac.ir/en) (University of Science and Culture) supervised by Dr. Keramatfar


## Installation

```
git clone https://github.com/Amin-Esfandyari/People_Counter.git
```

## Recommended Python Version:

People Counter currently supports **Python 3**.

## Dependencies:

People Counter depends on the `opencv-python`, `imutils`, `numpy` and `argparse` python modules.


These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python39\python.exe -m pip install -r requirements.txt
```
- Installation on Linux
```
sudo pip install -r requirements.txt
```


## Usage

Short Form    | Long Form     | Description
------------- | ------------- | -------------
-i            | --image       | path to image test file directory
-h            | --help        | show the help message and exit

## Examples

* To list all the basic options and switches use -h or --help switch:

  ```python3 people_counter.py -h```
  or
  ```python3 people_counter.py --help```
  
* To set your an input image use -i or --image switch:

   ```python3 people_counter.py -i IMAGE```
  or
  ```python3 people_counter.py --image IMAGE```

