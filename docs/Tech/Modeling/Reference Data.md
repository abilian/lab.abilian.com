To effectively represent "reference" or "master" data (taxonomies, controlled vocabulary, data dictionaries, etc.) in a relational model, a well-structured approach is crucial. Reference data typically consists of predefined values used across the system, ensuring consistency, standardization, and efficient data management. 

## Context

### Understand the Types of Reference Data

Reference data can generally be categorized into two types:

1. **Static Reference Data:** Rarely changes over time, such as country codes, currency codes, and status codes.
2. **Dynamic Reference Data:** Changes more frequently, such as exchange rates, tax rates, and organizational hierarchies.

### Define the Requirements

Before designing the relational model, define the requirements:
- **Scope:** Determine the types of reference data to be managed.
- **Usage:** Identify how and where the reference data will be used.
- **Maintenance:** Establish the processes for updating and maintaining reference data.
- **Constraints:** Identify any constraints, such as referential integrity and uniqueness.


## Design and Implementation

### Design the Tables

#### Reference Data Tables

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

#### Hierarchical Reference Data

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

### Implement Relationships

#### Foreign Keys

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

#### Composite Keys

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

### Normalize the Data

Ensure that the reference data is normalized to reduce redundancy and improve data integrity. Follow the principles of normalization (1NF, 2NF, 3NF) to structure the data efficiently.

### Implement Constraints and Indexes

#### Unique Constraints

Ensure that certain columns, or combinations thereof, remain unique.

Example:

```sql
ALTER TABLE Country ADD CONSTRAINT UQ_CountryName UNIQUE (CountryName);
```

#### Indexes

Create indexes to improve query performance, especially on columns frequently used in WHERE clauses or JOIN operations.

Example:

```sql
CREATE INDEX IDX_Product_CategoryID ON Product (CategoryID);
```

### Manage Data Changes

#### Auditing

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

#### Versioning

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

### Optimize Data Access

#### Caching

Implement caching mechanisms for frequently accessed reference data to reduce database load.

#### Denormalization

In some cases, denormalization might be necessary to optimize read performance, but it should be done carefully to avoid compromising data integrity.

### Maintain Data Quality

#### Data Validation

Implement validation rules to ensure the accuracy and consistency of reference data.

#### Data Cleansing

Regularly cleanse reference data to remove duplicates and correct errors.

### Documentation

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

## Worked-out Example

We outline below the design for a universal reference data engine. This involves creating a system that is flexible, scalable, and can cater to various use cases with an object-oriented API and a relational backend. The design must support CRUD operations, hierarchical data, versioning, and extensibility.

### Database Schema Design

#### Core Tables

1. **Reference Data Types Table:**
   - This table defines different types of reference data (e.g., Country, Currency, Status).

   ```sql
   CREATE TABLE ReferenceDataType (
       DataTypeID INT PRIMARY KEY,
       DataTypeName VARCHAR(100) NOT NULL,
       Description TEXT NULL
   );
   ```

2. **Reference Data Table:**
   - This table stores the actual reference data values.

   ```sql
   CREATE TABLE ReferenceData (
       DataID INT PRIMARY KEY,
       DataTypeID INT,
       Code VARCHAR(100) NOT NULL,
       Value VARCHAR(255) NOT NULL,
       ParentDataID INT NULL,
       EffectiveDate DATE NOT NULL,
       ExpiryDate DATE NULL,
       Metadata JSON NULL,
       FOREIGN KEY (DataTypeID) REFERENCES ReferenceDataType(DataTypeID),
       FOREIGN KEY (ParentDataID) REFERENCES ReferenceData(DataID)
   );
   ```

3. **Reference Data Version Table:**
   - This table tracks changes in reference data values.

   ```sql
   CREATE TABLE ReferenceDataVersion (
       VersionID INT PRIMARY KEY,
       DataID INT,
       OldValue VARCHAR(255),
       NewValue VARCHAR(255),
       ChangeDate DATETIME,
       ChangedBy VARCHAR(100),
       FOREIGN KEY (DataID) REFERENCES ReferenceData(DataID)
   );
   ```

### API Design

#### Object-Oriented API

Define classes and methods for interacting with the reference data. Use an ORM (Object-Relational Mapping) framework to bridge the object-oriented API with the relational database.

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class ReferenceDataType(Base):
    __tablename__ = 'ReferenceDataType'
    DataTypeID = Column(Integer, primary_key=True)
    DataTypeName = Column(String, nullable=False)
    Description = Column(String)

class ReferenceData(Base):
    __tablename__ = 'ReferenceData'
    DataID = Column(Integer, primary_key=True)
    DataTypeID = Column(Integer, ForeignKey('ReferenceDataType.DataTypeID'))
    Code = Column(String, nullable=False)
    Value = Column(String, nullable=False)
    ParentDataID = Column(Integer, ForeignKey('ReferenceData.DataID'))
    EffectiveDate = Column(Date, nullable=False)
    ExpiryDate = Column(Date)
    Metadata = Column(JSON)

    data_type = relationship("ReferenceDataType")
    parent_data = relationship("ReferenceData", remote_side=[DataID])

class ReferenceDataVersion(Base):
    __tablename__ = 'ReferenceDataVersion'
    VersionID = Column(Integer, primary_key=True)
    DataID = Column(Integer, ForeignKey('ReferenceData.DataID'))
    OldValue = Column(String)
    NewValue = Column(String)
    ChangeDate = Column(Date)
    ChangedBy = Column(String)

    reference_data = relationship("ReferenceData")

# Database setup
engine = create_engine('sqlite:///reference_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

#### CRUD Operations

Implement methods for CRUD operations.

```python
class ReferenceDataManager:
    def __init__(self, session):
        self.session = session

    def create_data_type(self, name, description=None):
        data_type = ReferenceDataType(DataTypeName=name, Description=description)
        self.session.add(data_type)
        self.session.commit()

    def create_reference_data(self, data_type_id, code, value, effective_date, expiry_date=None, parent_data_id=None, metadata=None):
        ref_data = ReferenceData(
            DataTypeID=data_type_id, Code=code, Value=value, EffectiveDate=effective_date,
            ExpiryDate=expiry_date, ParentDataID=parent_data_id, Metadata=metadata
        )
        self.session.add(ref_data)
        self.session.commit()

    def update_reference_data(self, data_id, new_value, changed_by):
        ref_data = self.session.query(ReferenceData).get(data_id)
        old_value = ref_data.Value
        ref_data.Value = new_value
        self.session.add(ref_data)
        version = ReferenceDataVersion(
            DataID=data_id, OldValue=old_value, NewValue=new_value,
            ChangeDate=datetime.now(), ChangedBy=changed_by
        )
        self.session.add(version)
        self.session.commit()

    def delete_reference_data(self, data_id):
        ref_data = self.session.query(ReferenceData).get(data_id)
        self.session.delete(ref_data)
        self.session.commit()

    def get_reference_data(self, data_type_id, effective_date=None):
        query = self.session.query(ReferenceData).filter_by(DataTypeID=data_type_id)
        if effective_date:
            query = query.filter(
                ReferenceData.EffectiveDate <= effective_date,
                (ReferenceData.ExpiryDate >= effective_date) | (ReferenceData.ExpiryDate.is_(None))
            )
        return query.all()
```

### Implementation for Use Cases

#### Consistent Data Entry

Provide a method to fetch data by type and date, ensuring that only valid entries are used for data entry.

```python
def fetch_valid_reference_data(manager, data_type_name, effective_date=None):
    data_type = session.query(ReferenceDataType).filter_by(DataTypeName=data_type_name).one()
    return manager.get_reference_data(data_type.DataTypeID, effective_date)
```

#### Data Validation

Implement validation logic using the fetched reference data.

```python
def validate_data_entry(manager, data_type_name, code, effective_date=None):
    reference_data = fetch_valid_reference_data(manager, data_type_name, effective_date)
    valid_codes = [data.Code for data in reference_data]
    return code in valid_codes
```

#### Reporting and Analytics

Ensure that reference data used in reports is based on effective dates to maintain accuracy over time.

```python
def generate_report(manager, data_type_name, report_date):
    reference_data = fetch_valid_reference_data(manager, data_type_name, report_date)
    # Perform reporting using the valid reference data
```

#### Data Integration

Provide methods for fetching and synchronizing reference data across systems.

```python
def synchronize_reference_data(manager, external_data):
    for data in external_data:
        existing_data = session.query(ReferenceData).filter_by(Code=data['code']).first()
        if existing_data:
            manager.update_reference_data(existing_data.DataID, data['value'], 'system_sync')
        else:
            manager.create_reference_data(data['type_id'], data['code'], data['value'], data['effective_date'])
```

### Maintenance and Extensibility

#### Adding New Reference Data Types

Extend the system by adding new data types without altering the core architecture.

```python
manager.create_data_type('NewType', 'Description of the new type')
```

#### Handling Hierarchical Data

Ensure hierarchical relationships are managed correctly in the database and API.

```python
manager.create_reference_data(parent_data_id, code, value, effective_date)
```

#### Versioning and Auditing

Automatically track changes and maintain historical versions of reference data.

### Conclusion

This design provides a robust and flexible framework for managing reference data using a relational backend and an object-oriented API. It supports various use cases, ensuring data consistency, integrity, and ease of maintenance. This approach can be further extended and optimized based on specific requirements and system constraints.


## References

See also: [[Taxonomies vs. Ontologies]]
