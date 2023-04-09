# REST API Docs

Here you can find the rest api documentation in `HAR` and Insomnia Client format.

These files can be used in Insomnia and other HTTP Client tools to test the demo inference api.

## Demo 
The Demo inference api is hosted at:
https://pythoninternship.rakeshs.eu.org/

### API Enpoints:
 
- `/posts/get` - Get Posts
  - `lat` _(required)_ - query parameter to filter posts by latitude 
  - `lon` _(required)_ - query parameter to filter posts by longitude
  - `distance` _(optional)_ - query parameter to provide the distance radius in `Km`
  - `page` _(optional)_ - query parameter to provide page number (default: is `1`)
  - `per_page` _(optional)_ - query parameter to provide number of posts per page (default: `10`)


- `/posts/new` - New Post
  - `content` _(required in json body)_ - Content of the post
  - `lat` _(required in json body)_ - Latitude of the post
  - `lon` _(required in json body)_ - Longitude of the post


- `/weather/get` - Get Posts
    - `lat` _(required)_ - query parameter to find weather by latitude
    - `lon` _(required)_ - query parameter to find weather by longitude

## Try Out Live

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Python%20SDE%20Internship%202023&uri=https%3A%2F%2Fgithub.com%2FCypherpunkSamurai%2Fflask-restapi%2Fblob%2Fmaster%2Fdocs%2Frest_api_definition.insomnia.json)

