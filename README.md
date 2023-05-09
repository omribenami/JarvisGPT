Please ⭐ this repo if you find it useful

### ALERT!: Google decided to kill the "google Actions" on June 13th 2023, which means jarvisGPT  will soon be deprecated.



# JarvisGPT
JarvisGPT is a containerized solution to the wonderful script made by Amogh Agastya, this script allows the user to talk to chatGPT using google assistant (google Actions) by sending webhooks from the assistant to chatGPT and vise versa.


## Links 
* [betterprogramming.pub](https://betterprogramming.pub/how-to-integrate-dialogflow-with-gpt-3-creating-a-personal-virtual-mental-health-assistant-from-fee7d363993a)  - Credits and link to the instructions on how to use it.
* [Ngrok](https://github.com/shkoliar/docker-ngrok) - third party service to capture Webhooks.

## Installation
1. Follow the instructions in the * [betterprogramming.pub](https://betterprogramming.pub/how-to-integrate-dialogflow-with-gpt-3-creating-a-personal-virtual-mental-health-assistant-from-fee7d363993a) *until step 5*
2. run the following  docker compose:
```
version: "3.6"
services:
  jarvisgpt:
    image: omribenami/jarvisgpt:1.1
    container_name: jarvisgpt
    restart: always
    ports:
    - 7777:7777
    environment:
    - OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXX

```

### Environment
* OPENAI_API_KEY- is the token you created in step1 of the manual.

### NOTE!
For my method to succeed you need to expose port 7777 in your server to allow it to receive  the webhooks, if you want to do it in a more secure way (like i did) you can use Ngrok docker which gives you the ability to receive webhooks from Ngrok service without exposing your server (See the link above).





