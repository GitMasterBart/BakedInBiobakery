# BakedInBiobakery

![Flowchart application](static/img/flowchart/flowchart.png)
*Figure1: Shows the functionality of the application. The different colored arrows show which processes belong together.*

## Introduction


All around the world computational genomics is growing. This brings a lot of necessary analytical potential, because the computational power and collected data are still increasing. With the growth of these techniques comes an explosion in usage. The result of this is that the last decades many mainly open-source initiative appeared with the main goal of making it easier to analyze genomic-data. One of the possibilities is large-scale analysis of gene-expression data.

Large-scale analysis of gene-expression data can be important for sustainable water technologies, and safety. This analysis can be used for answering questions as: which genes in organisms are upregulated. With the information of which genes are upregulated, it can be determent which metabolic pathways become more active when changes in the environment occur. An example of this is the analyzation of toxic potential of chemical pollutants in water with Caenorhabditis elegans. Once it has been determined which genes have an increased expression. The metabolic pathways in which these genes are involved can be identified. Because Caenorhabditis elegans shares many genetic functions with mammals, including genes that influence the metabolism of xenobiotics. The two main screening methods for large-scale analysis of gene-expression data are: microarrays and RNA-seq. This latter is a based on next generation sequencing and if often referred to as transcriptome profiling.  

RNA-seq became popular a decade later than microarrays and is part of the next generation sequencing technologies that have arisen. It offers an advantage over microarrays by a lack of pre-selecting genes of interest, and instead, total RNA sequencing determines all the transcribed RNA are present in each sample at the moment of sampling. RNA-seq is more useful than microarrays for measuring transcript abundance, identifying transcripts, to improve annotation of genes, and de novo transcript assembly (Pevsner, 2015, p. 479). As stated earlier, in the context of a research center focused on water quality, water safety and sustainability, it is interesting to determine which microbial processes are at play in water. This can be in the scope of constructing a phylogenic tree or active metabolic pathways and their influence on important processes in water technology or water safety. Since there is increasing interest among people in using transcriptomics, it would be great if these tools are available in a way that makes them more accessible. To researchers with a wide variety of backgrounds, ranging from biologists to chemical engineers without biology backgrounds nor trained in programming languages, it would be beneficial if analytical tools could be easily used via access to a graphical interface that supports an analytical pipeline.

 In this project, I am using existing software to build a user-friendly pipeline with great flexibility to visualize and analyze the data through a Web User Interface or WUI. This approach can be easily made user friendly, in combination with a complete and easy to understand manual about the workings of the implemented code from the bio-bakery. For this path to be truly effective the combination of frameworks and programming languages must be written in a regulated manner. This will make maintenance and expanding possible.



## Usage

**Not User Ready.**

### Virtualenv Usage
For installing the virtualenv that includes all the necessary packages: use 
 ```
 $ virtualenv Bio-bakeryHumanNtoolenv
$ source <env_name>/bin/activate
(<env_name>)$ pip install -r Bio-bakeryHumanNtoolenv.txt
 ```

[^1]: Karengera, A., Sterken, M. G., Kammenga, J. E., Riksen, J. A. G., Dinkla, I. J. T., & Murk, A. J. (2022). Differential expression of genes in c. elegans reveals transcriptional responses to indirect-acting xenobiotic compounds and insensitivity to 2,3,7,8-tetrachlorodibenzodioxin. Ecotoxicology and Environmental Safety, 233. https://doi.org/10.1016/j.ecoenv.2022.113344

[^2]: Pevsner, J. (2015). Bioinformatics and Functional Genomics. Third Edition. In Briefings in Functional Genomics and Proteomics.