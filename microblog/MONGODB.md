# **What is MongoDB**

MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need. It is a NoSQL database that stores data in JSON-like documents, which makes the database very flexible and scalable.

## **Installing MongoDB**

To install MongoDB, you need to download the MongoDB Community Server from the [MongoDB website](https://www.mongodb.com/download-center/community). You can download the latest version of MongoDB Community Server for your operating system.

After downloading the MongoDB Community Server, you need to install it. You can follow the instructions on the [MongoDB website](https://docs.mongodb.com/manual/administration/install-community/) to install MongoDB.

## **Creating Atlas account**

To create an Atlas account, you need to go to the [Atlas website](https://www.mongodb.com/cloud/atlas) and click the **Sign Up** button.

- **Step 1**: After signing up, you need to choose the cloud provider and region for your cluster. You can choose the free tier for the cluster, the only free tier available is the M0 cluster. The M0 cluster is a shared cluster, which means that you share the cluster with other users. You can choose the region closest to you.
- **Step 2**: Now you need to configure the Network Access for your cluster. You can choose to allow access from anywhere or only from specific IP addresses. You can also choose to allow access from anywhere and add specific IP addresses later.
- **Step 3**: Now you need to configure the user access for your cluster. Make sure to use a password that you can remember because you will need it later. You can also choose to add more users later.

## **Connecting to Atlas Database using MongoDB Compass**

To connect to the Atlas database using MongoDB Compass, you need to do the following:

- **Step 1**: After opening MongoDB Compass, you can create a new connection, the URI is like the following (You can get the URI from the Atlas website in the **Connect** tab):
  ```
  mongodb+srv://<username>:<password>@<cluster-address>/test
  ```
- **Step 2**: After entering the URI, you need to click the **Connect** button. If you get an error, you need to make sure that you entered the correct username and password.

## **Creating a database**

To create a database, you need to do the following:

- **Step 1**: After connecting to the Atlas database using MongoDB Compass, you need to click the **Create database** button.
- **Step 2**: Now you need to enter the name of the database (in the class example, I have created a database with the name `entries`) and of the collection, then click the **Create Database** button.
