To effectively represent "reference" or "master" data (taxonomies, controlled vocabulary, data dictionaries, etc.) in a relational model, a well-structured approach is crucial. Reference data typically consists of predefined values used across the system, ensuring consistency, standardization, and efficient data management. 

## Context

### 1. Understand the Types of Reference Data

Reference data can generally be categorized into two types:

1. **Static Reference Data:** Rarely changes over time, such as country codes, currency codes, and status codes.
2. **Dynamic Reference Data:** Changes more frequently, such as exchange rates, tax rates, and organizational hierarchies.

### 2. Define the Requirements

Before designing the relational model, define the requirements:
- **Scope:** Determine the types of reference data to be managed.
- **Usage:** Identify how and where the reference data will be used.
- **Maintenance:** Establish the processes for updating and maintaining reference data.
- **Constraints:** Identify any constraints, such as referential integrity and uniqueness.


## Design and Implementation

### 3. Design the Tables

#### 3.1. Reference Data Tables

For each type of reference data, create a dedicated table. These tables should have the following characteristics:

- **Primary Key:** A unique identifier for each entry.
- **Descriptive Columns:** Columns that store the reference data values.
- **Metadata Columns:** Optional columns for additional metadata (e.g., descriptions, effective dates, expiry dates).

Example:

```sql
CREATE TABLE Country (
    CountryCode CHAR(3) PRIMARY KEY,
    CountryName VARCHAR(100) NOT NULL
);

CREATE TABLE Currency (
    CurrencyCode CHAR(3) PRIMARY KEY,
    CurrencyName VARCHAR(100) NOT NULL,
    Symbol CHAR(3) NOT NULL
);
```

#### 3.2. Hierarchical Reference Data

For hierarchical reference data (e.g., taxonomies), use a parent-child relationship within the same table or separate tables.

Example:

```sql
CREATE TABLE Category (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    ParentCategoryID INT NULL,
    FOREIGN KEY (ParentCategoryID) REFERENCES Category(CategoryID)
);
```

### 4. Implement Relationships

#### 4.1. Foreign Keys

Use foreign keys to establish relationships between reference data tables and other tables in the database. This ensures referential integrity.

Example:

```sql
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    CurrencyCode CHAR(3),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (CurrencyCode) REFERENCES Currency(CurrencyCode)
);
```

#### 4.2. Composite Keys

For composite reference data, where a combination of columns forms a unique identifier, use composite primary keys.

Example:

```sql
CREATE TABLE TaxRate (
    CountryCode CHAR(3),
    EffectiveDate DATE,
    TaxRate DECIMAL(5, 2),
    PRIMARY KEY (CountryCode, EffectiveDate)
);
```

### 5. Normalize the Data

Ensure that the reference data is normalized to reduce redundancy and improve data integrity. Follow the principles of normalization (1NF, 2NF, 3NF) to structure the data efficiently.

### 6. Implement Constraints and Indexes

#### 6.1. Unique Constraints

Ensure that certain columns, or combinations thereof, remain unique.

Example:

```sql
ALTER TABLE Country ADD CONSTRAINT UQ_CountryName UNIQUE (CountryName);
```

#### 6.2. Indexes

Create indexes to improve query performance, especially on columns frequently used in WHERE clauses or JOIN operations.

Example:

```sql
CREATE INDEX IDX_Product_CategoryID ON Product (CategoryID);
```

### 7. Manage Data Changes

#### 7.1. Auditing

Implement auditing mechanisms to track changes in reference data.

Example:

```sql
CREATE TABLE CurrencyAudit (
    AuditID INT PRIMARY KEY,
    CurrencyCode CHAR(3),
    OldCurrencyName VARCHAR(100),
    NewCurrencyName VARCHAR(100),
    ChangeDate DATETIME,
    ChangedBy VARCHAR(100)
);
```

#### 7.2. Versioning

For dynamic reference data, consider versioning to maintain historical records.

Example:

```sql
CREATE TABLE CurrencyVersion (
    VersionID INT PRIMARY KEY,
    CurrencyCode CHAR(3),
    CurrencyName VARCHAR(100),
    EffectiveDate DATE,
    ExpiryDate DATE
);
```

### 8. Optimize Data Access

#### 8.1. Caching

Implement caching mechanisms for frequently accessed reference data to reduce database load.

#### 8.2. Denormalization

In some cases, denormalization might be necessary to optimize read performance, but it should be done carefully to avoid compromising data integrity.

### 9. Maintain Data Quality

#### 9.1. Data Validation

Implement validation rules to ensure the accuracy and consistency of reference data.

#### 9.2. Data Cleansing

Regularly cleanse reference data to remove duplicates and correct errors.

### 10. Documentation

Document the reference data model, including the structure, relationships, constraints, and any business rules or processes associated with maintaining the data.

### Example Implementation

Here's a comprehensive SQL implementation based on the concepts discussed:

```sql
-- Country Table
CREATE TABLE Country (
    CountryCode CHAR(3) PRIMARY KEY,
    CountryName VARCHAR(100) NOT NULL
);

-- Currency Table
CREATE TABLE Currency (
    CurrencyCode CHAR(3) PRIMARY KEY,
    CurrencyName VARCHAR(100) NOT NULL,
    Symbol CHAR(3) NOT NULL
);

-- Category Table with Hierarchy
CREATE TABLE Category (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    ParentCategoryID INT NULL,
    FOREIGN KEY (ParentCategoryID) REFERENCES Category(CategoryID)
);

-- Product Table with Foreign Keys
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    CurrencyCode CHAR(3),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (CurrencyCode) REFERENCES Currency(CurrencyCode)
);

-- TaxRate Table with Composite Key
CREATE TABLE TaxRate (
    CountryCode CHAR(3),
    EffectiveDate DATE,
    TaxRate DECIMAL(5, 2),
    PRIMARY KEY (CountryCode, EffectiveDate)
);

-- Indexes for Performance
CREATE INDEX IDX_Product_CategoryID ON Product (CategoryID);

-- Unique Constraints
ALTER TABLE Country ADD CONSTRAINT UQ_CountryName UNIQUE (CountryName);

-- Auditing Table
CREATE TABLE CurrencyAudit (
    AuditID INT PRIMARY KEY,
    CurrencyCode CHAR(3),
    OldCurrencyName VARCHAR(100),
    NewCurrencyName VARCHAR(100),
    ChangeDate DATETIME,
    ChangedBy VARCHAR(100)
);

-- Versioning Table
CREATE TABLE CurrencyVersion (
    VersionID INT PRIMARY KEY,
    CurrencyCode CHAR(3),
    CurrencyName VARCHAR(100),
    EffectiveDate DATE,
    ExpiryDate DATE
);
```

## References

See also: [[Taxonomies vs. Ontologies]]