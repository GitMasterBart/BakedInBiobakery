
# BakedInBiobakery

*Contact:*

*Author: Bart Engels*
<br>
*Website: www.bartengels.eu*
<br>
*Email: b.engels@bioinf.nl*
<br>
*Version: v1*
## Table of Contents

1. [Intent](#intent)
2. [Getting ready for using](#usage)
   1. [Getting it on your computer](#getting_start)
   2. [Make it work](#make_it_work)
      1. [Packages](#packages)
      2. [Pathways](#pathways)
   3. [Testing](#testing)
3. [Using it](#using)
  1. [Adding your initials to db](#adding_int)
  2. [Starting using the application](#Starting)
4. [Dashboard](#dashboard)
5. [References](#bibliografie)



![Flowchart application](static/img/flowchart/flowchart.png)
*Figure1: Shows the functionality of the application. The different colored arrows show which processes belong together.*

<a name="intent"></a>
## 1) Intent

Transcriptome data shows which genes are activated, and to what extent these genes are active at the time of measurement [^2]. By analyzing transcriptomic data for multiple samples of interest, it is possible to see if there are changes or differences in gene expression. When in environment, an organism can up- or down regulated genes to cope with changing conditions. If this is done under controlled conditions, changes in gene expression can be related to the changes in the environment. In this way, the influence of substances on organisms in an environment can be investigated. In this project, I developed the BakedinBiobakery workflow that makes it possible, for users unexperienced with a command-line interface, to perform full transcriptomics data analysis based on functional profiling in metagenomics in the form of  a Web-user-Interface (WUI).  BakedinBiobakery utilizes three software parts: The first is a WUI that is built in a python-based framework in which the user can start a workflow. The application is named BakedinBiobakery because the biobakery toolkit with its HumaNn (v3.0) [^1] function is the foundation of the workflow. The second software package is a workflow written in Snakemake a python-based workflow manager and is called SnakePipeMultiHumaNn. This part runs both the transcriptomic data analysis and subsequent parsing of the results into a database. The third part is a software package that adds a dashboard written in R-Shiny for visualization and is named BakedinBiobakeryShinyDashboard. 
### 1.1 styling application
The interface is styled using a module that is a broadened version Bootstrap   called Material Design for Bootstrap (MDB).  This makes is possible to style your webpage with their styling objects. It is an easier and faster way of styling interfaces. Bootstrap already surplice a lot of possible styling options but because MDB is an extension on Bootstrap it has more options for styling. The downside is that it takes a lot of storage space. 
But because it was necessary to alter some standard styling object for the Bakedinbiobakery, the whole package is included in the repository. This also makes it more usable.

<a name="usage"></a>
## 2) Getting ready for using

<a name="getting_start"></a>
### 2.1) Getting it on your computer

First clone the both the BakedinBiobakery and the SnakePipeMultiHumaNn set the SnakePipeMultiHumaNn in the `biobakery/appModels` directory : 
```shell
 $ git clone https://github.com/GitMasterBart/BakedInBiobakery.git
 $ cd biobakery/appModels 
 $ git clone https://github.com/GitMasterBart/SnakePipeMultiHumaNn.git
 ```
<a name="make_it_work"></a>
### 2.2) Make it work
<a name="packages"></a>
#### 2.2.1) Packages

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

**Needed databases**

* Trimmomatic
* Silvadb 
* Choclophlan
* Uniref

If it does not work to get bowtie on your system, use:

*For linux:*
``
sudo apt-get install bowtie 
``

*For mac:*
``su apt-get install bowtie``

<a name="pathways"></a>
#### 2.2.2) Pathways

Go to the file `Patways.py`. This file contains al the packages that are used in this application. 
Set all the pathways to the location of the file that is asked for. Example: 
```python
# html script example
LOCATIONBASHSCRIPTHUMAN = "[PATH_TO_PROJECT]/BakedInBiobakery/static/sh_scripts/HumanBashStarter.sh"

# database example
LOCATIONUNIREFFPULLDATABASE = "homes/user/database_map/unirefdatabase"
```

After changing all the pathways in the `Patways.py` file you need tho change the file paths in the scripts `static/sh_scripts/`. 
The pathways that are set in the sh-file look like this:
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
<p>It is alos possible to change the <code>--cores n</code> and <code>--jobs n</code> </p>
<code> snakemake --cluster "sbatch" --cores n --jobs n  --config inputfiles=$1 name=$2 user_index=$3 research_index=$4 dataset=$5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15} ${16} &</code>
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

Now migrate the structure the models to the database, this can be done by using the following query's: 

```shell
$ python manage.py makemigrations

$ python manage.py migrate
```

***note:** If it does not work activate the virtual environment*


if you have done this, the program will be ready running. 

type in your terminal: 

```shell 
$ python manage.py runserver
```
*make sure that you are in the **root** map, and that the venv is **activated.***
*Reminder: `source [path_to_venv]/bin/activate`*

<a name="testing"></a>
### 2.3) Testing

Now everthing is working try if is works by testing the whole application. This can be done by going to your project folder and start the testcase.

```shell
$ python manage.py test -v2
```
***note:** the `-v` stands for verbosity this determines how manny feedback you will get from the terminal.*

<h4>Now that you have installed everything for the Django project part. Got to <a href="https://github.com/GitMasterBart/SnakePipeMultiHumaNn"> https://github.com/GitMasterBart/SnakePipeMultiHumaNn </a> and follow the instructions there. </h4>

<a name="using"></a>
## 3) Using it

<a name="adding_int"></a>
### 3.1) Adding your initials to db

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
### 3.2) Starting using the application

After you have singed in, you will be redirected to the upload screen. On this page
you can choose witch parameters you want to use in your pipeline. 

***note:** if you decide to not use the --fastqc-end and --fastqc-start as kneaddata 
variables it will not be possible to evaluate the reads* 

After you have decided witch parameter you want to use, the pipeline will start. 
There are two options: 1) you wil be redirected to a page where the reads can be evaluated. or 2) The complete pipeline will run and the follow text wil be shown: 
"**Great your file is sent to the system..**"

***note:** To make fully use of the application all parameters are recommended (only `--verdose` is really optional)* 

<a name="dashboard"></a>
## 4) Dashboard

To implement the dashboard that uses Maaslin2 to calculate reltations between datapoints. Donwload it from this  [reposetory](https://github.com/GitMasterBart/BakedinBiobakeryShinyDashboard).

or use: 

```{shell}
$ git clone https://github.com/GitMasterBart/BakedinBiobakeryShinyDashboard.git
```

If you want to run it localy you can easly change the `href` pathways to the local server that shiny is running in. These can be found on the on the `html` pages in the `templates` folder.
The templates that contain dashboard are:

* succes_page.html
* inf_page.html
* Upload_form.html
* fastqc_check_page.html


<a name="bibliografie"></a>
*References:*

[^1]: Beghini, F., McIver, L. J., Blanco-Míguez, A., Dubois, L., Asnicar, F., Maharjan, S., Mailyan, A., Manghi, P., Scholz, M., Thomas, A. M., Valles-Colomer, M., Weingart, G., Zhang, Y., Zolfo, M., Huttenhower, C., Franzosa, E. A., & Segata, N. (2021). Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with biobakery 3. ELife, 10. https://doi.org/10.7554/eLife.65088

[^2]: Pevsner, J. (2015). Bsioinformatics and Functional Genomics. Third Edition. In Briefings in Functional Genomics and Proteomics.