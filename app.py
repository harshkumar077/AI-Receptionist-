from flask import Flask, request, jsonify
import time
import threading
import random

app = Flask(__name__)

# Simulated emergency response database
emergency_responses = {
    "not breathing": "perform CPR by pushing firmly downwards in the middle of the chest and then releasing.",
    "bleeding": "apply pressure to the wound with a clean cloth.",
    "choking": "perform the Heimlich maneuver by standing behind the person and using your hands to exert pressure on the bottom of the diaphragm."
}

def delayed_response(emergency, callback):
    """ Simulates a delay in response from a database """
    time.sleep(15)  # Delay for 15 seconds to simulate database response time
    response = emergency_responses.get(emergency, "Call 911 immediately.")
    callback(response)

@app.route('/')
def welcome():
    return '''
    <html><head>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        h1 { color: #333; }
        form { margin-top: 20px; }
        input[type="text"], textarea { padding: 10px; width: 300px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; }
        input[type="submit"] { padding: 10px 20px; background-color: #5cb85c; color: white; border: none; border-radius: 5px; cursor: pointer; }
        input[type="submit"]:hover { background-color: #4cae4c; }
    </style>
    </head><body>
    <h1>Hello, are you having an emergency or would you like to leave a message? (emergency/message)</h1>
    <form action="/handle_input" method="post">
        <input type="text" name="text" placeholder="Enter 'emergency' or 'message'"/>
        <input type="submit" value="Submit"/>
    </form>
    </body></html>
    '''

@app.route('/handle_input', methods=['POST'])
def handle_input():
    user_input = request.form.get('text', '').lower()
    
    if user_input == 'emergency':
        return '''
        <html><body>
        What is the emergency? 
        <form action="/emergency_response" method="post">
            <input type="text" name="emergency_type" placeholder="Enter the type of emergency"/>
            <input type="submit" value="Submit"/>
        </form>
        </body></html>
        '''
    elif user_input == 'message':
        return '''
        <html><body>
        Please leave your message.
        <form action="/message" method="post">
            <textarea name="text"></textarea>
            <input type="submit" value="Submit"/>
        </form>
        </body></html>
        '''
    else:
        return "I don't understand that. Are you having an emergency or would you like to leave a message? (emergency/message)"

@app.route('/emergency_response', methods=['POST'])
def emergency_response():
    emergency_type = request.form.get('emergency_type', '').lower()
    thread = threading.Thread(target=delayed_response, args=(emergency_type, notify_user))
    thread.start()
    return f"I am checking what you should do immediately, meanwhile, can you tell me which area are you located right now?<br><form action='/location' method='post'><input type='text' name='text' placeholder='Enter your location'/><input type='submit' value='Submit'/></form>"

def notify_user(response):
    # This function would normally handle sending the response back to the user
    print("Emergency instructions: ", response)

@app.route('/message', methods=['POST'])
def message():
    user_message = request.form.get('text', '')
    return f"Thanks for the message, we will forward it to Dr. Adrin: {user_message}"

@app.route('/location', methods=['POST'])
def location():
    user_location = request.form.get('text', '')
    eta = random.randint(10, 30)  # Random ETA between 10 and 30 minutes
    return f"Dr. Adrin will be at your location in approximately {eta} minutes. Please follow the emergency instructions provided. If the situation worsens, call 911 immediately."

if __name__ == '__main__':
    app.run(debug=True)
