Project: Walmart Sales Prediction

Description: The project is a Time Series project to forecast weekly demand of the Walmart stores for each store-sku combination. The dataset used is Walmart sales dataset
from Kaggle which involves 45 stores and about 90 sku's/categories of products.The model built is able to predict weekly sales for each store-sku combination(45*90 = 4050)
Thus a total of 4500 models are required to achieve the objective. This is possible by levaraging distributed computing in pyspark.
The project utilizes the power of pandas udf and thus models are bullt for each store-product group

Base Language: Pyspark

Framework: Streamlit

Cloud Service for Deployment: Heroku

Project url: http://spark-sales-predictor.herokuapp.com/
