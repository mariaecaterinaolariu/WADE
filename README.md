# WADE - Project for Web Application Development
Project: 
Develop an extensible microservice-based system able to perform processing tasks such as browsing, smart faceted searching & filtering, etc. Adopting both deep learning (or machine learning) techniques – for example, a public REST API like DeepDetect – and semantic Web technologies, the platform will be able to generate various visualizations (e.g., semantic zoom), correlations, classifications, and recommendations exposed via a SPARQL endpoint. Also, a comparison study will be provided to explain the obtained results. Additional info: An Introduction to Data Visualization.
## Team: SuperMarIo - Ioana-Malina Pinzariu & Maria-Ecaterina Olariu

## Table of Contents
[About the Project](#about-the-project)
  * [Documentation](#documentation)
  * [Tech Stack](#tech-stack)
  * [Frontend](#frontend)
  * [Backend](#backend)
  * [Process](#process)
  * [Screenshots](#screenshots)
  * [Acknowledgements](#acknowledgements)


## About the project

Our project is an application that showcases portraits from 1900 to 1950 and provides data analysis and visualization based on the features of the paintings and the painters. We use the Kaggle dataset of portraits as our main source of data, and we enrich it with the DeepFace library that extracts the age, gender, race and emotion of the people in the portraits. We also use the Wikipedia API to obtain information about the painters, such as their biography, lifespan and artistic style. We store all the data in a Mongo database and expose it through a SPARQL endpoint. Our application allows users to browse the portraits in a gallery view, with options to filter, sort and search by various criteria. Users can also click on any portrait to see more details about the painter, including a correlation graph that shows the relationship between different attributes of their paintings. Additionally, users can contribute to our database by uploading their own portraits of the painters and providing the name of the painter. We will then use the DeepFace library to generate the data for the uploaded portraits and save them in our database. Our project aims to create a rich and interactive experience for users who are interested in exploring the portraits and painters from the early 20th century.

### Documentation - Scholarly HTML
Please access the folder Midterm Deliverables:
add link here

### Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
  </ul>
</details>

<details>
  <summary>Backend</summary>
  <ul>
    <li><a href="https://dotnet.microsoft.com/en-us/">.NET</a></li>
    <li><a href="https://flask.palletsprojects.com/en/3.0.x/">Flask</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details>
<summary>Cloud</summary>
  <ul>
    <li><a href="">TBA</a></li>
  </ul>
</details>


### Frontend
A brief description of the user interface:

- Gallery View, similar to Pinterest. Perhaps, hovering on each photo should show brief info about it such as: Artist and clicking on it will get you to a page about the artist and the photos of the artist. 
- Page about the artist: Featuring a short description of the artist, the page will contain a correlation graph with data such as ages, emotions, genders or races of the paintings done by this painter. 
- The main page will have filters similar to what we see on websites like altex.ro, filtering being done based on artist, emotion, gender, race or age of the person in the painting.
- With further processing of the wikipedia page of the painter perhaps we can extract the era / style / movement of the artist and create a filter with that.


### Backend
- Dataset: https://www.kaggle.com/datasets/deewakarchakraborty/portrait-paintings/data
- DeepFace library: https://pypi.org/project/deepface/
- Wikipedia API: https://en.wikipedia.org/api/rest_v1/ 

### Process
- Searched for dataset
- Looked for free API's for image processing
- Tested some API's and deciding over DeepFace
- Brainstormed a User Interface to fit the purpose of application
- Worked with DeepFace to check functionalities and limitations - Maria
- Tried to work with RDF for laboratory work - Ioana
- #### Google Docs document we used as communication: 
https://docs.google.com/document/d/1eiILmaOmAqXWwFkbKdkbUL31oG1_d0Qs_mqRMkXkD2k/edit

### Screenshots
Data from DeepFace:
- Example with a portrait and data returned:
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
- Example of two people portrait and where faces are detected
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
- Example of limitations:
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

### Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
