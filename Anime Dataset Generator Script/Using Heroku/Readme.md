# How to use Anime Dataset Generator

This script can be used to download anime dataset from [**Myanimelist**](https://myanimelist.net/) using an unofficial MyAnimeList REST API, [**Jikan**](https://jikan.me/docs).

#### Column metadata:

* animeID: id of anime as in anime url [https://myanimelist.net/anime/<span style="color:red">**1**</span>](https://myanimelist.net/anime/1)
* name: title of anime
* premiered: premiered on. default format (season year) 
* genre: list of genre
* type: type of anime (example TV, Movie etc) 
* episodes: number of episodes
* studios: list of studio
* source: source of anime (example original, manga, game etc) 
* scored: score of anime
* scoredBy: number of member scored the anime
* members: number of member added anime to their list

### Using Heroku

* Before doing this I will request you to watch this video - [Google Sheets and Python](https://youtu.be/vISRn5qFrkM). Here we are using this concept as a base. I just integrated this with heroku.

* First you need to visit [this link](https://console.developers.google.com/cloud-resource-manager) to create a project inside Google cloud resource manager.

* Click **CREATE PROJECT**, then give it a name. [If below gif is low quality, then click here](https://gfycat.com/gifs/detail/VibrantQuarterlyFieldmouse).


![](demo/createProject.gif)

* Now you need to enable Google sheet API for your project.

![](demo/enableAPI.gif)

* Next you need to get credential file. [If below gif is low quality, then click here](https://gfycat.com/gifs/detail/InsecureExcellentImpala).

![](demo/createClientScretJSON.gif)

* [Get files for deployment here](https://github.com/Dibakarroy1997/myanimelist-data-set-creator/tree/master/Anime%20Dataset%20Generator%20Script/Using%20Heroku).

* Add client_secret.json and give access to the spreadsheet. Spreadsheet contains header, which you need to add. [Watch how to do that here](https://youtu.be/M-q0ptxOJB0).

* Before deploying to Heroku. You need to create an app. [If below gif is low quality, then click here](https://gfycat.com/gifs/detail/AggressiveParallelDevilfish).

![](demo/preDeploy.gif)

* At last just push to heroku master and start the worker dyno. [Watch how to do that here](https://youtu.be/BvlCLwEMKHg)

**NOTE**: If the worker doesn't starts amnually, you can start it using the following command: **heroku ps:scale worker=1**

* Final Product:

![](demo/herokuFinal.gif)