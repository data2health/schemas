[![Build Status](https://travis-ci.org/data2health/schemas.svg?branch=biothings)](https://travis-ci.org/data2health/schemas)

# schemas
Hosting CD2H data schemas in schema.org standard

## Branch Description
This branch is about converting biolink model into schema.org compatible format

## Some Comment
1. Everything is either a class/type or property (or maybe enumeration)
2. When defining a class, the following information is required:
  * comment (description)
  * label (always same as the id)
  * subClassOf (its direct parent)
  * equivalentClass (not required)
3. When defining a property, the following information is required:
  * comment (description)
  * label (always same as the id)
  * domainIncludes (relate a property to a class that it is expected to be used on)
  * rangeIncludes (relate a property to a class that constitutes the types for values of the property)
4. Always start from the top level entity, its children is going to inherit all properties of its parents (direct or indirect)
5. 
