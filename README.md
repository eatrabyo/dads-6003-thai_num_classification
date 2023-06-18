# DADS 6003 Thai Hand Writing Number Classification


## Data Collection
Pictures of Thai numbers come from 2 sources.

1. [Kittinan 's Repository](https://github.com/kittinan/thai-handwriting-number)

2. Written Thai number by group members
 
 ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙
 
 
Image width and height: 28x28 pixels
  - Background : "White"
  - Font color : "Gray scale"
Data Preprocessing
### 1. Convert Image to Array

   Before feeding our dataset into the machine learning algorithm, we need to convert the pictures into an array of pixels. We can achieve this by utilizing the cv2 library to read the images and perform necessary image processing.

__1.1) Original Image__

The picture below displays a sample of the original image.
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/add8c1a8-0ecd-4289-9dd1-61ffb4107d08)



__1.2) Dilation

We have decided to apply a dilation process to the dataset, as dilation can assist in regularizing the machine learning model. The picture below demonstrates the reduction in the thickness of the numbers.
 
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/2f43314c-96e6-41c0-9cac-308dca7f8f38)


__1.3) Crop and Squared Image__

Some numbers are located in the corners of the pictures, with varying sizes, some being too small and others being large. Therefore, after dilating the dataset, we plan to crop out the white background, ensuring that the numbers are as close as possible to their edges.

![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/7105aef7-baff-4053-aafd-23019d84271b)


__1.4) Resize__
 
After applying dilation and cropping, we resize the pictures to 28 x 28 pixels. Subsequently, we flatten the arrays to 784 elements.
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/83213407/c6253682-8074-40bb-a9f2-4520f4d53fff)

### 2. Train & Test Split

<img width="1136" height="372" src="https://miro.medium.com/v2/resize:fit:1400/1*-8_kogvwmL1H6ooN1A1tsQ.png">

<p align="center">
<em>Figure1</em>
</p>

Combining the data from various sources into a single unit, then splitting it into 70% for training and the remaining 30% for testing.

### 3. Pipeline

<p align="center">
    <img width="768" height="310" src="https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png">
</p>
<p align="center">
<em>Figure2</em>
</p>


Pipeline Assembly

1. Preprocessing
   * Standardization
    - Standardizing the dataset can significantly improve runtime performance, especially considering the high dimensionality of X (784).
2. Model and Hyperparameter
 Below is the list of our selected models from Pycaret and the hyperparameters we are focusing on.
   * Random Forest
     * bootstrap
     * max_depth
     * max_features
     * max_leaf_nodes
     * n_estimators
     * warm_start
   * ExtraTreesClassifier
     * max_depth
     * max_features
     * max_leaf_nodes
     * n_estimators
     * warm_start
   * XGBoost
     * colsample_bylevel
     * colsample_bynode
     * colsample_bytree
     * eval_metric
     * learning_rate
     * max_depth
     * n_estimators
   * Neural Networks
     * activation
     * alpha
     * hidden_layer_sizes
     * solver
   * Logistic Regression
     * C
     * max_iter
     * multi_class
     * solver

```
pipe_et = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', ExtraTreesClassifier())
])
```
### 5. Tuning Hyper Parameter

We utilize GridSearchCV for hyperparameter tuning of each model. Although this method may take longer to obtain the results, we consider it suitable for our purposes. GridSearchCV operates by exploring every combination of user-provided hyperparameters. The completion time depends on the number of hyperparameters and the computational complexity (Big O Notation) of each model. We have chosen GridSearchCV over RandomizedSearchCV or TuneSearchCV due to the consistent scoring and the acceptable running time it offers for this particular dataset.

Below is an example of tuning Extra Trees Classifier.
```
parameters = {
    'criterion':['gini','entropy','log_loss'],
    'max_features':['sqrt','log2',None],
    'bootstrap':[True,False],
    'random_state':[10],
    'warm_start':[True,False],
    'class_weight':['balanced','balanced_subsample',None],
    'n_estimators':[50, 75],
    'max_depth': [i for i in range(5,16)],
    'max_leaf_nodes': [100,200]
}
tune = GridSearchCV(ExtraTreesClassifier(),cv=5,param_grid=parameters,n_jobs=-1,scoring='accuracy')
tune.fit(x_train, y_train)
print(tune.best_params_)
```

### 6. Plot Learning Curve

Learning curve is a useful tool for assessing the performance and generalization ability of a machine learning model. When a model exhibits a good fit, the learning curve demonstrates a desirable pattern: as the training data size increases, both the training and validation curves converge and plateau at a high level of performance. This indicates that the model is learning well from the data and can generalize effectively to new, unseen examples. On the other hand, an overfitting model shows a significant gap between the training and validation curves, with the training curve reaching near-perfect performance while the validation curve plateaus at a lower level. This suggests that the model is overly complex and has memorized the training data, failing to generalize well to new data. Achieving a good fit, where the training and validation curves converge at a satisfactory level, is the goal when building machine learning models to ensure reliable performance on unseen data.

```
plt.figure()
plt.xlabel("Training examples")
plt.ylabel("Accuracy Score")

plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                    train_scores_mean + train_scores_std, alpha=0.1,
                    color="r")
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                    test_scores_mean + test_scores_std, alpha=0.1, color="g")
plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
            label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
            label="Cross-validation score")

plt.legend(loc="best")
```
![image](https://github.com/eatrabyo/dads-6003-thai_num_classification/assets/92035314/45f915aa-0dbe-4d55-870c-9bdcf6d3e250)


### 7. Accuracy Score

We have chosen the accuracy score as the metric for measuring accuracy in this project instead of precision, recall, or F1-score. The reason behind this choice is that the accuracy score provides a straightforward measure of how well the model classifies the digits correctly.

Below are the accuracy score for each model.

|**Models**|**Randome Forest**|**Extra Trees Classifier**|**XGBoost**|**Neural Network**|**Logistic**|
|---|:---:|:---:|:---:|:---:|:---:|
|**Accuracy Train**|_0.9682_|_0.9462_|_0.8193_|__0.9812__|_0.9483_|
|**Accuracy Test**|*0.7907*|*0.7694*|*0.7093*|__0.7982__|*0.7970*|

### 8. Cross Validation Score


Cross-validation score is an essential evaluation metric in machine learning for assessing a model's performance and generalization ability. It involves splitting the dataset into multiple subsets, training the model on different combinations of these subsets, and evaluating its performance on the remaining data. By using cross-validation, we can obtain a more accurate estimation of the model's performance on unseen data compared to a single train-test split. It helps in detecting and mitigating issues such as overfitting or underfitting, aids in selecting the best hyperparameters, and provides a more reliable measure of the model's predictive capability. Ultimately, cross-validation score enables us to make informed decisions about model selection and optimization for better overall performance.

Beloew are the cross validation score (5 folds) for each model.

|**Models**|**Randome Forest**|**Extra Trees Classifier**|**XGBoost**|**Neural Network**|**Logistic**|
|---|:---:|:---:|:---:|:---:|:---:|
|**CV Score**|_0.7832_|_0.7778_|_0.6896_|_0.8058_|_0.7875_|
|**SD**|*0.0081*|*0.0176*|*0.0219*|_0.0212_|*0.0183*|





    



 
 
 
 



## Credits

  * [Data Set](https://github.com/kittinan/thai-handwriting-number) from [kittinan](https://github.com/kittinan)
  * [grid_search_utils](https://www.kaggle.com/code/juanmah/grid-search-utils) from [Juanma Hernández](https://www.kaggle.com/juanmah)
  * [_Figure1_](https://miro.medium.com/v2/resize:fit:1400/1*-8_kogvwmL1H6ooN1A1tsQ.png)
  * [_Figure2_](https://datatron.com/wp-content/uploads/2021/05/Machine-Learning-Pipeline_2.png)


