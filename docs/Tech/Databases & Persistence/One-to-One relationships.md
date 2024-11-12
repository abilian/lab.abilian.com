In relational database design, choosing where to place foreign keys is essential for maintaining data integrity and ensuring efficient query performance. For one-to-one relationships, the decision on where to place the foreign key can impact both the logical representation of the data and its maintainability. This note aims to clarify best practices for foreign key placement in one-to-one relationships within relational models.

## The One-to-One Relationship: A Brief Overview

A **one-to-one (1:1) relationship** between two tables occurs when a record in one table corresponds to exactly one record in another table, and vice versa. This relationship can be thought of as an extension of a single entity split across two tables, often used when separating optional or detailed attributes of an entity.

For example, you might have a `Person` table that holds basic information (e.g., `id`, `name`), and a `PersonDetails` table that holds additional information like an address, date of birth, or social security number. Every person in the `Person` table corresponds to one unique entry in the `PersonDetails` table, and vice versa.

The question arises: **On which table should the foreign key be placed to enforce this one-to-one relationship?**

## Option 1: Place the Foreign Key in the Dependent Table

In most cases, the foreign key should be placed in the table that is conceptually dependent or optional. This table often holds data that can be considered an extension of the primary table’s information.

Consider a `Person` and `Passport` relationship, where each person can have only one passport, and a passport cannot exist without a person:

```sql
CREATE TABLE Person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Passport (
    id INT PRIMARY KEY,
    person_id INT UNIQUE,
    passport_number VARCHAR(50),
    FOREIGN KEY (person_id) REFERENCES Person(id)
);
```

Here, the `Passport` table contains the foreign key (`person_id`) that points to the `Person` table. The `Passport` table is dependent on the `Person` table, which means a passport cannot exist without a corresponding person. Additionally, the `person_id` is marked as `UNIQUE`, ensuring that no two passports can be assigned to the same person, thus enforcing the one-to-one relationship.

## Option 2: Combine Both Tables and Place the Foreign Key in Either

In some scenarios, the relationship is truly symmetric, meaning both entities are equally important and neither is "more optional" than the other. In such cases, either table can hold the foreign key. However, it’s crucial to enforce uniqueness on the foreign key column to maintain the one-to-one constraint.

Let’s take an example with an `Employee` and `EmployeeDetails` table. Each employee has one corresponding record in `EmployeeDetails`, and no more than one:

```sql
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE EmployeeDetails (
    id INT PRIMARY KEY,
    employee_id INT UNIQUE,
    bio TEXT,
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);
```

In this case, the `EmployeeDetails` table holds a foreign key (`employee_id`) that references the `Employee` table. The uniqueness constraint (`UNIQUE`) on `employee_id` ensures that each employee has only one entry in the `EmployeeDetails` table.

## Key Considerations for Foreign Key Placement

When deciding where to place the foreign key in a one-to-one relationship, consider the following factors:

1. **Business Logic**:
   - If one table logically depends on the other, place the foreign key in the dependent table. For example, if `Passport` depends on `Person`, the foreign key should be in the `Passport` table.

2. **Optionality**:
   - In some cases, one of the entities may be optional. For example, not every `Person` has a `Passport`. In this case, it makes sense to put the foreign key in the `Passport` table because the existence of a `Passport` depends on the existence of a `Person`.

3. **Uniqueness**:
   - Ensure the foreign key column is unique, as the relationship implies that no two rows in one table can point to the same row in the other table. This can be enforced with a `UNIQUE` constraint or unique index on the foreign key column.

4. **Nullability**:
   - If the relationship allows for an entity to exist without a corresponding entry in the related table, the foreign key should be nullable. For example, a `Person` may exist without a `Passport`, meaning the `person_id` in the `Passport` table could be nullable.

5. **Performance and Querying**:
   - Placing the foreign key in the appropriate table can make queries more intuitive and performant. For example, if you're frequently querying information about passports for a given person, it may make sense to have the foreign key on the `Passport` table, making the join operations more efficient.

## Conclusion

In a one-to-one relationship, placing the foreign key in the correct table depends on understanding the nature of the relationship between the entities. If one entity logically extends the other or depends on it, the foreign key should be placed in the dependent table. If the relationship is truly symmetric, either table can hold the foreign key, provided that a `UNIQUE` constraint is applied to enforce the one-to-one rule.

By properly analyzing the relationship and ensuring the integrity constraints are enforced, you can design efficient and logically sound relational database schemas that align with the business rules of your application.

<!-- Keywords -->
#relational
<!-- /Keywords -->
