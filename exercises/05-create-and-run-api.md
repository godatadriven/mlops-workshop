# Create and run API locally ⚙️

In this exercise, we will create and run an API locally, which will be used to serve our model.

An API helps us bring our model to the end user. It allows us to enable end users to just send the required information to our model, such as wind speed, and they will get predictions back, without having to run our code.

## Run the application

We've already made a start with the implementation in `/turbine_power/app.py`.

Exercises:

1. Inspect the code in `/turbine_power/app.py`
2. Run the application with:
```
python turbine_power/app.py
```
3. When prompted, navigate to the given URL in your browser: [http://0.0.0.0:8080](http://0.0.0.0:8080)
4. Check out the Swagger UI by adding `/docs` to end of the URL in your browser: [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs)
5. Select the `/predict` endpoint in the UI, click "Try it out" in the top right corner, and click "Execute".
6. Scroll down to see our API's response.

## Finish the application

Our API doesn't actually *use* our model yet. Let's change that.

Exercises:

1. Open `/turbine_power/app.py` in your editor
2. Change the `/predict` endpoint to use our model
3. Try it out again in the Swagger UI!

🎉
