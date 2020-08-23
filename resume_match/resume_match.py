import nltk
nltk.download('stopwords')
import pandas as pd
from nltk.corpus import stopwords
import re

# load data
#df = pd.read_csv('./jobs_small.csv', encoding="latin-1")
df = pd.read_csv('./jobs.csv', encoding="utf-8")
#print(df.head())

# text preprocessing
REPLACE_BY_SPACE_RE = re.compile('[#+_/(){}!^?<>"''*\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
match_regex = re.compile('\d+')
STOPWORDS = set(stopwords.words('english'))

# data cleaning
def clean_text(text):
    # change to lower-csae
    text = str(text).lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    # remove BAD_SYMBOLS_RE
    text = BAD_SYMBOLS_RE.sub('', text)
    text = match_regex.sub('', text)
    # drop the stopwords
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) 
    return text

# read and clean the resume file
f = open('./CE.txt', 'r')          ############# change resume here ####################
text = f.read()
text = clean_text(text)

# clean the desc field
df['desc_clean'] = df['description'].apply(clean_text)
df.drop(columns=['description', 'id'], inplace=True)
df.loc[0] = ['resume', 0, 0, 0, text]

for i in range(len(df)):
  try:
    if df['desc_clean'][i]=='nan' or df['desc_clean'][i]=='' or len(df['desc_clean'][i]) < 100:
      df.drop(labels=i, inplace=True)
  except:
    continue

df.dropna(axis=0, inplace=True)
df['id'] = [i for i in range(len(df))]
#print(df['desc_clean'])
df.to_csv('./jobs_clean.csv')

from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover
from pyspark.ml.feature import HashingTF, IDF
#from pyspark.ml.feature import NGram

spark=SparkSession \
        .builder \
        .appName('tfidf_app') \
        .getOrCreate()

# load data
df0 = spark.read.csv("./jobs_clean.csv", header=True, multiLine=True, inferSchema=True)
df1 = pd.read_csv('./jobs_clean.csv')
#df0.show()
print('The number of jobs：',df0.count())
print('\nthe distinct jobs name: ', df1.job.unique())
print('\nThere are', len(df1.job.unique())-1, 'different kinds of jobs in the table.')

# split the desc field
tokenizer = Tokenizer(inputCol='desc_clean', outputCol='desc_words')
df = tokenizer.transform(df0)
#df.show()
#df.select('desc_words').show(10)

# compute TF-IDF
hashingTF = HashingTF(inputCol='desc_words', outputCol='desc_words_tf')
tf = hashingTF.transform(df).cache()
idf = IDF(inputCol='desc_words_tf', outputCol='desc_words_tfidf').fit(tf)
tfidf = idf.transform(tf).cache()
#print('tfidf for each job:', tfidf.select('desc_words_tfidf').show(10,truncate=False))

# data normalization
from pyspark.ml.feature import Normalizer
normalizer = Normalizer(inputCol="desc_words_tfidf", outputCol="norm")
tfidf = normalizer.transform(tfidf)
#tfidf.select("id", "norm").show(6)

# compute similarity between jobs and resume
import pyspark.sql.functions as psf 
from pyspark.sql.types import DoubleType
print('\nCompute the similarity between jobs and resume...')
dot_udf = psf.udf(lambda x,y: float(x.dot(y)), DoubleType()) # define dot-product function
tfidf = tfidf.alias("a1").join(tfidf.alias("a2"), psf.col("a1.id") == 0)\
        .select(
            psf.col("a1.job"),
            psf.col("a1.id").alias("id1"), 
            psf.col("a2.id").alias("id2"), 
            dot_udf("a1.norm", "a2.norm").alias("similarity"))
#tfidf.show(10)
print('Done!')

# show Top-20 matched jobs
match = tfidf.where('id1 = 0').sort('similarity', ascending=False).where('id2 > 0')
top_match = match.limit(20)
print('Top 20 matched jobs:')
df0.alias("a1").join(top_match.alias("a2"), psf.col("a1.id") == psf.col("a2.id2"))\
    .select(psf.col("a1.job"), "a1.company", "a1.location", "a2.similarity")\
    .sort('similarity', ascending=False).show()

match = df0.alias("a1").join(match.alias("a2"), psf.col("a1.id") == psf.col("a2.id2"))\
    .select(psf.col("a1.job"), "a1.company", "a1.location", "a2.similarity")\
    .sort('similarity', ascending=False)

# create SQL table
match.createOrReplaceTempView("match")

# start SQL query

# select jobs in specific location
df = spark.sql("SELECT * FROM match WHERE location like 'New York City%'")
#df = spark.sql("SELECT * FROM match WHERE location like 'San Francisco%'")
df.show()

#select specific jobs
#df = spark.sql("SELECT * FROM match where job = 'computer vision engineer'")
#df = spark.sql("SELECT * FROM match where job = 'FPGA Engineer'")
df = spark.sql("SELECT * FROM match where job = 'Embedded Systems Engineer'")

df.show()