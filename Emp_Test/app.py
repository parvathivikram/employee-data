from flask import Flask, request
from service import check_user

app = Flask(__name__)

# Employee signup
'''
End point implementation
API Implementation
Backend code 
'''

@app.route('/esignup/',methods = ['POST'])
def esignup():
    data = request.get_json()
    print("Data : ", data)
    print("Signup operation in Progress")

    is_exists = check_user(data['userid'], data['eid'])
    if is_exists:
        # Server side validation
        # Pass data to service layer
        return "Success"
    '''
    1. Check userid, Eid exists in db or not 
        1. If exists send error message
        2. Else pass data to service layer
    '''

    return "Success"


if __name__ == '__main__':
    app.run(host='localhost', port=4444)