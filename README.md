# Bioinformatics
Bioinformatics

learn from dataprofessor Chanin Nantasenamat.
Python for Bioinformatics - Drug Discovery Using Machine Learning and Data Analysis
2022.12.10


### fix the token
```
git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git

```


In the above command make sure to replace:

<githubtoken> with the personal access token you have copied in the previous step
<username> with your GitHub username
<repositoryname> with the name of your GitHub repository

```
git push
```


### command line
```
git clone 
git add * 
git git commit -m 'Initial project version,and information about where i learned.'
```


```
git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git
```
```
git push -u origin main
```


### log
1. get data.
2. preprocess. 
3. building modle. 
4. show result. 
5. compare results.
2022.12.13. 

## 1.1 ex1
```
pip install chembl_webresource_client
```

ex1_main.py
```
# Import necessary libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client



### problems: about MKL

MKL is Intel's "Math Kernel Library", and it basically handles calculations. The new version of Numpy uses MKL by default, and that is likely why this error is showing up.

Try to update numpy,

conda update numpy
or disable MKL by

conda install nomkl
Hope that helped! Reference: https://github.com/BVLC/caffe/issues/3884

```

### fix conda deactive problem
```
while [ ! -z $CONDA_PREFIX ]; do conda deactivate; done
```
can work. deactive base env.
