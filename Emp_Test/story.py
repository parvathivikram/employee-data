'''
Controller: Load data, Validation,
Service   : Business Logic
DAO       : Interact with DB and perform CRUD ops
'''

'''
Story:
============
1. SignUp  CREATE
------------------
 - Employee will give his details and his account should get created.
      FirstName    
      LastName   
      EId *
      UserId * 
      Password
      MobileNo
      EmailID
      DOB
      Address
      Gender M F T   Male Female Transgender
      DOJ
      Technology

    - Output should be 
        If Success: Employee ID created succsefully.
                    Login with your credentials
           Failure : Display error message


API Call:
--------------
Request URL     : http://localhost:8034/esignup
Request Method  : POST
Payload         : {json format}


      

2. Signin  RETRIEVE
3. Update Password   UPDATE
4. Deactivate account DELETE



'''