# spot
A clone of Reddit's /r/place

# Requirements

## Functional

* User (administrative) configurable canvas size
* Limited to 16 colors
* Users tracked by IP address (no accounts/logins)
* Administrative login
  * Reset the canvas
* User interface
  * Display a canvas containing all pixels
    * Assume for v1 that pan/zoom is not required
  * To update a pixel
    * Select an individual pixel
    * Select a color (perhaps remember last color)
    * Confirm to update

# Technical

* Updates to the canvas after the initial load must be in real time
* Store the server-side state of the canvas in memory
  * No persistence
* Able to run as a container
* Front end should be a single page app/simple html+js

# Decisions Made

* Users should get the full canvas when loading
  * REST
* Users should get updates in real time after loading
  * Websockets
* Users can make single-pixel updates at any time (no cooldown)
  * REST
* Ensuring consistency of the canvas
  * Sequence:
    * User loads page
    * Websocket to backend established and begins 'stashing' pixel update events
    * REST API call is made to retrieve the canvas snapshot at that moment
    * Client receives and renders the canvas snapshot
    * Client replays 'stashed' pixel update events
    * Client begins updating pixels in real time

## Tech Stack
  * Python (FastAPI for the backend)
  * Svelte (frontend)
