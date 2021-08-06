<!--
*** This README markdown is built from the following repo
*** https://github.com/othneildrew/Best-README-Template
-->

<!-- PROJECT SHIELDS -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



  <h3 align="center">AI Trainer</h3>

  <p align="left">
    AI virtual trainer will detect the number of counts of biceps exercise, it uses python and OpenCV
    
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

In this project we will an AI trainer using Python, OpenCV and Mediapipe frameworks

We can divide the project into the following tasks:
* Capture frames from webcam/video using `OpenCV` framework
* Detect arm landmarks using google `Mediapipe` package
* `pose_estimation_module` tracks landmarks of arm, find the coordinates of the important landmarks, and calculate the angle of the elbow 
* Using these landmarks, and angle, the number of biceps counts is calculated


### Built With

frameworks used in building this project

* [OpenCV](https://opencv.org)
* [MediaPipe](https://mediapipe.dev)



<!-- GETTING STARTED -->
## Getting Started

You need to install the following dependencies in order to run the project
### Dependencies
- OpenCV
- Mediapipe


### Prerequisites

Install the following python packages to your env/vevn using the shell/bash.
* pip
  ```sh
  pip install opencv-python
  pip install mediapipe
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SamirGouda/AI_Trainer.git
   ```
   
2. Run the python file using from your terminal
   ```shell
   python ai_trainer_project.py
   ```



<!-- USAGE EXAMPLES -->
## Usage

this project only detect the left arm, the face should be visible
for mediapipe framework to accurately detect the arm landmarks

to change the capture to your webcam, change the following line in code

```python
cap = cv2.VideoCapture('ai_trainer/curls2.mp4')
```
to 
```python
cap = cv2.VideoCapture(0)
```
note that your capture device (i.e. webcam) may differ, try other number (0,1,2) until it works

to close frame window just press the `q` button on your keyboard

[![video-screenshot][screenshot-2]]
[![webcam-screenshot][screenshot-3]]


<!-- CONTACT -->
## Contact

Samir Gouda - [https://www.linkedin.com/in/samirgouda](https://www.linkedin.com/in/samirgouda) 

email: [samiir.ahmedd@gmail.com](mailto:samiir.ahmedd@gmail.com)

Project Link: [https://github.com/SamirGouda/AI_Trainer](https://github.com/SamirGouda/AI_Trainer)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew/) for his README template
* [murtazahassan](https://github.com/murtazahassan) for his computer vision course  




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/samirgouda/
[product-screenshot]: images/1.png
[screenshot-2]: images/2.png
[screenshot-3]: images/3.png
