# DADS 6003 Thai Hand Writing Number Classification


## Data collection
รูปภาพตัวเลขไทยของกลุ่มเราได้มาจาก 2 แหล่ง ข้อมูล 
 1.จาก repo ของคุณ กิตินันท์
 2.เขียนเองเอง
 
 ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙
 
 
Image width and height: 28x28 pixels
  - Background : "White"
  - Font color : "Gray scale"
Data Preprocessing
### 1. convert image to array

__1.1) Original image__

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/add8c1a8-0ecd-4289-9dd1-61ffb4107d08)



__1.2) Dilated image__

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/2f43314c-96e6-41c0-9cac-308dca7f8f38)


__1.3) Crop and squared Imaage__
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/7105aef7-baff-4053-aafd-23019d84271b)


__1.4) Resize__
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/c6253682-8074-40bb-a9f2-4520f4d53fff)

### 2.Train Test Split

<img width="1136" height="372" src="https://miro.medium.com/v2/resize:fit:1400/1*-8_kogvwmL1H6ooN1A1tsQ.png">

<p align="center">
_Figure1_
</p>

ทำการรวมแหล่งของข้อมูลมาเป็นก้อนเดียวแล้วหลังจากนั้นแยก ข้อมูล ไปเทรน 7 ส่วน และ อีก 3 ส่วนนำมาเพื่อใช้ทดสอบ

### 3.put in pipeline

<p align="center">
    <img width="768" height="310" src="https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png">
</p>
<p align="center">
_Figure2_
</p>


โดยการนำไปใส่ pipeline  ประกอบไปด้วย

1. preprocessing
2. โมเดลที่กลุ่มพวกเราเลือกใช้
 
   * Random Forest
   * ExtraTreesClassifier
   * XGBoost
   * Neural Networks
   * Logistic Regression

### 5.Tuning Hyper Parameter
 โดยใช้ gridseach เพื่อหา hyperparameter ที่ให้ train test score ออกมาดีที่สุด

### 6.Plot Learning Curve
เพื่อใช้ดูทิศทางการ converge ของระหว่างค่า train score และ test score

### 7.Accuracy Score

### 8.Cross Validation Score







    



 
 
 
 



## Credits

  * [Data Set](https://github.com/kittinan/thai-handwriting-number) from [kittinan](https://github.com/kittinan)
  * [grid_search_utils](https://www.kaggle.com/code/juanmah/grid-search-utils) from [Juanma Hernández](https://www.kaggle.com/juanmah)
  * [_Figure1_](https://miro.medium.com/v2/resize:fit:1400/1*-8_kogvwmL1H6ooN1A1tsQ.png)
  * [_Figure2_](https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png)


