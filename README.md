# 📉 Air Quality Data Analysis Project (2021 Purdue Univ) 📈

<br>

## 📑 Project Title
> **A Study on the Relationship between Outdoor Air Public Data(ODA) and Indoor Air Measurement Data(IDA) in the United States**

<br/>

## 📅 Project Period
> **10-10-2021(SUN) ~ 12-20-2021(MON)**

<br/>

## 🔍 Problem Statement
 > **Air pollution, such as yellow dust and fine dust, is a problem that all countries and institutions are trying to solve in modern society.**
 >
 > The importance of air quality is a fact that everyone knows well. In addition, the importance of air quality has become more prominent since the COVID-19 pandemic. he U.S. Centers for Disease Control and Prevention (CDC) officially recognizes air transmission as a major transmission route for COVID-19, and the World Health Organization (WHO) also includes air transmission as a COVID-19 transmission route.
 >    
 >With the above importance, many people check outdoor air quality data (fine dust and ultrafine dust concentrations) provided by the government or provided by each institution every day before starting their daily routine. 
 >
 > Nevertheless, it can be said that the general public's interest in indoor air quality is weaker than that of outdoor air quality.
 >    
 >According to the U.S. Environmental Protection Agency, indoor air, where modern people live more than 80% to 90% of the day, is 100 times more polluted than outside air and a study also suggested that indoor air pollutants are 100 times more likely to be delivered to human lungs than air pollutants. The American Lung Association (ALA) also announced that indoor harmful substances are two to five times more than outdoor air and that there are cases of 100 times more harmful substances.  **Analysts say that various chemical components discharged from walls and furniture, beds, pillows, house dust, and dust caused by human movement are combined, polluting indoor air.**
>
>**therefore, we compare major indoor air pollutants and factor data provided by the Environmental Protection Agency (EPA) with data measured directly in the actual indoor environment to see how much difference there is,between external air data provided by countries or institutions and actual indoor air data.**

<br/>

## 📖 Considerations

### 💻 Software Architecture : 
#### 1) Node-Red

It is a flow-based development tool for wiring and visualizing hardware devices as part of the Internet of Things. 
This program can use JavaScript language, which was used because developers who participated in this study can use JavaScript and it is convenient to extract file data in the form of JSON.
    
#### 2) Arduino Integrated development environment

The Arduino integrated development environment is a development environment provided to users for Arduino programming. 
In this study, data values were uploaded without using wireless communication in the form of LAN. When the Arduino MCU was executed, the required value was delivered to UART communication.
    
#### 3) Jupyter notebook

Jupiter Laptop is an open source-based web application. It was used because visualization should be performed in each unit by comparing and analyzing indoor air measurement data and outdoor air public data.
        
### 📡 Hardware Architecture : 

Hardware basically used aurduino uno **rev3(2) , pms 5003 (fine dust sensor), dht 11 (temperature and humidity sensor), mq2 (gas sensor), and mq131 (gas sensor).**

The sensor selection criteria consisted of sensors capable of extracting external air components provided by EPA, and two Arduinoes were used due to the research characteristics in which relatively many sensors were used.


<br/>

## 💡 Novelty

Data comparison analysis of indoor and outdoor air data.

To date, several studies and papers have measured only outdoor data or measured only indoor data to derive and analyze results. However, in this study, there is a process of comparing and analyzing actual indoor air quality data and outdoor air data provided by the state. This may seem relatively simple, but it is a study that has hardly been conducted. There is an accurate measurement goal of pollutant comparison, and it is a study in which time and place are systematically conducted.

<br>




## 📋 System Overview

 <p align="center">
   <img src="https://user-images.githubusercontent.com/63999666/154166528-e93b8a23-4c23-4725-984c-12118b8ab57a.png" width="700"alt="Image Error"/>
</p>

**1) Collecting Indoor data:** Indoor air data measured pollutants such as fine dust, nitrogen dioxide (NO), carbon monoxide (CO), and ozone with sensors. The measurement devices were measured using two Arduino uno and pms 5003 (dust sensor), dht 11 (temperature and humidity sensor), mq2 (gas sensor), and mq135 (gas sensor).

**2) Collecting Outdoor data:** As for indoor air measurement items, carbon monoxide CO, No2, Ozone, pm10, pm2.5 pollutants and general temperature and humidity data that can be measured by the equipped measuring device among pollutants held by the U.S. Environmental Protection Agency (EPA).

**3) Data analysis and visualization:** Both indoor air data and outdoor air data were extracted in the form of CSV files, and visualization of the extracted data was performed using the Jupyter laptop.

<br>

## 🛢 Data Structure

<p align="center">
   <img src="https://user-images.githubusercontent.com/63999666/154166751-cda74f22-55d4-4fe7-9cee-dfaab4dcb1d2.png" width="600" alt="Image Error"/>
</p>

#### Data Base Design:
Mysql was used as the database, and each schema was designed based on four actual measured Purdue University places. There are a total of five tables (=relations) in each schema. In each table, data tuples measured for 1 hour per 30 seconds per day were stored. The attributes were designed in total of four types: fine dust, temperature and humidity, carbon monoxide, nitrogen dioxide, and ozone.

__therefore, there are a total of 600 data on measured pollutants per schema. A total of four database schemas have 2,400 data__

<br>



 
## ⚙ Environment Setting

   #### Software Environment Setting
    
   ✔️macOS Big Sur version 11.5.2
    
   ✔️Arduino IDE version 1.8.19
   
   ✔️Node-RED version: v2.2.0
    
   ✔️Jupyter Notebook 3.7.9
   
   ✔️Python version 3.9
    
   #### Hardware Environment Setting
    
   ✔️Sensor : Aurduno Uno rev3, pms 5003, dht 11, mq2, mq135
    


<br>
  
## 📤 Installation

   $ git clone https://github.com/MINJILEE-PURDUE/KSW_2021_Fall_Program.git
   
   $ cd Eco_Avengers


<br>


## 🎅 👦 👩 Collaborator
     
  #### 🎅Junho Jung
  
   -Yonsei Univeristy
      
   -Major: Computer Engineering & Venture
      
   -Email: llovejune@yonsei.ac.kr
      
   -Github: https://github.com/DevelopJun

 #### 👦DuYong Chung
  
   -Yonsei Univeristy
   
   -Major: Computer Engineering & Venture
   
   -Email: endyd4@yonsei.ac.kr
   
   -Github: https://github.com/Yondubuntu

  #### 👩Qingyi Zhang
  
   -Purdue Univeristy
   
   -Major: Cyber Security
   
   -email: zhan2801@purdue.edu
   
   -github: https://github.com/Maxim-afk

