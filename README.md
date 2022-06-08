# BakedInBiobakery

## Table of Contents

1. [Intent](#intent)
2. [Getting ready for using](#usage)
   1. [Getting it on your computer](#getting_start)
   2. [Make it work](#make_it_work)
      1. [Packages](#packages)
      2. [Pathways](#pathways)
   3. [Testing](#testing)
   4. [Using it](#using)
      1. [Adding your initials to db](#adding_int)
      2. [Starting using the application](#Starting)
3. [Bibliografie](#bibliografie)


![Flowchart application](static/img/flowchart/flowchart.png)
*Figure1: Shows the functionality of the application. The different colored arrows show which processes belong together.*

<a name="intent"></a>
## Intent

The Biobakery is a tool package that facilitates the analysis of transcriptome data (Beghini et al., 2021)[^1]. Transcriptome data shows which genes are active, and to what extent these genes are active at the time of measurement (Pevsner, 2015, p. 479) [^2]. By doing this for multiple samples of interest, it is possible to see if there are changes or differences in gene expression. When there are changes in an environment, genes can be up- or down regulated. If this is done in a controlled environment, the changes in gene expression can be related to the changes in the environment. In this way, the influence of substances on organisms in an environment can be investigated. 
 
The Biobakery is made for use in a non-graphical environment. For the average user, this is not advantageous in terms of usability. Therefore, it is common for students and even for professionals not to use these tools. 
To help encourage more people to work with these tools, the idea was conceived to create an usable application around. The purpose of this application is not only to run the tools, but also to store the output data in a smart, easy-to-access and easy-to-interpret way.

<a name="usage"></a>
## Getting ready for using

<a name="getting_start"></a>
### 1) Getting it on your computer
**Not User Ready.**

First clone the both the BakedinBiobakery and the SnakePipeMultiHumaNn set the SnakePipeMultiHumaNn in the `biobakery/appModels` directory : 
```shell
 $ git clone https://github.com/GitMasterBart/BakedInBiobakery.git
 $ cd biobakery/appModels 
 $ git clone https://github.com/GitMasterBart/SnakePipeMultiHumaNn.git
 ```
<a name="make_it_work"></a>
### 2) Make it work
<a name="packages"></a>
#### 2.1) Packages

Now create a virtual enviorement (venv/conda). And install
all the following packages. 

```shell
$ pip install [package]
```
or 

```shell
$ conda install [package]
```

**For running django:**
* Django
* pymsql
* Mysql (or another database server)

**Used for the biobakery snakefile-pipeline:** 
* human
* kneaddata
* bowtie2 

If it does not work to get bowtie on your system, use:

*For linux:*
``
sudo apt-get install bowtie 
``

*For mac:*
``su apt-get install bowtie``

<a name="pathways"></a>
#### 2.2) Pathways

Go to the file `Patways.py`. This file contains al the packages that are used in this application. 
Set all the pathways to the location of the file that is asked for. Example: 
```python
# html script example
LOCATIONBASHSCRIPTHUMAN = "[PATH_TO_PROJECT]/BakedInBiobakery/static/sh_scripts/HumanBashStarter.sh"

# database example
LOCATIONUNIREFFPULLDATABASE = "homes/user/database_map/unirefdatabase"
```

After changing all the pathways in the `Patways.py` file you need tho change the file paths in the scripts `static/sh_scripts/`. 
The pathways that are set in this file look like:
```shell
source [PATWAY_TO_VENV]

cd [PATWAY_TO_SNAKEMAKE_FILE]
```
<details>
  <summary><b>Extra options: <u>Slurm</u> in snakefile query:</b></summary>
  <p>If you want to use slurm a snakefile add "sbatch" like this:</p>
<code>snakemake --cluster "sbatch" --cores 2 --jobs 200 --config inputfiles=$1 name=$2 user_index=$3 research_index=$4 dataset=$5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15} ${16} &
 </code> 
<p>There are also options for adding more details to your sbatch syntax: </p>
<code> --cluster "sbatch -A {cluster.account} -p {cluster.partition} -n {cluster.n}  -t {cluster.time}"</code>
</details>

To use databases first you need to create a database, as a tip call this database `biobakery`. when this dabase is created 
you need to add a department to the department table in this case call this department: `Microbiologie`. 
Now it is time for the next step: fill in `djangoProject/settings.py.DATABASES` as shown below: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': [NAME_DATABASE],
        'USER': [NAME_USER],
        'PASSWORD': [PASSWORD],
        'HOST': [SERVER],
        'PORT': [PORT],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

if you have done this, the program will be ready running. 

type in your terminal: 

```shell 
$ python manage.py runserver
```
*make sure that you are in the **root** map, and that the venv is **activated***
*reminder `source [path_to_venv]/bin/activate`*

<a name="testing"></a>
### 3) Testing

Now everthing is working try if is works by testing the whole application. This can be done by going to your project folder and start the testcase.

```shell
$ python manage.py test -v2
```
***note:** the `-v` stands for verbosity this determines how manny feedback you will get from the terminal.*

<a name="using"></a>
### 4) Using it

<a name="adding_int"></a>
#### 4.1) Adding your initials to db

I understand that you are trilled to use this web-application, but first we need you to add yourself as a user.
This can be done in on the page `addUsers`. If it runs on your localhost you can find it under: 
```http request
http://127.0.0.1:8000/biobakery/addUser
``` 
You can also just go to `http://127.0.0.1:8000/biobakery/Home` and click on "Your initials 
are not there?" in the sign in screen.

Now that you have added yourself to the database the application can be used. 

***note:** it can take a while before the pages are refreshed and your name shows op in the sing in screen.*

<a name="Starting"></a>
#### 4.2) Starting using the application

After you have singed in, you will be redirected to the upload screen. On this page
you can choose witch parameters you want to use in your pipeline. 

***note:** if you decide to not use the --fastqc-end and --fastqc-start as kneaddata 
variables it will not be possible to evaluate the reads* 

After you have decided witch parameter you want to use, the pipeline will start. 
There are two options: 1) you wil be redirected to a page where the reads can be evaluated. or 2) The complete pipeline will run and the follow text wil be shown: 
"**Great your file is sent to the system, 
when the chosen tool is finished with all the hard work 
you wil get a message.**"

***note:** To make fully use of the application all parameters are recommended (only `--verdose` is really optional)* 

<a name="bibliografie"></a>
*Bibliografie:*

[^1]: Beghini, F., McIver, L. J., Blanco-Míguez, A., Dubois, L., Asnicar, F., Maharjan, S., Mailyan, A., Manghi, P., Scholz, M., Thomas, A. M., Valles-Colomer, M., Weingart, G., Zhang, Y., Zolfo, M., Huttenhower, C., Franzosa, E. A., & Segata, N. (2021). Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with biobakery 3. ELife, 10. https://doi.org/10.7554/eLife.65088

[^2]: Pevsner, J. (2015). Bsioinformatics and Functional Genomics. Third Edition. In Briefings in Functional Genomics and Proteomics.