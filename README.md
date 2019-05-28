# innovationartsbackend
Creating an API with Flask and AWS

## Description

This app allows the user to create an API. It has the following features:
* Users can upload a JSON string to S3 using a POST request
* Users can view this JSON string from S2 using a GET request.

## Tech Stack

Python 3.7.2, Flask, Boto3, AWS S3

**Deployment**

AWS Lambda with Zappa

## Quickstart

```bash
$ git clone https://github.com/matharotheelf/Saved_game

```
To see the widget run the file index.html in any browser.

To run the tests run the file SpecRunner.html in any browser.

## How to Use

When on the page of the app, press "Complete Game" to complete the 'game'.

Then you can press "Restart Game" to restart the 'game'.

To save the progress of the 'game' as either complete or incomplete press "Save Game". This means when you re-open the page later in the same browser you will find the 'game' in the same state.

## User Stories
```
As a User 
So I can complete my 'game', I can press a "Complete Game" button which completes my 'game'.
So I can restart my 'game', I can press a "Restart Game" button which restarts my 'game'.
So I can save my 'game', I can press a "Save Game" button which stores my 'game' status to local storage.

```

## Screenshots

**App When Game Incomplete**

<img width="649" alt="Screen Shot 2019-05-21 at 12 45 33" src="https://user-images.githubusercontent.com/44533664/58093811-376b5480-7bc7-11e9-8012-4426f85f2d36.png">

**App When Game Complete**

<img width="625" alt="Screen Shot 2019-05-21 at 12 45 47" src="https://user-images.githubusercontent.com/44533664/58094032-a5178080-7bc7-11e9-8324-c638627535ca.png">

## References

To display whether game is complete or incomplete: 

https://stackoverflow.com/questions/3961422/conditional-display-of-html-element-forms

https://stackoverflow.com/questions/2928688/how-to-hide-elements-without-having-them-take-space-on-the-page

https://stackoverflow.com/questions/17630945/is-there-an-opposite-to-displaynone

To create buttons: 

https://www.w3schools.com/jsref/event_onclick.asp

To format the user interface:

https://css-tricks.com/almanac/properties/t/text-align/

https://www.w3schools.com/css/css_font.asp

https://www.w3schools.com/css/css3_buttons.asp

https://stackoverflow.com/questions/3622756/button-center-css

https://stackoverflow.com/questions/15438774/give-space-above-and-below-a-div

## Contributors 

[Tom Lawrence](https://github.com/matharotheelf)  

## How to Contribute

If you want to improve this project and see your name added to the above list of contributors, simply branch this repo, change the code, and make a pull request back to this repo explaining the contributions you made.
