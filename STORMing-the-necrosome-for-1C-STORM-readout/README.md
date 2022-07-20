# Cluster analysis of two-color STORM imaging

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Installing
You can download Fiji and ilastik from the following website.
https://fiji.sc
https://www.ilastik.org/download.html

## Goals and input/output formats

 ### main_Area_ratio.py
 

 - **What it does:** Calculate the area ratio of the two proteins in the overlapping part.
 - **Input:** CSV file containing protein area generated in ImageJ.
 - **Output:** The csv file of the total area of the protein, visualization file, the csv file of the ratio of the area of the two proteins in the overlapping part, the csv file of the detailed information of the two proteins in the overlapping part.
 
 ### composite_visualization.py
 
 - **What it does:** Assess whether the overlap between two proteins is reliable.
 - **Input:** Image of the merged two protein channels, the csv file of the ratio of the area of the two proteins in the overlapping part.
 - **Output:** Visualized image of the overlap between two proteins.

### Pre_Class.py

 - **What it does:** Arrange the detailed information of the two proteins in the overlapping part as required to facilitate subsequent protein classification.
 - **Input:** CSV file of the detailed information of the two proteins in the overlapping part.
 - **Output:** The preprocessed csv file of the protein details of the overlap.

## Example of use
First you will need to open the Protein image processed by ilastik you want to analyse using the **Fetch.ijm** macro. Just run the macro, chose your folder.
Then run **main_Area_ratio.py** to obtain the area ratio and detailed information of the two proteins in the overlap.
Finally Run **Pre_Class.py** and use the result files after the run to perform protein classification.

## Authors

 - **Xin Chen:** xchen@xmu.edu.cn
 - **Rongfeng Zhu**
 - **Jinjin Zhong**
 - **Yongfa Ying:** 1129205545@qq.com
