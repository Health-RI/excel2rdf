## Introduction
**excel2rdf** is a workflow designed to generate a Turtle (.ttl) file from a metadata schema provided in CSV format.

## Target Audience
The current primary users are within Health RI.

## Requirements
Basic familiarity with Git, including committing via the command line or GitHub Desktop.

## How to Use
When a metadata schema (CSV file) is pushed to the `metadata` folder, the workflow automatically converts it into a SHACL shape by utilizing the [SKOS Play API](https://xls2rdf.sparna.fr/rest/). The resulting Turtle (.ttl) file is saved in the `turtle` folder.

### CSV File Template
A template for the metadata schema is currently under discussion.

---
