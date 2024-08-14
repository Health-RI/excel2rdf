# excel2rdf
In this repository, a workflow is developed to automate the process from a metadata schema (in csv format) to rdf output (ttl file). 

When a metadata schema is published to metadata folder in this repository, the workflow starts to transfer it into schacl shape by calling SKOS play(https://skos-play.sparna.fr/play/convert). The output ttl is in schacl folder.
