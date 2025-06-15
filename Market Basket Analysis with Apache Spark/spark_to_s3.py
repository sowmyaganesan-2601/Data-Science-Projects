from pyspark.sql import SparkSession
import boto3
from botocore.exceptions import ClientError

# Initialize Spark Session with AWS S3 configuration
def create_spark_session():
    spark = SparkSession.builder \
        .appName("MarketBasketAnalysisToS3") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.access.key", "YOUR_ACCESS_KEY") \
        .config("spark.hadoop.fs.s3a.secret.key", "YOUR_SECRET_KEY") \
        .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
        .getOrCreate()
    
    return spark

# Function to save DataFrame to S3
def save_dataframe_to_s3(dataframe, s3_bucket, s3_path, format="csv"):
    """
    Save a Spark DataFrame to S3
    
    Parameters:
    -----------
    dataframe : pyspark.sql.DataFrame
        The DataFrame to save
    s3_bucket : str
        S3 bucket name
    s3_path : str
        Path within the bucket
    format : str
        File format (csv, parquet, json)
    """
    try:
        # Full S3 path
        s3_uri = f"s3a://{s3_bucket}/{s3_path}"
        
        # Save the DataFrame to S3
        if format == "csv":
            dataframe.write.mode("overwrite").option("header", "true").csv(s3_uri)
        elif format == "parquet":
            dataframe.write.mode("overwrite").parquet(s3_uri)
        elif format == "json":
            dataframe.write.mode("overwrite").json(s3_uri)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        print(f"Successfully saved DataFrame to {s3_uri}")
        
    except Exception as e:
        print(f"Error saving DataFrame to S3: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create Spark session
    spark = create_spark_session()
    
    # Load your data
    df = spark.read.csv("Groceries_dataset.csv", header=True, inferSchema=True)
    
    # Process data (example: group by Member_number and Date)
    df_grouped = df.groupBy("Member_number", "Date").agg({"itemDescription": "collect_list"})
    
    # Save to S3
    save_dataframe_to_s3(
        dataframe=df_grouped,
        s3_bucket="your-bucket-name",
        s3_path="market-basket-analysis/grouped_data",
        format="parquet"  # parquet is more efficient for structured data
    )
    
    # You can also save the frequent itemsets and association rules
    # Example:
    # save_dataframe_to_s3(frequent_itemsets, "your-bucket-name", "market-basket-analysis/frequent_itemsets", "csv")
    # save_dataframe_to_s3(association_rules, "your-bucket-name", "market-basket-analysis/association_rules", "csv")
    
    # Stop Spark session
    spark.stop()