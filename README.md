# excel2rdf
A workflow to generate ttl file using a metadata schema (in csv format) as input. 

Requirements:
Basic knowledge of using Git commit (via cmd line or Github desktop)

When a metadata schema is pushed to the metadata folder, the workflow starts to transfer it into schacl shape by calling [SKOS play API](https://xls2rdf.sparna.fr/rest/). The output ttl is stored into turtle folder.
