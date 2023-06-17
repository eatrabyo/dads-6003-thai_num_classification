# DADS 6003 Thai Hand Writing Number Classification


1 Data collection
รูปภาพตัวเลขไทยของกลุ่มเราได้มาจาก 2 แหล่ง ข้อมูล 
1.จาก repo ของคุณ กิตินันท์
2.เขียนเองเอง
 
 ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙
 
 
Image width and height: 28x28 pixels
  - Background : "White"
  - Font color : "Gray scale"
Data Preprocessing
##1. convert image to array

#1.1)Original image

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/add8c1a8-0ecd-4289-9dd1-61ffb4107d08)




#1.2)Dilated image

 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/2f43314c-96e6-41c0-9cac-308dca7f8f38)



#1.3)Crop and squared Imaage
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/7105aef7-baff-4053-aafd-23019d84271b)



#1.4)Resize
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/c6253682-8074-40bb-a9f2-4520f4d53fff)

##2.แยก train test split 

##3. preprocessing standard scaler

##4.put in pipeline

##5.tuning hyper parameter

6.







    



 
 
 
 



## Credits

  * [Data Set](https://github.com/kittinan/thai-handwriting-number) from [kittinan](https://github.com/kittinan)
  * [grid_search_utils](https://www.kaggle.com/code/juanmah/grid-search-utils) from [Juanma Hernández](https://www.kaggle.com/juanmah)


