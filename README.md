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

_1.1) Original image_

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/add8c1a8-0ecd-4289-9dd1-61ffb4107d08)




_1.2) Dilated image_

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/2f43314c-96e6-41c0-9cac-308dca7f8f38)



_1.3) Crop and squared Imaage_
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/7105aef7-baff-4053-aafd-23019d84271b)



_1.4) Resize_
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/c6253682-8074-40bb-a9f2-4520f4d53fff)

### 2.แยก train test split

![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/4186f401-2098-409d-8342-13c0162b1f02)

ทำการรวมแหล่งของข้อมูลมาเป็นก้อนเดียวแล้วหลังจากนั้นแยก ข้อมูล ไปเทรน 7 ส่วน และ อีก 3 ส่วนนำมาเพื่อใช้ทดสอบ

### 3.put in pipeline

<p align="center">
    <img src="[https://picsum.photos/460/300](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/e59e2cc9-8e67-4fd2-a502-c154f4fee214)">
</p>

<p align="center">
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/e59e2cc9-8e67-4fd2-a502-c154f4fee214)
</p>



โดยการนำไปใส่ pipeline  ประกอบไปด้วย

1. preprocessing
2. โมเดลที่กลุ่มพวกเราเลือกใช้
 
   * Random Forest
   * ExtraTreesClassifier
   * XGBoost
   * Neural Networks
   * Logistic Regression

### 5.tuning hyper parameter
 โดยใช้ gridseach เพื่อหา hyperparameter ที่ให้ train test score ออกมาดีที่สุด

### 6.Plot Learning Curve
เพื่อใช้ดูทิศทางการ converge ของระหว่างค่า train score และ test score

### 7.accuracy score

### 8.cross validation score







    



 
 
 
 



## Credits

  * [Data Set](https://github.com/kittinan/thai-handwriting-number) from [kittinan](https://github.com/kittinan)
  * [grid_search_utils](https://www.kaggle.com/code/juanmah/grid-search-utils) from [Juanma Hernández](https://www.kaggle.com/juanmah)


