import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('users-by-city-job').getOrCreate()

json = [
  {
    "id": "8059ed43-ce32-4f62-887b-5f4371bdc959",
    "name": "Dan Volkman",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/947.jpg",
    "phone-number": "(650) 725-5481",
    "zip-code": "23463-6034",
    "birth-date": "2022-08-16T10:04:34.467Z",
    "city": "Sammamish"
  },
  {
    "id": "3dc40c64-03e8-4b4c-9e8d-14d05fba31ac",
    "name": "Mrs. Leonard VonRueden",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/341.jpg",
    "phone-number": "1-733-577-8310",
    "zip-code": "07632-9841",
    "birth-date": "2023-01-28T05:26:40.535Z",
    "city": "Pine Bluff"
  },
  {
    "id": "bcfcdc63-ff9e-4d13-b9a4-6f133c670a9b",
    "name": "Winifred Bahringer",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/171.jpg",
    "phone-number": "680-731-1417 x32360",
    "zip-code": "21083-8956",
    "birth-date": "2022-06-09T03:36:54.117Z",
    "city": "Waterloo"
  },
  {
    "id": "5825838a-cd9d-4d46-b035-2ae8e09e6ced",
    "name": "Phillip Dickens",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/21.jpg",
    "phone-number": "535.956.0079 x434",
    "zip-code": "78835",
    "birth-date": "2022-09-25T00:07:07.130Z",
    "city": "Waterloo"
  },
  {
    "id": "af8da616-324f-4f63-9e7a-dbf0d8937118",
    "name": "Jake Rowe",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/517.jpg",
    "phone-number": "560-763-8714",
    "zip-code": "85175-8550",
    "birth-date": "2023-03-22T16:32:14.767Z",
    "city": "Waterloo"
  },
  {
    "id": "6503558e-56aa-4929-8c72-24cfba371fec",
    "name": "Hubert Kertzmann",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/786.jpg",
    "phone-number": "(263) 581-8236",
    "zip-code": "26573",
    "birth-date": "2022-11-13T01:10:22.632Z",
    "city": "DeSoto"
  },
  {
    "id": "6ccc46b9-6010-476b-b5e0-4711a6cfa33f",
    "name": "Pamela Goodwin",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/228.jpg",
    "phone-number": "(905) 626-8980 x1276",
    "zip-code": "29077",
    "birth-date": "2023-02-15T12:42:58.073Z",
    "city": "Citrus Heights"
  },
  {
    "id": "9097dfe4-e9ec-4377-ad80-21ce6ccba011",
    "name": "Mr. Lucas D'Amore",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/130.jpg",
    "phone-number": "1-635-265-5438 x48133",
    "zip-code": "29125-8852",
    "birth-date": "2023-01-24T18:30:32.605Z",
    "city": "Mount Vernon"
  },
  {
    "id": "0aec31f9-e884-416c-bc47-52d35501cd73",
    "name": "Archie Konopelski",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1203.jpg",
    "phone-number": "1-786-318-7540 x54269",
    "zip-code": "75847-4181",
    "birth-date": "2022-11-09T15:36:59.468Z",
    "city": "Mount Vernon"
  },
  {
    "id": "50976588-e0c1-4fde-84d8-d1ec6fa943ac",
    "name": "Andre Funk",
    "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/13.jpg",
    "phone-number": "1-694-708-2735 x0041",
    "zip-code": "02772",
    "birth-date": "2023-02-05T23:01:31.979Z",
    "city": "Tonawanda"
  }
]

df_users = spark.createDataFrame(data=json)

df_users.createOrReplaceTempView("usuarios")

spark.sql("""
  select 
    id,
    city,
    name
  from usuarios
""").show(truncate=False)

spark.sql("""
  select count(*) users_by_city,
    city
  from usuarios
  group by city
""").show(truncate=False)