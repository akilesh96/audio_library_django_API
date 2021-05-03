# audio_library_django_API

## Quick Start

1. clone
  
            git clone https://github.com/akilesh96/audio_library_django_API.git

2. go into directory `cd audio_library_django_API`
3. Run `pip install -r requirements.txt`
4. Then run `python manage.py runserver 0:8080`
5. Load `Postman_Collections/Audio Library.postman_collection_v1.json` into POSTMAN application
<br>
<br>
## API end points

### 1. create
    url = http://0.0.0.0:8080/content/song/add
    method = POST
    content-type = application/json
    
   - endpoints :
        - Song 
                
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

        - Podcast
            
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
                       
        - Audiobook
        
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

### 4. get details

   1. song
           
            http://0.0.0.0:8080/content/song - returns all song details
            http://0.0.0.0:8080/content/song/1 - return song 1 details
            method = GET

   2. podcast
           
            http://0.0.0.0:8080/content/podcast - returns all podcast details
            http://0.0.0.0:8080/content/podcast/1 - return podcast 1 details
            method = GET
           
   3. audiobook
           
          http://0.0.0.0:8080/content/audiobook - returns all audiobook details
          http://0.0.0.0:8080/content/audiobook/1 - return audiobook 1 details
          method = GET
    
    
### Return RESPONSE

    - Action is successful: 200 OK
    - The request is invalid: 400 bad request
    - Any error: 500 internal server error