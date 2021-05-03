# audio_library_django_API

## Quick Start

1. clone
  
            git clone https://github.com/akilesh96/audio_library_django_API.git

2. go into directory `cd audio_library_django_API`
3. Run `pip install -r requirements.txt`
4. Then run `python manage.py runserver 0:8080`
<br>
<br>

## setup the system

1. Setup
 
    1. clone
  
            git clone https://github.com/akilesh96/audio_library_django_API.git
    2. go into directory `cd audio_library_django_API`
    3. Run `pip install -r requirements.txt`

2. Django and database connection

     Run following commands (For first time)
     1. For creating python migration files, `python manage.py makemigrations`
     2. Will create tables in DB, `python manage.py migrate`
     3. To load default data, `python manage.py loaddata fixtures/data.json`

3. Run the following command to run server
    `python manage.py runserver 0:8080`
<br>
<br>
# API end points

### 1. create
    url = http://0.0.0.0:8080/content/song/add
    method = POST
    content-type = application/json
    
   - endpoints :
        - song 
                
            request body
                
               {
                "name": "Jana Gana Mana",
                "duration": 52
                }
                
            response body

               {
                    "id": 4,
                    "name": "Jana Gana Mana",
                    "duration": 52,
                    "upload_time": "2021-05-03T11:34:28.695212Z"
               }

        - podcast
            
            request body
            
                {
                    "name": "Song Exploder",
                    "host": "Hrishikesh Hirway",
                    "participants": "The Mountain Goats, John Carpenter",
                    "duration": 5000
                }

            response body
            
                {
                    "id": 3,
                    "name": "Song Exploder",
                    "duration": 5000,
                    "upload_time": "2021-05-03T12:50:28.033518Z",
                    "host": "Hrishikesh Hirway",
                    "participants": "The Mountain Goats, John Carpenter"
                }
                       
        - audiobook
        
            request body
            
                {
	                "title": "Jana Gana Mana",
	                "author": "Rabindranath Thakur",
	                "narrator": "Rabindranath Thakur",
	                "duration": 52
                }

            response body

                {
                    "id": 3,
                    "title": "Jana Gana Mana",
                    "author": "Rabindranath Thakur",
                    "narrator": "Rabindranath Thakur",
                    "duration": 52,
                    "upload_time": "2021-05-03T12:57:23.784499Z"
                }
                    
### 2. Update

    url = http://0.0.0.0:8080/content/<audioFileType>/<audioFileID> 
    method = PUT
    content-type = application/json
- song
    
    - url : `http://0.0.0.0:8080/content/song/1`
    - request body : Same as create request body
        
- podcast
    
    - url : `http://0.0.0.0:8080/content/podcast/1`
    - request body : Same as create request body
    
- audiobook
    
    - url : `http://0.0.0.0:8080/content/audiobook/1`       
    - request body: Same as create request body

### 3. delete
  
    url = http://0.0.0.0:8080/content/<audioFileType>/<audioFileID>
    method = DELETE
    content-type = application/json
    
- song
    - url: `http://0.0.0.0:8080/content/song/1` - deletes record at id 1
- podcast
    - url: `http://0.0.0.0:8080/content/podcast/1` - deletes record at id 1
- audiobook
    - url : `http://0.0.0.0:8080/content/audiobook/1` - deletes record at id 1

### 4. get

   1. song
           
            http://0.0.0.0:8080/content/song - returns all song details
            http://0.0.0.0:8080/content/song/1 - return song 1 details

   2. podcast
           
            http://0.0.0.0:8080/content/podcast - returns all podcast details
            http://0.0.0.0:8080/content/podcast/1 - return podcast 1 details
           
   3. audiobook
           
          http://0.0.0.0:8080/content/audiobook - returns all audiobook details
          http://0.0.0.0:8080/content/audiobook/1 - return audiobook 1 details
    
    
### Return RESPONSE

    - Action is successful: 200 OK
    - The request is invalid: 400 bad request
    - Any error: 500 internal server error