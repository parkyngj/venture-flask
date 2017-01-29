'''
Imports the `app` variable from app package, and invokes the run method to start the server.
Recall that the `app` variable holds the Flask instance that we created above.
'''
from app import app
app.run(debug = True)
