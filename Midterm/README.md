# Python Version

3.9 is fine for all problems except Question 8, which requires 3.7.

Requirements stored in `requirements.txt` in each folder (if applicable).

# Strucutre of Files

- Question 1
  - Part a - Q1/Q1a.py
  - Part b - Q1/Q1b.py
  - Part c - Q1/Q1c.py
- Question 2
  - Part a - Q2/Q2.txt and Q2/Q2a.pdf
  - Part b - Q2/Q2.txt
  - Part c - Q2/Q2.txt and Q2/Q2c.py
- Question 3
  - Part a - Q3/Q3a.py
  - Part b - Q3/Q3b.py
- Question 4
  - Part a - Q4/Q4a.md
  - Part b - Q4/Q4b.py
  - Part c - Q4/Q4c.py
- Question 5
  - part a - Q5/Q5a.txt
  - part b - Q5/Q5b.png
  - part c - Q5/Q5c.py, Q5/model.obj and Q5/Q5 train Q learn model.py
- Question 6
  - part a - Q6/Q6a.ipynb
  - part b - Q6/Q6b_output.mp4 and Q6/Q6bc.ipynb
  - part c - Q6/Q6bc.ipynb
- Question 7
  - part a - Q7/Q7.md and Q7/Q7.py (other models are called their respective names)
- Question 8
  - part a - Q8/Q8a.py
  - part b - Q8/8B/Q8b.py
    -  From within 8B/yolo5 run $ python train.py --batch 16 --epochs 5 --data dataset.yaml --weights yolov5s.pt
    -  Edit the batch size, number of epocs, and add a '--workers <x>' argument depending on hardware specs. Default values for these are 16, 3, and 0.
    -  Results will be displayed in terminal, additionally, graphics will be placed in 8B/yolo5/runs/train/exp<x>.
    -  The highest value after (exp) will be the most recent data to use.
    -  The best model will be found in 8B/yolov5/runs/train/exp<x>/weights/best.pt
    -  Text result of findings is found in results.txt
- Question 9
  - parts a-d - Q9/Q9.md


