# NoSQL

## What NoSQL means
NoSQL, or "Not Only SQL," is a term used to describe a category of database systems that are designed to store and retrieve data in a way that is different from traditional relational databases. Unlike traditional relational databases, which use a structured schema and SQL (Structured Query Language) for data manipulation, NoSQL databases are more flexible and can handle unstructured or semi-structured data.

## What is difference between SQL and NoSQL
Data Model:
SQL (Relational Databases): Follow a structured and predefined schema, often represented as tables with rows and columns.
NoSQL Databases: Offer more flexibility with various data models, such as document-oriented (e.g., MongoDB), key-value pairs (e.g., Redis), wide-column stores (e.g., Cassandra), and graph databases (e.g., Neo4j).

Schema:
SQL: Enforces a rigid schema where the structure of the data must be defined in advance.
NoSQL: Generally allows for a dynamic or schema-less approach, enabling flexibility in handling evolving data structures.

Scalability:
SQL: Typically scales vertically by adding more powerful hardware to a single server.
NoSQL: Often scales horizontally by adding more servers or nodes to a distributed database cluster, making it more suitable for handling large amounts of data and traffic.

Consistency and ACID Properties:
SQL: Emphasizes ACID properties (Atomicity, Consistency, Isolation, Durability) to ensure data integrity in transactions.
NoSQL: May sacrifice some ACID properties in favor of performance and scalability, often opting for eventual consistency.

Use Cases:
SQL: Well-suited for applications with complex relationships and structured data, such as financial systems and traditional business applications.
NoSQL: Ideal for scenarios with large amounts of unstructured or semi-structured data, real-time applications, and where flexibility and scalability are crucial, such as in social media platforms and big data analytics.

Examples:
SQL: MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.
NoSQL: MongoDB, Cassandra, Redis, Neo4j.

## What is ACID
ACID is an acronym that represents a set of properties or characteristics that ensure the reliability and consistency of transactions in a relational database system. These properties are essential for maintaining the integrity of data in a database, particularly in scenarios where multiple operations need to be performed as part of a single transaction.

The ACID properties are:

Atomicity (A): This property ensures that a transaction is treated as a single, indivisible unit of work. Either all the operations within the transaction are successfully completed, or none of them are. If any part of the transaction fails, the entire transaction is rolled back to its previous state, maintaining the consistency of the database.

Consistency (C): Consistency ensures that a transaction brings the database from one valid state to another. In other words, the database must adhere to a set of predefined rules and constraints, maintaining the integrity of relationships between data elements. If a transaction violates the integrity constraints, it is rolled back.

Isolation (I): Isolation ensures that the execution of one transaction is isolated from the execution of other transactions. Even though multiple transactions may be executing concurrently, the outcome should be as if they were executed sequentially. Isolation prevents interference and ensures that the intermediate states of a transaction are not visible to other transactions until the transaction is committed.

Durability (D): Durability guarantees that once a transaction is committed, its effects are permanent and survive any subsequent failures or system crashes. The changes made by a committed transaction are stored in a way that ensures they will persist, even in the event of a power outage, hardware failure, or other system disruptions.

## What is a document storage
Document storage, in the context of databases, refers to a type of storage system used by NoSQL databases, specifically in document-oriented databases. In this model, data is stored in flexible, semi-structured documents, typically in formats like JSON (JavaScript Object Notation) or BSON (Binary JSON). Each document can contain key-value pairs, arrays, and nested structures.

Key characteristics of document storage include:

Document Format: Data is stored as documents, which are self-contained and can include nested structures. Each document may have a unique structure, allowing for flexibility in data representation.

No Fixed Schema: Document-oriented databases do not enforce a rigid schema. Each document within a collection can have its own set of fields, allowing for dynamic and evolving data models.

Querying: Document-oriented databases provide mechanisms for querying and indexing the data within documents. Queries can be performed on the content of the documents, and indexing helps optimize the retrieval of data.

Scalability: Document-oriented databases are often designed to scale horizontally by distributing data across multiple servers or nodes. This scalability is useful for handling large amounts of data and accommodating growing workloads.

Examples: MongoDB is a popular example of a document-oriented database. In MongoDB, data is stored as BSON documents in collections, and queries can be performed using a flexible query language.

## What are NoSQL types
NoSQL databases can be categorized into several types based on their data models and storage approaches. The main types of NoSQL databases include:

Document-oriented Databases:
Characteristics: Store data in flexible, semi-structured documents (e.g., JSON or BSON). Each document can have a different structure within the same collection.
Examples: MongoDB, CouchDB, RavenDB.

Key-Value Stores:
Characteristics: Simplest NoSQL model, where each data item (value) is associated with a unique key. Efficient for read and write-intensive operations.
Examples: Redis, Amazon DynamoDB, Riak.

Column-family Stores:
Characteristics: Data is organized into columns rather than rows, and columns can be grouped into column families. Well-suited for read and write-intensive workloads.
Examples: Apache Cassandra, HBase.

Graph Databases:
Characteristics: Designed for representing and querying graph-like structures with nodes, edges, and properties. Efficient for complex relationships and network analysis.
Examples: Neo4j, Amazon Neptune, ArangoDB.

Object-oriented Databases:
Characteristics: Store data in the form of objects, similar to object-oriented programming. Each object can have attributes and methods.
Examples: db4o, ObjectDB.

Multi-model Databases:
Characteristics: Support multiple data models within the same database system, allowing users to choose the most appropriate model for their specific use case.
Examples: ArangoDB, OrientDB.

## What are benefits of a NoSQL database
NoSQL databases offer several benefits that make them suitable for specific use cases. Here are some key advantages of using NoSQL databases:

Schema Flexibility:
Benefit: NoSQL databases allow for flexible and dynamic schemas, enabling developers to work with semi-structured or unstructured data. This flexibility is particularly useful in scenarios where the data model is expected to evolve over time.

Scalability:
Benefit: NoSQL databases are often designed to scale horizontally by adding more servers or nodes to a distributed system. This horizontal scalability makes them well-suited for handling large amounts of data and accommodating increased workloads.

High Performance:
Benefit: NoSQL databases are optimized for specific use cases, leading to high performance in scenarios such as read or write-intensive workloads. They can provide faster query responses compared to traditional relational databases for certain types of applications.

Support for Large Data Sets:
Benefit: NoSQL databases excel at handling large volumes of data, making them suitable for big data and real-time analytics applications. Their distributed and scalable nature allows them to manage and process massive amounts of data efficiently.

Variety of Data Models:
Benefit: NoSQL databases support various data models, including document-oriented, key-value pairs, wide-column stores, and graph databases. This diversity allows developers to choose the most appropriate model for their specific application requirements.

Flexibility in Data Representation:
Benefit: NoSQL databases allow for diverse data representations within the same database, enabling developers to store and retrieve data in ways that suit their application needs. This is especially beneficial in dynamic and evolving environments.

Cost-Effective Scaling:
Benefit: Horizontal scaling, a common feature of NoSQL databases, allows organizations to scale their infrastructure more cost-effectively by adding commodity hardware as needed, rather than relying on more expensive vertical scaling.

Useful for Agile Development:
Benefit: NoSQL databases support agile development practices by accommodating changes to the data model without requiring extensive modifications to the database schema. This is beneficial in fast-paced development environments.

Better Handling of Unstructured Data:
Benefit: NoSQL databases are well-suited for scenarios where data is semi-structured or unstructured. They can handle diverse data types, making them suitable for applications dealing with content management, social media, and real-time data.

## How to query information from a NoSQL database
Querying information from a NoSQL database depends on the type of NoSQL database you are using, as different types (document-oriented, key-value stores, column-family stores, etc.) have distinct query languages or methods. Here, I'll provide a general overview based on common NoSQL database types:

1. **Document-Oriented Databases (e.g., MongoDB):**

   - **Query Language:** MongoDB uses a query language that is similar to JSON and supports various operators.
   
   - **Example Query:**
     ```javascript
     // Find documents where the "name" field is "John"
     db.users.find({ name: "John" });

     // Find documents with an age greater than 25
     db.users.find({ age: { $gt: 25 } });
     ```

2. **Key-Value Stores (e.g., Redis):**

   - **Query Method:** Key-value stores are typically simple and retrieve data based on keys.
   
   - **Example Query:**
     ```redis
     // Get the value associated with the key "user:123"
     GET user:123
     ```

3. **Column-Family Stores (e.g., Apache Cassandra):**

   - **Query Language:** Cassandra uses CQL (Cassandra Query Language), which resembles SQL but is adapted for a distributed, non-relational environment.
   
   - **Example Query:**
     ```sql
     // Select data from the "users" table
     SELECT * FROM users WHERE user_id = '123';
     ```

4. **Graph Databases (e.g., Neo4j):**

   - **Query Language:** Graph databases use query languages optimized for traversing and querying graph structures.
   
   - **Example Query:**
     ```cypher
     // Find friends of a user in a social network
     MATCH (user:User {id: '123'})-[:FRIENDS_WITH]->(friend:User) RETURN friend;
     ```

5. **Object-Oriented Databases (e.g., db4o):**

   - **Query Language:** Object-oriented databases may use a query language or API specific to the programming language.
   
   - **Example Query (using Java API):**
     ```java
     // Query to retrieve all instances of the User class
     ObjectSet<User> result = db.queryByExample(User.class);
     ```

It's essential to refer to the documentation of the specific NoSQL database you are using for detailed information on its query language or methods. Keep in mind that NoSQL databases often have different querying approaches compared to traditional SQL databases, as they are optimized for specific data models and use cases.

## How to insert/update/delete information from a NoSQL database
Inserting, updating, and deleting information from a NoSQL database varies depending on the type of NoSQL database you are using. Here are general guidelines for common NoSQL database types:

1. **Document-Oriented Databases (e.g., MongoDB):**

   - **Insert:**
     ```javascript
     // Insert a new document into the "users" collection
     db.users.insert({ name: "Alice", age: 30, email: "alice@example.com" });
     ```

   - **Update:**
     ```javascript
     // Update the document where the "name" is "Alice"
     db.users.update({ name: "Alice" }, { $set: { age: 31 } });
     ```

   - **Delete:**
     ```javascript
     // Delete the document where the "name" is "Alice"
     db.users.remove({ name: "Alice" });
     ```

2. **Key-Value Stores (e.g., Redis):**

   - **Insert/Update:**
     ```redis
     // Set a key-value pair
     SET user:123 '{"name": "John", "age": 25}'
     ```

   - **Delete:**
     ```redis
     // Delete a key
     DEL user:123
     ```

3. **Column-Family Stores (e.g., Apache Cassandra):**

   - **Insert/Update:**
     ```sql
     // Insert or update data in the "users" table
     INSERT INTO users (user_id, name, age) VALUES ('123', 'John', 25);
     ```

   - **Delete:**
     ```sql
     // Delete a row from the "users" table
     DELETE FROM users WHERE user_id = '123';
     ```

4. **Graph Databases (e.g., Neo4j):**

   - **Insert:**
     ```cypher
     // Create a new user node
     CREATE (user:User {id: '123', name: 'John', age: 25});
     ```

   - **Update:**
     ```cypher
     // Update the properties of a user node
     MATCH (user:User {id: '123'}) SET user.age = 26;
     ```

   - **Delete:**
     ```cypher
     // Delete a user node and relationships
     MATCH (user:User {id: '123'}) DETACH DELETE user;
     ```

5. **Object-Oriented Databases (e.g., db4o):**

   - **Insert:**
     ```java
     // Insert a new instance of the User class
     User user = new User("123", "John", 25);
     db.store(user);
     ```

   - **Update:**
     ```java
     // Update the properties of a User instance
     User user = db.queryByExample(new User("123")).next();
     user.setAge(26);
     db.store(user);
     ```

   - **Delete:**
     ```java
     // Delete a User instance
     User user = db.queryByExample(new User("123")).next();
     db.delete(user);
     ```

Always refer to the specific documentation of the NoSQL database you are using for detailed and database-specific syntax for insert, update, and delete operations. The examples provided here are generalized, and syntax may vary based on the actual database system.

## How to use MongoDB
Using MongoDB involves several steps, including installation, connecting to the database, performing CRUD (Create, Read, Update, Delete) operations, and managing the database. Here's a general guide to get you started with MongoDB:

### 1. Install MongoDB:

#### On Windows:

1. Download the MongoDB Community Edition installer from the official website: [MongoDB Download Center](https://www.mongodb.com/try/download/community).
2. Run the installer and follow the installation wizard.
3. MongoDB Compass, a graphical user interface, is included in the installation.

#### On macOS:

1. Install MongoDB using Homebrew:
   ```bash
   brew tap mongodb/brew
   brew install mongodb-community
   ```
2. Start the MongoDB server:
   ```bash
   brew services start mongodb-community
   ```

#### On Linux (Ubuntu):

1. Follow the official installation guide for MongoDB on Ubuntu: [Install MongoDB Community Edition on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/).

### 2. Connect to MongoDB:

1. Open a terminal or command prompt.
2. Start the MongoDB shell:
   ```bash
   mongo
   ```
3. By default, MongoDB connects to a server running on `localhost` at port `27017`.

### 3. Basic CRUD Operations:

#### Create (Insert) Data:

```javascript
// Switch to a specific database or create a new one
use mydatabase

// Insert a document into a collection
db.mycollection.insertOne({ name: "John", age: 25, city: "New York" })
```

#### Read Data:

```javascript
// Find all documents in a collection
db.mycollection.find()

// Find documents with a specific condition
db.mycollection.find({ name: "John" })
```

#### Update Data:

```javascript
// Update a document
db.mycollection.updateOne({ name: "John" }, { $set: { age: 26 } })
```

#### Delete Data:

```javascript
// Delete a document
db.mycollection.deleteOne({ name: "John" })
```

### 4. MongoDB Compass (GUI):

1. Open MongoDB Compass.
2. Connect to the MongoDB server using the default connection settings.
3. Explore databases, collections, and perform CRUD operations using the GUI.

### 5. Additional Concepts:

- **Indexing:** Create indexes to improve query performance.
- **Aggregation:** Use the aggregation framework for complex queries.
- **Authentication:** Secure your MongoDB deployment with authentication.

### 6. Resources:

- [MongoDB Official Documentation](https://docs.mongodb.com/)
- [MongoDB University](https://university.mongodb.com/): Free courses to deepen your MongoDB knowledge.

Remember that this is a simplified guide, and it's crucial to refer to the MongoDB documentation for more detailed and up-to-date information.
