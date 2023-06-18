# DADS 6003 Thai Hand Writing Number Classification


## Data collection
Pictures of Thai numbers come from 2 sources.

1.[Kittinan 's Repository](https://github.com/kittinan/thai-handwriting-number)

2.Written Thai number by group members
 
 ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙
 
 
Image width and height: 28x28 pixels
  - Background : "White"
  - Font color : "Gray scale"
Data Preprocessing
### 1. convert image to array

   Converting an image to an array involves representing the image's pixel values in a structured numerical format. This allows for efficient manipulation and processing of the image using programming tools and algorithms. By converting the image to an array, we obtain a data structure that represents the image's content, enabling us to perform various image processing tasks effectively.

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
<em>Figure1</em>
</p>

Combining the data from various sources into a single unit, then splitting it into 70% for training and the remaining 30% for testing.

### 3.put in pipeline

<p align="center">
    <img width="768" height="310" src="https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png">
</p>
<p align="center">
<em>Figure2</em>
</p>


Pipeline Assembly

1. preprocessing
2. model and hyperparameter
 
   * Random Forest
     * bootstrap
     * max_depth
     * max_features
     * max_leaf_nodes
     * n_estimators
     * random_state
     * warm_start
   * ExtraTreesClassifier
     * max_depth
     * max_features
     * max_leaf_nodes
     * n_estimators
     * random_state
     * warm_start
   * XGBoost
     * colsample_bylevel
     * colsample_bynode
     * colsample_bytree
     * eval_metric
     * learning_rate
     * max_depth
     * n_estimators
     * etc.
   * Neural Networks
     * activation
     * alpha
     * hidden_layer_sizes
     * random_state
     * solver
   * Logistic Regression
     * C
     * max_iter
     * multi_class
     * random_state
     * solver

### 5.Tuning Hyper Parameter
GridSearch is a technique for tuning hyperparameters by exhaustively searching through a predefined grid of hyperparameter values. It systematically evaluates the performance of a machine learning model across all possible combinations of hyperparameters, allowing for the selection of the optimal configuration. Although it can be computationally expensive, GridSearch provides an effective approach to finding the best hyperparameter values for maximizing the model's performance.

### 6.Plot Learning Curve
Learning curve is a useful tool for assessing the performance and generalization ability of a machine learning model. When a model exhibits a good fit, the learning curve demonstrates a desirable pattern: as the training data size increases, both the training and validation curves converge and plateau at a high level of performance. This indicates that the model is learning well from the data and can generalize effectively to new, unseen examples. On the other hand, an overfitting model shows a significant gap between the training and validation curves, with the training curve reaching near-perfect performance while the validation curve plateaus at a lower level. This suggests that the model is overly complex and has memorized the training data, failing to generalize well to new data. Achieving a good fit, where the training and validation curves converge at a satisfactory level, is the goal when building machine learning models to ensure reliable performance on unseen data.

### 7.Accuracy Score

### 8.Cross Validation Score







    



 
 
 
 



## Credits

  * [Data Set](https://github.com/kittinan/thai-handwriting-number) from [kittinan](https://github.com/kittinan)
  * [grid_search_utils](https://www.kaggle.com/code/juanmah/grid-search-utils) from [Juanma Hernández](https://www.kaggle.com/juanmah)
  * [_Figure1_](https://miro.medium.com/v2/resize:fit:1400/1*-8_kogvwmL1H6ooN1A1tsQ.png)
  * [_Figure2_](https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png)


