# Install steps

Currently you can log in or sign up with any info for email and password.

To log in as admin use:

email:  admin

password: admin

There is a script that can install and run everything needed to start the web app up.
To run the startup script you need to run these two commands in your terminal from this repo:

`sudo chmod +x init.sh`
`./init.sh`

This will start up the FastAPI backend and the vite dev server to serve the frontend.

FastAPI will be served to localhost:8000

The frontend will be served to localhost:3000
